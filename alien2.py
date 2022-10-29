import pygame
from pygame.sprite import Sprite
 
class Alien2(Sprite):
    """A class to represent another alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('C:/Users/Farah/alien/alien-invasion/images/alien2.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.a = self.rect.width
        self.rect.b = self.rect.height

        # Store the alien's exact horizontal position.
        self.a = float(self.rect.a)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.top or self.rect.bottom <= 0:
            return True

    def update(self):
        """Move the alien diagonally."""
        self.a += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.a = self.a
