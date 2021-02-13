## -*- coding: GB2312 -*-
import sys
import pygame
import plant


def check_events(screen, view_manager, x, y, press, p1):
    ''' ��Ӧ����������¼� '''
    for event in pygame.event.get():
        # ������Ϸ�˳�
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if press[0]:
                print('hit')
                if 120 <= x < 120 + view_manager.cards.get_rect(
                ).width and 15 <= y <= 15 + view_manager.cards.get_rect(
                ).height:
                    p = plant.plant()
                    p1.append(p)


def update_screen(screen, view_manager, mm):
    ''' ���������Ϸ����ķ��� '''
    # ������ɹ���
    mm.generate_monster(view_manager)
    # ���Ʊ���ͼƬ
    screen.blit(view_manager.background, (0, 0))
    screen.blit(view_manager.cards, (120, 15))
    # ���ƹ���
    mm.draw_monster(screen, view_manager)
    # ������Ļ��ʾ���������һ��
    pygame.display.flip()