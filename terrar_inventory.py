import pygame as pg
from colors import *


class element(pg.sprite.Sprite):
    def __init__(self, x, y, elm):
        pg.sprite.Sprite.__init__(self)
        self.pos = pg.Vector2((x, y))
        self.type, self.cnt = elm
        self.image = pg.Surface((30, 30))
        self.image.fill(BLUE)
        self.image.set_alpha(150)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class inventory():
    def __init__(self):
        self.inv = [[(0, 0) for _ in range(10)] for __ in range(6)]
        self.inv[0][0] = (1, 1)
        self.tec = 0
        self.elements = pg.sprite.Group()
        self.change_mode(0)

    def get_element(self, i, j):
        return self.inv[i][j]

    def update_element(self, i, j, elm):
        self.inv[i][j] = elm  # Егор если ты это читаешь я предлагаю перенести проверку на нулевой тип в отрисовку уже самого элемента

    def draw(self, screen):
        self.elements.draw(screen)

    def change_mode(self, mode):
        for e in self.elements:
            e.kill()
        for x in range(10):
            for y in range(6 if mode else 1):
                el = element(40 * x + 5, 40 * y + 5, self.get_element(y, x))
                self.elements.add(el)
