import pygame
from src.states.State import State
from src.config import *
from lib.utils import draw_text
import time


class Finish(State):
    def __init__(self, assets):
        self.assets = assets
        self.backgroundImg = self.assets['images']['background']
        self.font = self.assets['font']['Large']
        self.md_font = self.assets['font']['medium'] 
        self.button_music = self.assets['sounds']['trampoline']
        self.loading_score = self.assets['images']['Loading_score']
        self.display_loading_score = True
        self.loading_score_timer = 2.0  # Time to display loading score in seconds
        self.loading_score_elapsed = 0.0

    def load(self):
        # Load necessary resources for the finish state
        pass

    def unload(self):
        # Unload resources when the finish state is no longer needed
        pass

    def init(self):
        # Initialize any state-specific variables or settings
        
        self.read_scores("Last_score.txt")
        self.highlighted = 1

    def free(self):
        # Free up resources and perform clean-up activities
        pass

    def pause(self):
        # Pause any ongoing activities or processes
        pass

    def resume(self):
        # Resume from a paused state
        pass

    def read_scores(self, file_name):
        # Read scores from the file
        with open(file_name, "r") as file:
            self.scores = file.readlines()

    def update(self, dt):
        if self.display_loading_score:
            self.loading_score_elapsed += dt
            if self.loading_score_elapsed >= self.loading_score_timer:
                self.display_loading_score = False
                self.loading_score_elapsed = 0.0


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the return key
                if self.highlighted == 1:
                    self.stateManager.changeState(self.stateManager.ready_states["Play"](self.assets))
                elif self.highlighted == 2:
                    self.stateManager.changeState(self.stateManager.ready_states["Menu"](self.assets))
            elif event.key == pygame.K_UP:
                # Handle the up arrow key
                self.highlighted = 1
                self.button_music.play()
                
            elif event.key == pygame.K_DOWN:
                # Handle the down arrow key
                self.highlighted = 2
                self.button_music.play()
                
                

    def render(self, virtual_screen, dt=0.0):
        scaled_background = pygame.transform.scale(self.backgroundImg, (VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
        virtual_screen.blit(scaled_background, (0, 0))

        if self.display_loading_score:
            scaled_score_image = pygame.transform.scale(self.loading_score, (748, 634))
            score_rect = scaled_score_image.get_rect(center=(VIRTUAL_WIDTH // 2 - 50, VIRTUAL_HEIGHT // 2 + 50))  
            virtual_screen.blit(scaled_score_image, score_rect)
        else:
            heading_text = self.font.render("Your Score", True, (0, 0, 0))
            heading_rect = heading_text.get_rect(center=(VIRTUAL_WIDTH // 2, 200))
            virtual_screen.blit(heading_text, heading_rect)

            for i, score in enumerate(self.scores):
                score_text = self.md_font.render(score.strip(), True, (255, 0, 0))
                score_rect = score_text.get_rect(center=(VIRTUAL_WIDTH // 2, 250 + i * 50))
                virtual_screen.blit(score_text, score_rect)

            color = (0, 0, 0)
            if self.highlighted == 1:
                color = (255, 0, 0)
            draw_text('RESTART', self.md_font, VIRTUAL_WIDTH / 2, 350, color, virtual_screen)
            color = (0, 0, 0)
            if self.highlighted == 2:
                color = (255, 0, 0)
            draw_text('MENU', self.md_font, VIRTUAL_WIDTH / 2, 425, color, virtual_screen)
