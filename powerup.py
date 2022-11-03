import pygame
from pygame import rect
from pygame.sprite import Sprite
from settings import Settings
from random import randint
import random

class poweruppp(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.power_color

        display_rect = self.screen.get_rect()

        self.x = random.randint(0, display_rect.w -100 )
        self.y = 1
        self.image = pygame.image.load('images/power_up_.jpg')
        self.image = pygame.transform.scale(self.image, (150, 100))
        # You can also pass the coords directly to `get_rect`.
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


        # Start each new alien near the top left of the screen.


        # Store the alien's exact horizontal position.

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += 0.2
        # Update the rect position.
        self.rect.y = self.y

    def draw_power(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)