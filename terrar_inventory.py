import pygame as pg
import random
import math
from colors import *


class element(pg.sprite.Sprite):
    def __init__(self, x, y, elm):
        pg.sprite.Sprite.__init__(self)
        self.pos = pg.Vector2((x, y))
        self.type = elm[0]
        self.cnt = elm[1]
        self.image = pg.Surface((30, 30))
        self.image.fill(BLUE)
        self.image.set_alpha(150)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class inventory():
    def __init__(self):
        self.inv = [[(0, 0) for i in range(10)] for j in range(6)]

        self.elements = pg.sprite.Group()
        for i in range(10):
            el = element(40 * i + 5, 5, self.get_element(0, i))
            self.elements.add(el)

    def get_element(self, i, j):
        return self.inv[i][j]

    def update_element(self, i, j, type, cnt):
        if cnt == 0: type = 0
        self.inv[i][j] = (type, cnt)

    def draw(self, screen):
        self.elements.draw(screen)

    def change_mode(self, mode):
        self.elements = pg.sprite.Group()
        if mode == 0:
            for e in self.elements:
                e.kill()
            for x in range(10):
                el = element(40 * x + 5, 5, self.get_element(0, x))
                self.elements.add(el)
        elif mode == 1:
            for e in self.elements:
                e.kill()
            for y in range(6):
                for x in range(10):
                    el = element(40 * x + 5, 40 * y + 5, self.get_element(y, x))
                    self.elements.add(el)
