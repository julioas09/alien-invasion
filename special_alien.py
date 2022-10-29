import pygame
from pygame.sprite import Sprite
 
class sAlien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.lives = 3

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.x)
        self.direction = 1

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += ((self.settings.alien_speed*2) * self.direction) / 8
        self.rect.x = self.x
        self.y += ((self.settings.alien_speed / 8))
        self.rect.y = self.y
        
    def check_level(self,n):
        if n == 2: 
            #change image 
            self.image = pygame.image.load('images/ship.bmp')