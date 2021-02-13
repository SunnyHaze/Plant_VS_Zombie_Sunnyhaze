import pygame
from pygame.sprite import Sprite
from ViewManager import ViewManager


class Bullet(Sprite):
    def __init__(self, view_manager, speed, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.x_speed = speed
        self.is_effect = True
        self.image = view_manager.bullet

    def move(self):
        self.x += self.x_speed