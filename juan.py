import pygame
from pygame.sprite import Sprite


class Juan(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/AlienD.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges_j(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.juan_speed * self.settings.juan_direction)
        self.y += self.settings.juan_speed
        self.rect.x = self.x
        self.rect.y = self.y//2

    #def check_juan_hp(self):
        #juan_hp = self.settings.juan_hp
        #if juan_hp == 0:
            #self.juan.empty()
            #juan_hp += 3
            #if self.settings.juan_direction != 1:
                #self.settings.juan_direction == 1