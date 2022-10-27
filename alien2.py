import pygame
from pygame.sprite import Sprite
 
class Alien2(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/obama.bmp')
        IMAGESIZE = (500,500)
        self.image = pygame.transform.scale(self.image, IMAGESIZE)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction = 1
        self.lives = 3

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


        

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.special_alien_speed * self.direction)
        self.rect.x = self.x
        self.y += ((self.settings.alien_speed / 8))
        self.rect.y = self.y
