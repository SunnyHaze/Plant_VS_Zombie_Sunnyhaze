import pygame, os


class ViewManager:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        main_dir = os.path.split(os.path.abspath(__file__))[0]

        self.dingding = [
            pygame.image.load(
                os.path.join(main_dir, "images", "dingding",
                             'dingding{:d}.png'.format(i))).convert_alpha()
            for i in range(8)
        ]
        self.superstar = [
            pygame.image.load(
                os.path.join(main_dir, "images", "superstar",
                             'superstar{:d}~2.png'.format(i))).convert_alpha()
            for i in range(8)
        ]
        self.green = pygame.image.load(
            os.path.join(main_dir, "images", "plant.png")).convert_alpha()
        self.cards = pygame.image.load(
            os.path.join(main_dir, "images", "card.png")).convert_alpha()
        self.background = pygame.image.load(
            os.path.join(main_dir, "images",
                         "background.png")).convert_alpha()
        self.bullet = pygame.image.load(
            os.path.join(main_dir, "images", "bullet.png")).convert_alpha()
