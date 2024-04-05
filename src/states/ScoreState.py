import pygame
from src.states.State import State
from src.states.StartState import StartState
from src.config import *

class ScoreState(State):
    def __init__(self, assets):
        self.assets = assets
        self.scores = []

    def load(self):
        # Load assets and initialize variables here
        self.backgroundImg = self.assets['images']['background']
        self.font = self.assets['font']['Large']
        self.md_font = self.assets['font']['small'] 

    def unload(self):
        pass

    def init(self):
        # Read scores from the file when the state is initialized
        self.read_scores("score.txt")

    def pause(self):
        pass
    

    
    def resume(self):
        pass

    def free(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:  # Check if it's a keyboard event
            if event.key == pygame.K_RETURN:
                self.stateManager.changeState(StartState(self.assets))

    def read_scores(self, file_name):
        # Read scores from the file
        with open(file_name, "r") as file:
            self.scores = file.readlines()

    def update(self, dt):
        pass

    def render(self, virtual_screen, dt=0.0):
        # Draw the background image
        scaled_background = pygame.transform.scale(self.backgroundImg, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        virtual_screen.blit(scaled_background, (0, 0))

        # Render heading "High Score"
        heading_text = self.font.render("High Score", True, (0, 0, 0))
        heading_rect = heading_text.get_rect(center=(VIRTUAL_WIDTH // 2, 50))
        virtual_screen.blit(heading_text, heading_rect)

        # Render scores line by line
        y_offset = 100
        for score in self.scores:
            score_text = self.md_font.render(score.strip(), True, (255, 0, 0))
            score_rect = score_text.get_rect(center=(VIRTUAL_WIDTH // 2, y_offset))
            virtual_screen.blit(score_text, score_rect)
            y_offset += 50
