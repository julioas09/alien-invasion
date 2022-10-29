import random
import pygame
from pygame.sprite import Sprite
 
class Monster(Sprite):
    """A class to represent a new monster enemy in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.hitpoints = 3 

        # Rect method gets the size and location of the element.
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.screen.get_rect().width - self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= self.rect.height:
            return True

    def update(self):
        """Move the alien right or left."""
        self.y += (self.settings.monster_speed/2 *
                        self.settings.monster_direction)
        self.rect.y = self.y

        # Horizontal movement
        self.x -= self.settings.monster_direction/2
        self.rect.x =self.x
        
