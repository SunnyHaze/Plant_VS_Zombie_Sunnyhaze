## -*- coding: GB2312 -*-
import sys
import pygame
import plant


def check_events(screen, view_manager, x, y, press, p1):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        # 处理游戏退出
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
    ''' 处理更新游戏界面的方法 '''
    # 随机生成怪物
    mm.generate_monster(view_manager)
    # 绘制背景图片
    screen.blit(view_manager.background, (0, 0))
    screen.blit(view_manager.cards, (120, 15))
    # 绘制怪物
    mm.draw_monster(screen, view_manager)
    # 更新屏幕显示，放在最后一行
    pygame.display.flip()