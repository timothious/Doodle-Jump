import pygame
from src.config import *
import random

class Stages:
    def __init__(self, assets,x = 0, y = 1000):
        self.assets = assets
        self.x = x
        self.y = y
        self.width = 125
        self.height = 35
        self.jump_factor = 0
        self.plain = self.assets['images']['atlas']
        self.spring_atlas = self.assets['images']['spring'] 
        self.image = None  # Initialize image attribute

    def update(self, dt):
        pass

    def render(self, virtual_screen):
        virtual_screen.blit(self.image, (self.x, self.y))

    def move_down(self, velocity, dt):
        self.y = self.y - velocity

class Plain_Platform(Stages):
    def __init__(self,assets,x,y):
        super().__init__(assets,x,y)
        self.jump_factor = 20 
        plain_rect = pygame.Rect(0, 0, self.width, self.height)    
        self.plain_paddle = self.plain.subsurface(plain_rect)
        self.image = self.plain_paddle

class Jump_Platform(Stages):
    def __init__(self,assets,x,y):
        super().__init__(assets,x,y)
        
        self.jump_factor = 40
        plain_rect = pygame.Rect(0, self.height, self.width, self.height)
        self.jump_paddle = self.plain.subsurface(plain_rect)
        self.image = self.jump_paddle


class Moving_Platform(Stages):
    def __init__(self,assets,x,y):
        super().__init__(assets,x,y)
        
        self.dx = 20
        self.direction =random.choice(["right","left"]) 
        self.jump_factor=20
        Moving_rect =  pygame.Rect(0, self.height * 3, self.width, self.height)
        self.Moving_rect = self.plain.subsurface(Moving_rect)
        self.image = self.Moving_rect 
    
    def update(self,dt):
        if (self.x + self.width) >= VIRTUAL_WIDTH or self.x <= 0:
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"
        
        if self.direction == "right":
            self.x += self.dx*dt
        else:
            self.x -= self.dx*dt
                
            

class Broken_platform(Stages):
    def __init__(self,assets,x,y):
        super().__init__(assets,x,y)
        self.jump_factor = 0
        broken_rect = pygame.Rect(0,self.height * 4, self.width,self.height)
        self.Broken_Paddle = self.plain.subsurface(broken_rect)
        self.image = self.Broken_Paddle

class lava_platform(Stages):
    def __init__(self, assets, x, y):
        super().__init__(assets, x, y)
        self.jump_factor = 10
        self.loose = True
        lava_rect = pygame.Rect(0,self.height * 17, self.width,self.height)
        self.lava_paddle = self.plain.subsurface(lava_rect)
        self.image = self.lava_paddle
