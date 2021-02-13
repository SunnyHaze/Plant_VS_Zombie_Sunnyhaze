import pygame, os
from random import randint


class plant:
    def __init__(self, lane):
        self.position = 800
        self.lane = lane
        self.is_die = False
        self.life = 10
        main_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # self.image = pygame.image.load('superstar.jpg')
        self.images = pygame.image.load(
            os.path.join(main_dir, "images", "plant.png")).convert_alpha()
        self.rect = self.images[0].get_rect()

    def move(self):
        if self.position == 0:
            return 0
        else:
            self.position -= 1
            self.rect.left, self.rect.top = self.position, -70 + 100 * self.lane
            return 1
        # print(self.position)
