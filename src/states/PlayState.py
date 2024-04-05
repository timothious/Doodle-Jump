import pygame
from src.states.State import State
from src.config import *
from src.Stages import *
from src.Player import character
import time
import random
from lib.utils import *


class PlayState(State):
    def __init__(self, assets):
        self.assets = assets
        self.screen_y_offset = 0  
        self.scroll_speed = 5
        

    def load(self):
        self.isPaused = False
        self.backgroundImg = self.assets['images']['background']
        self.platforms = [Plain_Platform(self.assets, 100, VIRTUAL_HEIGHT - 35)]
        self.next_platform_y = VIRTUAL_HEIGHT - 100 
        self.player = character(self.assets)
        self.loos_sound = self.assets['sounds']['pada']
        self.status_Bar = self.assets['images']['Score_bar']
        self.jump = self.assets['sounds']['jump']
        self.jump_high = self.assets['sounds']['propeller']
        bar_rect = pygame.Rect(0,0,800,80)
        self.score_Bar = self.status_Bar.subsurface(bar_rect)
        self.font = self.assets['font']['Large']
        self.loading_score = self.assets['images']['Loading_score']
        

    def unload(self):
        pass

    def init(self):
        print("Initializing player character...")
        self.player = character(self.assets)
        
        print("Player character initialized. Loose state:", self.player.lost)
        self.player.jump(20)

    def free(self):
        pass

    def pause(self):
        self.isPaused = True
    
    def resume(self):
        self.isPaused = False
    
    def write_score(self, file_name, score):
        with open(file_name,"w+") as f:
            f.write(str(score))
    
    def update_player_score(self, player_scores, new_player, new_score):
        player_scores.append([new_player, new_score])
        player_scores.sort(key=lambda x: x[1], reverse=True)
        return player_scores 
    
    def read_file(self,file_name):
        lst = []
        with open(file_name, "r+") as f:
            file = f.readlines()
            for i in file:
                data = i.rstrip("\n").split(":")
                data[1] = int(data[1])
                lst.append(data)
        return lst
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.stateManager.changeState(self.stateManager.ready_states["Score"](self.assets))
            
    def Generate_Platform(self):
        if self.platforms:
            plat = self.platforms[-1]
            while plat.y > 15:
                x = plat.y - PLATFORM_Y_GAP
                variable = x - PLATFORM_Y_GAP - 30
                new_plat_y = random.randint(min(int(x), int(variable)), max(int(x), int(variable)))
                new_plat_x = random.randint(15, VIRTUAL_WIDTH - plat.width - 15)
                if variable > 0:
                    var = random.randint(1, 30)
                    if var > 5:
                        if var > 10:
                            new_platform = Plain_Platform(self.assets, new_plat_x, new_plat_y)
                        else:
                            new_platform = Moving_Platform(self.assets, new_plat_x, new_plat_y)
                    else:
                        if var == 3:
                            
                            new_platform = Jump_Platform(self.assets, new_plat_x, new_plat_y)
                        else:
                            new_platform = Broken_platform(self.assets, new_plat_x, new_plat_y)
                        if var == 2:
                            new_platform = lava_platform(self.assets, new_plat_x,new_plat_y)

                    self.platforms.append(new_platform)
                    plat = new_platform
                else:
                    break

    def remove_platforms(self):
        for i in self.platforms:
            if i.y > VIRTUAL_HEIGHT:
                self.platforms.remove(i) 
                
    def update_scores(self, file_name, lst):
        
        lst.sort(key=lambda x: x[1], reverse=True)
        top_10_scores = lst[:10]

        # Write the top 10 scores to the file
        with open(file_name, "w+") as file:
            for player_score in top_10_scores:
                file.write(f"{player_score[0]}:{player_score[1]}\n")
    
    def update(self, dt):
        if not self.is_paused():
            #print("Player loose state (before update):", self.player.loose)
            if self.player.lost == True:
                #print("Player has lost the game.")
                self.loos_sound.play()

                self.write_score(r"Last_score.txt",self.player.score)
                lst_score_file = self.read_file("score.txt")
                score = self.update_player_score(lst_score_file,"player",self.player.score)
                self.update_scores("score.txt",score)
                self.stateManager.changeState(self.stateManager.ready_states["Finish"](self.assets))

        self.player.update(dt)

        for platform in self.platforms:
            platform.update(dt)
        play_sound = self.player.check_collision(self.platforms)
        if play_sound!= False and play_sound>=40:
            self.jump.play()
            self.jump_high.play()
        elif play_sound !=  False and play_sound<40:
            self.jump.play()
        if self.player.is_hit():
                for platform in self.platforms:
                    platform.move_down(self.player.dy,dt)
        self.Generate_Platform()
        self.remove_platforms()
        if self.player.lost:
                self.screen_y_offset -= self.scroll_speed
                for platform in self.platforms:
                    platform.y -= (self.scroll_speed + 100)
                self.player.y -= self.scroll_speed
        else:
                # Scroll the screen up as usual when player hasn't lost
                if self.player.y < VIRTUAL_HEIGHT // 2:
                    self.screen_y_offset += self.scroll_speed
                    for platform in self.platforms:
                        platform.y += self.scroll_speed
                    self.player.y += self.scroll_speed

        self.player.check_collision(self.platforms)

        self.player.check_collision(self.platforms)
        #player character dimensions
        #print("Player Character Width:", self.player.width)
        #print("Player Character Height:", self.player.height)

        #for platform in self.platforms:
        #    print("Platform Width:", platform.width)
        #    print("Platform Height:", platform.height)

    def is_paused(self):
        """
        Checks if the state is currently paused.
        
        Returns:
            bool: True if the state is paused, False otherwise.
        """
        return self.isPaused

    def render(self, virtual_screen, dt=0.0):
        
        scaled_background = pygame.transform.scale(self.backgroundImg, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        virtual_screen.blit(scaled_background, (0, 0))
        
        for platform in self.platforms:
            platform.render(virtual_screen)
        self.player.render(virtual_screen)
        
        #--------------------Bug Calculations---------------------------
        # Calculate the position for score bar
        virtual_screen.blit(self.score_Bar, (0, 0))

        # Render score on top left corner over the score bar
        score_text = self.font.render(f"Score: {self.player.score}", True, (0, 0, 0))
        virtual_screen.blit(score_text, (5, 3))

        

        


