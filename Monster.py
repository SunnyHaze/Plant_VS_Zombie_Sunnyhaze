import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
# ���ƹ��ﶯ�����ٶ�
COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8
# �������������͵ĳ��������������Ҫ���Ӹ���Ĺ����ֻ���ڴ˴���ӳ������ɣ�
TYPE_SUPERSTAR = 1
TYPE_DINGDING = 2


class Monster(Sprite):
    def __init__(self, view_manager, tp=TYPE_SUPERSTAR):
        super().__init__()
        # ������������
        self.type = tp
        # ��������X��Y���������
        self.x = 0
        self.y = 0
        # ��������Ƿ��Ѿ����������
        self.is_die = False
        # ���ƹ���ͼƬ���Ͻǵ�X����
        self.start_x = 0
        # ���ƹ���ͼƬ���Ͻǵ�Y����
        self.start_y = 0
        # ���ƹ���ͼƬ���½ǵ�X����
        self.end_x = 0
        # ���ƹ���ͼƬ���½ǵ�Y����
        self.end_y = 0
        # �ñ������ڿ��ƶ���ˢ�µ��ٶ�
        self.draw_count = 0
        # ���嵱ǰ���ڻ��ƹ��ﶯ���ĵڼ�֡�ı���
        self.draw_index = 0
        self.life = 5
        # ���ڼ�¼�����Ķ���ֻ����һ�Σ�����Ҫ�ظ�����
        # ÿ����������ʱ���ñ������ᱻ��ʼ��Ϊ����������������֡��
        # ���������������֡������ɺ󣬸ñ�����ֵ��Ϊ0
        self.die_max_draw_count = sys.maxsize
        # ������﷢����ӵ�
        self.bullet_list = Group()
        #������ù����y����������
        self.y = 20 + randint(0, 4) * 136.8
        # �����������X���ꡣ
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