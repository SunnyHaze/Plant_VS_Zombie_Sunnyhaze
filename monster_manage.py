import pygame
from pygame.sprite import Group
import Monster
from random import randint

monster_list = Group()


def generate_monster(view_manager):
    if len(monster_list) < 7:
        monster = Monster.Monster(view_manager, randint(0, 2))
        monster_list.add(monster)


def draw_monster(screen, view_manager):
    del_list = []
    for monster in monster_list.sprites():
        monster.x -= 1
        monster.draw(screen, view_manager)
        if monster.x < 0:
            del_list.append(monster)
    monster_list.remove(del_list)
    del_list.clear()
