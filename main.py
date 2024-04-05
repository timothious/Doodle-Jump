import pygame
import sys
from src.config import *
from src.StateManager import StateManager
from src.states.LoadState import LoadState
from lib.utils import *

# Global game state variables
virtual_screen = None
window = None
clock = None
last_time = 0
stateManager = None
music = None
small_font = None
assets = {}

def load():
    '''
    This function loads game resources: the game window, fonts, and game objects etc.
    '''
    global window, virtual_screen, clock, stateManager, music, small_font, assets

    # Initialize pygame
    pygame.init()

    # Create game window of size WINDOW_WIDTH x WINDOW_HEIGHT
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Set window title
    pygame.display.set_caption('Doodle Jump')
    
    # Create a virtual screen to draw on before scaling to the window size
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

    # The Clock object is responsible for keeping track of time and 
    # regulating the frame rate. It provides methods like tick() to 
    # control the frame rate and measure the time between frames.
    clock = pygame.time.Clock()

    # Initialize the StateManager
    stateManager = StateManager()

    # Load the game music
    #music = pygame.mixer.music.load('assets/sounds/music.wav')

    # Load small font for FPS
    small_font = pygame.font.Font('assets/fonts/font.ttf', 8)

    load_state = LoadState({})
    load_state.load()  # Call the load method to populate the assets dictionary
    assets = load_state.assets 
    
    if assets:
        print("Assets loaded successfully!")
        print("Number of assets loaded:", len(assets))
    else:
        print("No assets loaded!")

def init():
    '''
    This function initializes the game state variables.
    Note that everything was loaded earlier in the load() function.
    '''
    global stateManager, assets

    # Play the music
    # -1 makes the music play indefinitely in a loop; use 0 to play it just once
    #pygame.mixer.music.play(-1)
    
    # Change the current state to StartState
    #stateManager.changeState(PlayState(assets))
    stateManager.changeState(stateManager.ready_states["Start"](assets))

def render(dt):
    # Draw the current state
    stateManager.render(virtual_screen, dt)
    # Scale the virtual screen to the window size
    scale_to_window()

def scale_to_window():
    # Scale the virtual screen surface to the window size
    # If you want to keep the pixelated look:
    scaled_surface = pygame.transform.scale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # If you want to smooth things out:
    #scaled_surface = pygame.transform.smoothscale(virtual_screen, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_surface, (0, 0))

def handle_input(dt):
    pass

def update(dt):
    stateManager.update(dt)

def main():
    global last_time, stateManager, running

    # Load game resources
    load()
    # Initialize game state variables
    init()

    running = True
    last_time = pygame.time.get_ticks() / 1000.0

    while running:
        current_time = pygame.time.get_ticks() / 1000.0
        dt = current_time - last_time
        last_time = current_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE key pressed")
                    running = False
            stateManager.handle_event(event)
        # Print the current state
        if stateManager.current_state:
            print("Current State:", stateManager.current_state.__class__.__name__)


        
        handle_input(dt)
        update(dt)
        render(dt)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
