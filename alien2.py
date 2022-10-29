import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien2_hitpoints = 3
        self.alien2_direction = 1
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien2_speed *
                        self.alien2_direction)
        self.rect.x = self.x
        self.y += 0.1
        self.rect.y = self.y

    def kill_alien2(self):
        self.alien2_hitpoints -= 1
        if self.alien2_hitpoints == 0:
            return True

    def change_direction(self):
        self.alien2_direction *= -1