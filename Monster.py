import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
# 控制怪物动画的速度
COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8
# 定义代表怪物类型的常量（如果程序需要增加更多的怪物，则只需在此处添加常量即可）
TYPE_SUPERSTAR = 1
TYPE_DINGDING = 2


class Monster(Sprite):
    def __init__(self, view_manager, tp=TYPE_SUPERSTAR):
        super().__init__()
        # 定义怪物的类型
        self.type = tp
        # 定义怪物的X、Y坐标的属性
        self.x = 0
        self.y = 0
        # 定义怪物是否已经死亡的旗标
        self.is_die = False
        # 绘制怪物图片左上角的X坐标
        self.start_x = 0
        # 绘制怪物图片左上角的Y坐标
        self.start_y = 0
        # 绘制怪物图片右下角的X坐标
        self.end_x = 0
        # 绘制怪物图片右下角的Y坐标
        self.end_y = 0
        # 该变量用于控制动画刷新的速度
        self.draw_count = 0
        # 定义当前正在绘制怪物动画的第几帧的变量
        self.draw_index = 0
        self.life = 5
        # 用于记录死亡的动画只绘制一次，不需要重复绘制
        # 每当怪物死亡时，该变量都会被初始化为等于死亡动画的总帧数
        # 当怪物的死亡动画帧播放完成后，该变量的值变为0
        self.die_max_draw_count = sys.maxsize
        # 定义怪物发射的子弹
        self.bullet_list = Group()
        #随机放置怪物的y坐标于列中
        self.y = 20 + randint(0, 4) * 136.8
        # 随机计算怪物的X坐标。
        self.x = view_manager.screen_width + randint(
            0, int(view_manager.screen_width / 2))

    def draw(self, screen, view_manager):
        if self.type == TYPE_DINGDING:
            self.draw_anim(screen, view_manager, view_manager.dingding)
        elif self.type == TYPE_SUPERSTAR:
            self.draw_anim(screen, view_manager, view_manager.superstar)
        else:
            pass

    def draw_anim(self, screen, view_manager, bitmap_arr):
        self.draw_index %= len(bitmap_arr)
        bitmap = bitmap_arr[self.draw_index]
        if bitmap == None:
            return
        draw_x = self.x
        draw_y = self.y
        screen.blit(bitmap, (draw_x, draw_y))
        self.start_x = draw_x
        self.start_y = draw_y
        self.end_x = self.start_x + bitmap.get_width()
        self.end_y = self.start_y + bitmap.get_height()
        self.draw_count += 1
        if self.draw_count >= (COMMON_SPEED_THRESHOLD):
            self.draw_index += 1
            self.draw_count = 0

    def is_hurt(self, x, y):
        return self.start_x < x < self.end_x and self.start_y < y < self.end_y

    def __del__(self):
        pass

    def is_died(self, x, y):
        if is_hurt(x, y) == 1:
            if self.life == 1:
                self.__del__
            else:
                self.life -= 1
                return 0