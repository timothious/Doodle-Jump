
import pygame
from src.states.State import State
from lib.utils import *
from src.config import *



class LoadState():

    def __init__(self, assets):
        self.assets = assets
        
#--------------------------------------------------------------------------------------------------

    def load(self):
        # Fonts:
        self.assets['font'] = {}
        self.assets['font']['Large'] = pygame.font.Font('assets/fonts/font.ttf', 64)
        self.assets['font']['medium'] = pygame.font.Font('assets/fonts/font.ttf', 50)
        self.assets['font']['small'] = pygame.font.Font('assets/fonts/font.ttf', 32)

        

        pygame.mixer.init()
        # Sounds:
        self.assets['sounds'] = {}
        self.assets['sounds']['bijeli'] = pygame.mixer.Sound(r'assets/sounds/bijeli.wav')
        self.assets['sounds']['feder'] = pygame.mixer.Sound(r'assets/sounds/feder.wav')
        self.assets['sounds']['jump'] = pygame.mixer.Sound(r'assets/sounds/jump.wav')
        self.assets['sounds']['lomise'] = pygame.mixer.Sound(r'assets/sounds/lomise.wav')
        self.assets['sounds']['pada'] = pygame.mixer.Sound(r'assets/sounds/pada.wav')
        self.assets['sounds']['propeller'] = pygame.mixer.Sound(r'assets/sounds/propeller.wav')
        self.assets['sounds']['trampoline'] = pygame.mixer.Sound(r'assets/sounds/trampoline.wav')
        self.assets['sounds']['background'] = pygame.mixer.Sound(r'assets/sounds/theme.wav')

        # Images:
        self.assets['images'] = {}
        self.assets['images']['background'] = pygame.image.load('assets/images/bck.png')
        self.assets['images']['cancel-on'] = pygame.image.load('assets/images/cancel-on.png')
        self.assets['images']['cancel'] = pygame.image.load('assets/images/cancel.png')
        self.assets['images']['doodle-jump'] = pygame.image.load('assets/images/doodle-jump.png')
        self.assets['images']['bottom-bug-tiles'] = pygame.image.load('assets/images/bottom-bug-tiles.png')
        self.assets['images']['atlas'] = pygame.image.load('assets/images/game-tiles.png')
        self.assets['images']['atlas-2'] = pygame.image.load('assets/images/start-end-tiles.png')
        self.assets['images']['play'] = pygame.image.load('assets/images/play.png')
        self.assets['images']['play-on'] = pygame.image.load('assets/images/play-on.png')
        self.assets['images']['spaceship_1'] = pygame.image.load('assets/images/spaceship_1.png')
        self.assets['images']['spaceship_2'] = pygame.image.load('assets/images/spaceship_2.png')
        self.assets['images']['menu-on'] = pygame.image.load('assets/images/menu-on.png')
        self.assets['images']['score'] = pygame.image.load('assets/images/scores.png')
        self.assets['images']['score-on'] = pygame.image.load('assets/images/scores-on.png')
        self.assets['images']['spring'] = pygame.image.load('assets/images/springshoes-side.png')
        self.assets['images']['Score_bar'] = pygame.image.load('assets/images/top-score.png')
        self.assets['images']['Loading_score'] = pygame.image.load('assets/images/loading-scores.png')

        self.assets['Player'] = {}
        self.assets['Player']['player_1'] = pygame.image.load('assets/images/lik-right.png')
        '''
        # Quads:
        self.assets['quads'] = {}
        self.assets['quads']['paddle'] = GenerateQuadsPaddles()
        self.assets['quads']['balls'] = GenerateQuadsBalls()
        # Calculate the number of tiles in the spritesheet
        sheet_width = self.assets['images']['atlas'].get_width() // TILE_WIDTH
        sheet_height = self.assets['images']['atlas'].get_height() // TILE_HEIGHT
        self.assets['quads']['bricks'] = GenerateQuadsBricks(sheet_width, sheet_height)

        '''
        print(self.assets)


#--------------------------------------------------------------------------------------------------
    
    def unload(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def init(self):
        self.timer = 0.0
        
#--------------------------------------------------------------------------------------------------
    
    def free(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def pause(self):
        pass
    
#--------------------------------------------------------------------------------------------------
    
    def resume(self):
        pass

#--------------------------------------------------------------------------------------------------
    
    def handle_event(self, event):
        pass

#--------------------------------------------------------------------------------------------------
    
    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
             self.stateManager.changeState(self.stateManager.available_states["play"](self.assets))
    
#--------------------------------------------------------------------------------------------------
    
    def render(self, virtual_screen, dt=0.0):
        # Clear the screen
        virtual_screen.fill((0, 0, 0))
        # Draw the title of the game
        

#--------------------------------------------------------------------------------------------------
