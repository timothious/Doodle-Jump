import pygame
from src.config import *


class character:
    def __init__(self, assets):
        '''
        Constructor for the Character class.
        '''
        self.assets = assets
        # Load the character image.
        self.image = self.assets['Player']['player_1']
        self.jump_sound = self.assets['sounds']['jump']

        self.width = 60 
        self.height = 90

        self.y = VIRTUAL_HEIGHT - 300
        self.x = VIRTUAL_WIDTH // 2
        
        self.direction = "Right"
        
        self.dx = 0
        self.dy = 0

        self.lost = False
        self.score = 0

        self.jump_sound_effect = self.assets['sounds']['propeller']

    def move_left(self):
        if self.direction == "Right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "Left"
        self.dx = -PLAYER_SPEED
     
    def move_right(self):
        if self.direction == "Left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = "Right"      
        self.dx = PLAYER_SPEED
    
    def is_hit(self):
        return self.y <= VIRTUAL_HEIGHT // 2
    
    def play_jump_sound(self):
        self.jump_sound_effect.play()

    def jump(self, value):
        
        self.dy = -value
        self.score += 100   

    def check_collision(self, platforms=[]):
        for platform in platforms:
            if self.dy > 0 and platform.x < self.x + self.width and platform.x + platform.width > self.x:
                if platform.y <= self.y + self.height <= platform.y + platform.height:
                    if platform.jump_factor:
                        self.jump(platform.jump_factor)
                        return platform.jump_factor
                    else:
                        platforms.remove(platform)
                        return False
        return False

    def update(self, delta_time):
        if not self.lost:
            self.dy += GRAVITY * delta_time
            if self.x > VIRTUAL_WIDTH:
                self.x = 0 - self.width
            if self.x + self.width < 0:
                self.x = VIRTUAL_WIDTH

            self.x += self.dx * delta_time

            if self.dx > 0:
                self.dx = max(0, self.dx - PLAYER_FRICTION)
            else:
                self.dx = min(0, self.dx + PLAYER_FRICTION)

            if self.y > VIRTUAL_HEIGHT // 2:
                self.y = min(VIRTUAL_HEIGHT, self.y + self.dy)
            else:
                self.score += 1
                self.y = max(VIRTUAL_HEIGHT // 2, self.y + self.dy)

            if self.y + self.height > VIRTUAL_HEIGHT:
                self.lost = True
        else:
            if self.y > VIRTUAL_HEIGHT:
                self.y = 0 - self.height
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
