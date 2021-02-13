import pygame, os
from random import randint
from pygame.sprite import Group
from bullet import *
from ViewManager import ViewManager


class plant:
    def __init__(self, view_manager):
        self.view_manager = view_manager
        self.MAX_SHOOT_TIME = 70
        self.is_die = False
        self.life = 100
        main_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # self.image = pygame.image.load('superstar.jpg')
        self.images = pygame.image.load(
            os.path.join(main_dir, "pvz", "images",
                         "plant.png")).convert_alpha()
        self.images = pygame.transform.scale(self.images, (120, 180))
        self.rect = self.images.get_rect()
        self.x = 0
        self.y = 0
        self.motivated = False
        self.shoot_time = 100
        self.bullet_list = Group()

    def add_bullet(self, view_manager):
        bullet_x = self.x + 30
        bullet = Bullet(view_manager, 5, bullet_x, self.y + 60)
        self.bullet_list.add(bullet)
        self.shoot_time = self.MAX_SHOOT_TIME

    def draw_bullet(self, screen):
        delete_list = []
        for bullet in self.bullet_list.sprites():
            if bullet.x > self.view_manager.screen_width:
                delete_list.append(bullet)
        self.bullet_list.remove(delete_list)
        for bullet in self.bullet_list.sprites():
            bitmap = bullet.image
            bullet.move()
            screen.blit(bitmap, (bullet.x, bullet.y))
        self.shoot_time -= 1
