import pygame
from src.states.State import State
from src.config import *
from lib.utils import draw_text


class MenuState(State):
    def __init__(self,assets):
        self.assets = assets
        self.backgroundImg = self.assets['images']['background']
        self.font = self.assets['font']['Large']
        self.md_font = self.assets['font']['medium'] 
        self.button_music = self.assets['sounds']['trampoline']
        

    #--------------------------------------------------------------------------------------------------

    def load(self):
        # background image
        self.backgroundImg = pygame.image.load('assets/images/bck.png')


    def unload(self):
        pass

    #--------------------------------------------------------------------------------------------------

    def init(self):
        # initialize the highlighted menu item
        self.highlighted = 1

    #--------------------------------------------------------------------------------------------------

    def free(self):
        pass

    #--------------------------------------------------------------------------------------------------



    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the return key
                if self.highlighted == 1:
                    self.stateManager.changeState(self.stateManager.ready_states["Score"](self.assets))
                elif self.highlighted == 2:
                    self.stateManager.changeState(self.stateManager.ready_states["Start"](self.assets))
                elif self.highlighted == 3:
                    self.stateManager.changeState(self.stateManager.ready_states["Start"](self.assets))
            elif event.key == pygame.K_UP:  
                # Handle the up arrow key
                if self.highlighted == 1:
                    self.highlighted = 3
                else:
                    self.highlighted -= 1
                self.button_music.play()
            elif event.key == pygame.K_DOWN:
                # Handle the down arrow key
                if self.highlighted == 3:
                    self.highlighted = 1
                else:
                    self.highlighted += 1
                self.button_music.play()


    #--------------------------------------------------------------------------------------------------
   

    def render(self, virtual_screen, dt=0.0):
        # Draw the background image
        scaled_background = pygame.transform.scale(self.backgroundImg, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        virtual_screen.blit(scaled_background, (0, 0))


        
        color = (0, 0, 0)
        # Check if the first menu item is highlighted
        if self.highlighted == 1:
            # Change the color to indicate that it is highlighted
            color = (255, 0, 0)
        # Draw the 'START' menu item
        draw_text('HIGHSCORE', self.md_font, VIRTUAL_WIDTH / 2, 350, color, virtual_screen)
        # Reset the color to the default
        color = (0, 0, 0)
        # Check if the second menu item is highlighted
        if self.highlighted == 2:
            # Change the color to indicate that it is highlighted
            color = (255, 0, 0)
        # Draw the 'HIGH SCORES' menu item
        draw_text('CHARACTER SELECT', self.md_font, VIRTUAL_WIDTH / 2, 425, color, virtual_screen)

        color = (0, 0, 0)
        # Check if the second menu item is highlighted
        if self.highlighted == 3:
            # Change the color to indicate that it is highlighted
            color = (255, 0, 0)
        # Draw the 'HIGH SCORES' menu item
        draw_text('MAIN MENU', self.md_font, VIRTUAL_WIDTH / 2, 500, color, virtual_screen)


