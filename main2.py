## -*- coding: GB2312 -*-
import pygame, sys, os
from ViewManager import ViewManager
import game_functions as gf
import monster_manage as mm
from plant import plant
import time


def update_screen(screen, view_manager, mm):
    ''' ���������Ϸ����ķ��� '''
    # ������ɹ���
    mm.generate_monster(view_manager)
    # ���Ʊ���ͼƬ
    # ���ƹ���
    mm.draw_monster(screen, view_manager)
    # ������Ļ��ʾ���������һ��
    pygame.display.update()


def run_game():
    # ��ʼ����Ϸ
    pygame.init()
    # ����ViewManager����
    screen = pygame.display.set_mode((1024, 768))
    view_manager = ViewManager()
    block = pygame.time.Clock()
    # ������ʾ��Ļ������Surface����
    p1 = []
    # ���ñ���
    pygame.display.set_caption('pvz')
    p2 = []

    #�Ƿ������״̬
    is_pick = False
    while 1:
        block.tick(30)
        screen.blit(view_manager.background, (0, 0))
        screen.blit(view_manager.cards, (120, 15))
        press = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()

        # ������Ϸ�¼�
        for event in pygame.event.get():
            # ������Ϸ�˳�
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if not is_pick:
                    if press[0]:
                        if 120 <= x < 120 + view_manager.cards.get_rect(
                        ).width and 15 <= y <= 15 + view_manager.cards.get_rect(
                        ).height:
                            p = plant(view_manager)
                            p1.append(p)
                            is_pick = True
                if is_pick:
                    if not (120 <= x <
                            120 + view_manager.cards.get_rect().width and 15 <=
                            y <= 15 + view_manager.cards.get_rect().height):
                        if press[2]:
                            p1.clear()
                            is_pick = False
                        if press[0]:
                            p.x = x - 50
                            p.y = y - 80
                            p.motivated = True
                            p2.append(p)
                            p1.clear()
                            is_pick = False
        for i in p1:
            screen.blit(i.images, (x - 50, y - 80))
        for i in p2:
            if i.motivated and i.shoot_time <= 0:
                i.add_bullet(view_manager)
            i.draw_bullet(screen)
            screen.blit(i.images, (i.x, i.y))
            # print((str(len(i.bullet_list))), str(i.shoot_time))
        if press[1]:
            print(len(p2))

        del_monster = []
        for i in mm.monster_list:
            for j in p2:
                for k in j.bullet_list:
                    if(i.is_hurt(k.x+50,k.y+26)):
                        j.bullet_list.remove(k)
                        i.life -= 1
                        if i.life <= 0:
                            del_monster.append(i)
        mm.monster_list.remove(del_monster)
        del_monster.clear()
        update_screen(screen, view_manager, mm)


run_game()