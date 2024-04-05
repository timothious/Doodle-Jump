import pygame
from src.states.State import State
from src.spaceship import Spaceship
from lib.utils import draw_text
from src.config import *
from src.states.PlayState import PlayState


class StartState(State):
    def __init__(self, assets):
        self.assets = assets
        self.spaceships = []
        self.play_flag = None
        self.menu_flag = None
        self.score_flag = None
             
    def load(self):

        #-----------------------------background image---------------------------------
        self.backgroundImg = self.assets['images']['background']
        self.starttext = self.assets['images']['doodle-jump']
        self.starttext = pygame.transform.smoothscale(self.starttext, (404, 92))

        #------------------Space ship---------------------------------
        self.spaceship_img_1 = self.assets['images']['spaceship_1']
        self.spaceship_img_2 = self.assets['images']['spaceship_2']

        spaceship_1 = [self.spaceship_img_1, 178, 146]  
        spaceship_2 = [self.spaceship_img_2, 178, 146]
        space_list = [spaceship_1,spaceship_2]
        s = Spaceship(space_list,top_right_offset=(10, 10))

        self.spaceships.append(s)

        self.backgroundfooter = self.assets['images']['atlas-2']
        footer_rect = pygame.Rect(1, 400, 700, 100)
        self.footer_part = self.backgroundfooter.subsurface(footer_rect)

        #------------------play button------------------------------
        self.playbutton = self.assets['images']['play']
        self.playbutton = pygame.transform.smoothscale(self.playbutton, (222, 80))
        self.playbutton_rect = self.playbutton.get_rect()
        self.playbutton_rect.center = (VIRTUAL_WIDTH // 2, VIRTUAL_HEIGHT // 2)

        self.playbutton_on = self.assets['images']['play-on']
        self.playbutton_on = pygame.transform.smoothscale(self.playbutton_on, (222, 80))
        self.playbutton_on_rect = self.playbutton_on.get_rect()
        self.playbutton_on_rect.center = (VIRTUAL_WIDTH // 2, VIRTUAL_HEIGHT // 2)

        #----------------------Bug---------------------------------
        # Bug 1 (Blue)
        self.bug = self.assets['images']['bottom-bug-tiles']
        bug_1 = pygame.Rect(645, 45, 50, 45)
        self.bu_1_part = self.bug.subsurface(bug_1)
        # Bug 2 (Green)
        bug_2 = pygame.Rect(645, 5, 50, 40)
        self.bu_2_part = self.bug.subsurface(bug_2)
        # Bug 3 (Flying Bug Blue)
        bug_3 = pygame.Rect(690, 5, 80, 40)
        self.bu_3_part = self.bug.subsurface(bug_3)
        # Bug 4 (Orange)
        bug_4 = pygame.Rect(690, 45, 80, 47)
        self.bu_4_part = self.bug.subsurface(bug_4)

        #-------------------------------Menu-------------------------
        self.start_end_tiles = self.assets['images']['atlas-2']
        self.menu_rect = pygame.Rect(0,100,230,150)
        self.menu = self.start_end_tiles.subsurface(self.menu_rect)
        self.menu_rect.center = ((VIRTUAL_WIDTH - self.starttext.get_width() - 200)+100 , (VIRTUAL_HEIGHT // 2 - self.playbutton.get_height() // 2) + (self.playbutton.get_height() + 200) )

        self.menu_on = self.assets['images']['menu-on'] 
        self.menu_on = pygame.transform.smoothscale(self.menu_on, (224, 82))
        self.menu_on_rect = self.menu_on.get_rect()
        self.menu_on_rect.center = (VIRTUAL_WIDTH // 2, VIRTUAL_HEIGHT // 2)
        #-------------------------------Score------------------------
        self.score = self.assets['images']['score']
        self.score = pygame.transform.smoothscale(self.score, (222, 80))
        self.score_rect = self.score.get_rect()
        self.score_rect.center = ((VIRTUAL_WIDTH - self.starttext.get_width() - 200)+350,(VIRTUAL_HEIGHT // 2 - self.playbutton.get_height() // 2) + (self.playbutton.get_height() + 200))
        
        # Score On
        self.score_on = self.assets['images']['score-on']
        self.score_on = pygame.transform.smoothscale(self.score_on, (222, 80))
        self.score_on_rect = self.score_on.get_rect()

        #----------------------------Back-Ground Music---------------
        self.bg_music = self.assets['sounds']['background']
        self.bg_music.play(loops=-1)




    def unload(self):
        self.bg_music.stop()

    def init(self):
        self.timer = 0.0
 

        

    def free(self):
        pass

    def pause(self):
        pass
    
    def resume(self):
        pass
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Scale mouse position to match virtual resolution
            scaled_mouse_pos = (
                event.pos[0] * VIRTUAL_WIDTH // WINDOW_WIDTH,
                event.pos[1] * VIRTUAL_HEIGHT // WINDOW_HEIGHT
            )

            # Check if the mouse click is on the play button
            if self.playbutton_rect.collidepoint(scaled_mouse_pos):
                print("Play button clicked!")  # Debug message
                self.play_flag = True 
                self.timer = 0.2
                #self.stateManager.changeState(self.stateManager.ready_states["Play"](self.assets)) 

            # Check if the mouse click is on the menu button
            elif self.menu_rect.collidepoint(scaled_mouse_pos):
                print("Menu button clicked!")  # Debug message
                self.menu_flag = True 
                self.timer = 0.2 
            
            elif self.score_rect.collidepoint(scaled_mouse_pos):
                print("Score button clicked!")  # Debug message
                self.score_flag = True 
                self.timer = 0.2 
            
            # Debug mouse position and collision detection
            print("Mouse position:", event.pos)
            print("Scaled mouse position:", scaled_mouse_pos)
            print("Play button rectangle:", self.playbutton_rect)
            print("Menu button rectangle:", self.menu_rect)

    def is_paused(self):
        """
        Checks if the state is currently paused.
        
        Returns:
            bool: True if the state is paused, False otherwise.
        """
        pass


    def update(self, dt):
        
        self.timer -= dt
        for spaceship in self.spaceships:
            spaceship.update()
        if self.play_flag and self.timer <= 0:
               self.stateManager.changeState(PlayState(self.assets))
        if self.menu_flag and self.timer <= 0:
                self.stateManager.changeState(self.stateManager.ready_states["Menu"](self.assets))
        elif self.score_flag and self.timer <= 0:
                self.stateManager.changeState(self.stateManager.ready_states["Score"](self.assets))

    def render(self, virtual_screen, dt=0.0):
        # Draw the background image
        scaled_background = pygame.transform.scale(self.backgroundImg, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        virtual_screen.blit(scaled_background, (0, 0))

        # Calculate the position for doodle-jump.png (right side)
        doodle_jump_x = VIRTUAL_WIDTH - self.starttext.get_width() - 200 
        doodle_jump_y = 100
        virtual_screen.blit(self.starttext, (doodle_jump_x, doodle_jump_y))

        # Calculate the position for play.png (next row, aligned to the right)
        play_x = (VIRTUAL_WIDTH - self.playbutton.get_width()) // 2
        play_y = VIRTUAL_HEIGHT // 2 - self.playbutton.get_height() // 2

        # Draw the play button
        if self.play_flag :
            virtual_screen.blit(self.playbutton_on, (play_x, play_y))
        else:
            virtual_screen.blit(self.playbutton, (play_x, play_y))

        #--------------------Bug Calculations---------------------------
        # Calculate the position for bug_1
        bug_1_x = doodle_jump_x + 50 

        bug_1_y = doodle_jump_y + self.starttext.get_height() + 500  


        # Draw bug_1
        virtual_screen.blit(self.bu_1_part, (bug_1_x, bug_1_y))

        # Calculate the position for bug_2
        bug_2_x = doodle_jump_x + 150 
        bug_2_y = doodle_jump_y + self.starttext.get_height() + 150  

        # Draw bug_2
        virtual_screen.blit(self.bu_2_part, (bug_2_x, bug_2_y))

        # Calculate the position for bug_3
        bug_3_x = doodle_jump_x + 250 
        bug_3_y = doodle_jump_y + self.starttext.get_height() + 400  

        # Draw bug_3
        virtual_screen.blit(self.bu_3_part, (bug_3_x, bug_3_y))

        bug_4_x = doodle_jump_x + 400 
        bug_4_y = doodle_jump_y + self.starttext.get_height() + 200  

        # Draw bug_4
        virtual_screen.blit(self.bu_4_part, (bug_4_x, bug_4_y))



        #---------------------------Menu-------------------------
        menu_x = doodle_jump_x + 100 
        #menu_y = doodle_jump_y + self.starttext.get_height() + 600
 
        menu_y = play_y + self.playbutton.get_height() + 200  # Adjust as needed




        # Draw menu
        virtual_screen.blit(self.menu, (menu_x, menu_y))

        score_x = menu_x + 250 
        score_y = menu_y  

        # Draw score
        virtual_screen.blit(self.score, (score_x, score_y))

        # Draw the menu button
        if self.menu_flag :
            virtual_screen.blit(self.menu_on, (menu_x, menu_y))
        else:
            virtual_screen.blit(self.menu, (menu_x, menu_y))

        # Draw the Score button
        if self.score_flag :
            virtual_screen.blit(self.score_on, (score_x, score_y))
        else:
            virtual_screen.blit(self.score, (score_x, score_y))


        # Draw the footer image at the bottom of the window
        footer_x = 0  
        footer_y = VIRTUAL_HEIGHT - self.footer_part.get_height()  
        virtual_screen.blit(self.footer_part, (footer_x, footer_y))




        # Draw spaceships
        for spaceship in self.spaceships:
            spaceship.draw(virtual_screen)