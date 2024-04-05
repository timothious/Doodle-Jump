'''
    Python port of the Harward's GD50 course
    https://cs50.harvard.edu/games/2018/

    Ported by:  Fakhir Shaheen
    Website:    https://fakhirshaheen.com/
    github:     https://github.com/fakhirsh
    linkedin:   https://www.linkedin.com/in/fakhirshaheen/
'''

from src.states.StartState import StartState
from src.states.PlayState import PlayState
from src.states.ScoreState import ScoreState
from src.states.MenuState import MenuState
from src.states.FinishState import Finish

# StateManager - a state machine manager
# Define the StateMachine class to manage different game states
class StateManager:
    def __init__(self):
        self.states = []           
        self.ready_states = {"Start": StartState, 
                             "Play": PlayState,                          
                             "Finish": Finish,
                             "Score": ScoreState,
                             "Menu": MenuState
                             }

        self.current_state = None
    def changeState(self, newState):
        '''
        Changes the current state to a new state
        @param newState: The fully initialized object of the new state to switch to...       
        '''
        if self.states:
            self.states[-1].free()
            self.states[-1].unload()
            self.states.pop()
        
        newState.stateManager = self
        self.states.append(newState)
        self.states[-1].load()
        self.states[-1].init()


    def update(self, dt):
        '''
        Updates the current state
        @param dt: The delta time since the last frame
        '''
        if self.states:
            self.states[-1].update(dt)

    def render(self, virtual_screen, dt=0.0):
        '''
        Renders the current state
        @param virtual_screen: The Pygame screen surface to draw on
        @param dt: The delta time since the last frame
        '''

        if self.states:
            self.states[-1].render(virtual_screen, dt)

    def handle_event(self, event):
        '''
        Handles events for the current state
        @param event: The Pygame event to handle
        '''
        if self.states:
            self.states[-1].handle_event(event)

