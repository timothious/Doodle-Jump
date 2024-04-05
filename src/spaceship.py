import pygame
from src.config import *

class Spaceship:
    def __init__(self, images, top_right_offset=(0, 0)):
        self.images = images  # List of spaceship images
        self.index = 0  # Index to track the current image
        self.image = self.images[self.index][0]  # Get the first image
        self.rect = self.image.get_rect()
        self.top_right_offset = top_right_offset
        self.rect.topright = (VIRTUAL_WIDTH - top_right_offset[0], top_right_offset[1])  # Set initial position
        self.speed = 2  # Adjust the speed as needed
        self.timer = 0
        self.swap_interval = 30  # Swap image every 30 frames

    def update(self):
        # Move the spaceship left and right
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > VIRTUAL_WIDTH:
            # Change direction when hitting the window boundaries
            self.speed = -self.speed
        
        # Swap images periodically
        self.timer += 1
        if self.timer >= self.swap_interval:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index][0]  # Get the image from the list
            self.rect.topleft = (self.images[self.index][1], self.images[self.index][2])  # Update rect position
            self.rect.topright = (VIRTUAL_WIDTH - self.top_right_offset[0], self.top_right_offset[1])  # Update rect position
            self.timer = 0

    def draw(self, surface):
        # Draw the spaceship onto the surface
        surface.blit(self.image, self.rect)
