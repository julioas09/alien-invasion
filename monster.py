import pygame
from pygame.sprite import Sprite
 
class Monster(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.monster_hitpoints = 3
        self.monster_direction = 1

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/monster3.png')
        self.rect = self.image.get_rect()

        # Start each new monster near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the monster's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if monster is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the monster right or left."""
        self.x += (self.settings.monster_speed *
                        self.monster_direction)
        self.rect.x = self.x
        self.y += 0.1
        self.rect.y = self.y

    def kill_monster(self):
        self.monster_hitpoints -= 1
        if self.monster_hitpoints == 0:
            return True

    def change_direction(self):
        self.monster_direction *= -1


