import pygame as pg
import random
import math
from colors import *


def contur(text, clr1, clr2, x, y, n):
    my_font = pg.font.SysFont('Times New Roman', 25)
    text_surface = my_font.render(text, True, clr2)
    for i, j in [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]:
        screen.blit(text_surface, (x + i * n, y + j * n))

    text_surface = my_font.render(text, True, clr1)
    screen.blit(text_surface, (x, y))


def sgn(x):
    if abs(x) < 1e-6:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


def mp(x, y, x0, y0):
    # print(int(x) // TILE + x0, len(map), x, y, y0, x0)
    if int(x + 0.0001) // TILE + x0 > 0 and int(y + 0.0001) // TILE + y0 > 0:
        return map[int(x + 0.0001) // TILE + x0][int(y + 0.0001) // TILE + y0]


def mapping(cam, pl):
    for x in range(int(pl.pos[0] - SC_WIDTH / 2) // TILE * TILE, int(pl.pos[0] + SC_WIDTH / 2) + TILE, TILE):
        for y in range(int(pl.pos[1] - SC_HEIGHT / 2) // TILE * TILE, int(pl.pos[1] + SC_HEIGHT / 2) + TILE, TILE):

            # if map[i // TILE][j // TILE]:
            # print(map[i // TILE][j // TILE])
            if map[(x) // TILE][(y) // TILE] == 1:

                pg.draw.rect(screen, BROWN, (x + cam[0], y + cam[1], TILE, TILE))
            elif map[(x) // TILE][(y) // TILE] == 2:

                pg.draw.rect(screen, GREEN, (x + cam[0], y + cam[1], TILE, TILE))


class Player(pg.sprite.Sprite):
    def points(self):
        an = []
        for j, i in [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]:
            an.append([self.pos[0] + i * TILE, self.pos[1] + j * TILE])
        an.append([self.pos[0] + 2 * TILE - 1, self.pos[1]])
        an.append([self.pos[0] + 2 * TILE - 1, self.pos[1] + TILE])
        an.append([self.pos[0] + 2 * TILE - 1, self.pos[1] + 2 * TILE])
        an.append([self.pos[0], self.pos[1] + 3 * TILE - 1])
        an.append([self.pos[0] + TILE - 1, self.pos[1] + 3 * TILE - 1])
        an.append([self.pos[0] + 2 * TILE - 1, self.pos[1] + 3 * TILE - 1])

        return an

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.pos = pg.Vector2((x, y))
        self.dir = pg.Vector2((0, 0))
        self.hp = 100
        self.maxhp = 100

        self.image = pg.Surface((20, 30))
        try:
            self.image = pg.image.load('img/terrar_player.png')
            self.image.set_colorkey(WHITE)
        except:
            self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pressed = pg.key.get_pressed()
        # for i in self.points():
        # pygame.draw.line(screen, RED, i, i)
        # print(i, mp(i[0], i[1], 0, 0), end=' ')
        # pygame.draw.rect(screen, BLUE, (i[0] // TILE * TILE, i[1] // TILE * TILE, TILE, TILE), 1)
        # print()
        if mp(self.pos[0], self.pos[1], 0, 3) or mp(self.pos[0], self.pos[1], 1, 3) or mp(self.pos[0] + TILE - 1,
                                                                                          self.pos[1], 1, 3):
            self.dir[1] = 0
            if pressed[pg.K_SPACE]:
                self.dir -= (0, 7)
        else:
            self.dir += (0, 0.5)
        if pressed[pg.K_a]:
            if self.dir[0] > 0:
                self.dir[0] = 0
            self.dir += (-0.1, 0)
        elif pressed[pg.K_d]:
            if self.dir[0] < 0:
                self.dir[0] = 0
            self.dir += (0.1, 0)
        else:
            self.dir -= (self.dir[0] / 6, 0)
            if abs(self.dir[0]) < 0.01:
                self.dir[0] = 0
        if self.dir[0] >= 2: self.dir[0] = 2
        if self.dir[0] <= -2: self.dir[0] = -2
        if self.dir[1] >= 20: self.dir[1] = 20
        # if self.dir[1] <= -3: self.dir[1] = -3
        now = self.pos[:]

        self.pos[0] += self.dir[0]

        # print(self.is_inb())
        if self.is_inb():
            self.pos[0] -= self.dir[0]
            if self.dir[0] > 0:
                self.pos[0] = (self.pos[0] + TILE - 1) // TILE * TILE
            if self.dir[0] < 0:
                self.pos[0] = (self.pos[0]) // TILE * TILE
            self.dir[0] = 0
        self.pos[1] += self.dir[1]
        if self.is_inb():
            self.pos[1] -= self.dir[1]

            if self.dir[1] > 0:
                self.pos[1] = (self.pos[1] + TILE - 1) // TILE * TILE
            if self.dir[1] < 0:
                self.pos[1] = (self.pos[1]) // TILE * TILE
            self.dir[1] = 0
        self.now = now - self.pos
        # print(self.now)
        self.rect.topleft = self.pos

    def is_inb(self):
        for i, j in self.points():
            if mp(i, j, 0, 0):
                return True, (i, j)
        return False


v = pg.Vector2
WIDTH = 150000  # 136
HEIGHT = 5000  # 70

SC_WIDTH = 1365  # 1365
SC_HEIGHT = 700  # 700
FPS = 60
TILE = 10
map = [[0] * (2 * HEIGHT // TILE) for i in range(2 * WIDTH // TILE)]  # x,y
for x in range(len(map[0])):
    map[0][x] = 3
    map[-1][x] = 3

for x in range(len(map)):

    map[x][108] = 2
    for y in range(109, 300):
        map[x][0] = 3
        map[x][-1] = 3

        map[x][y] = 1
    # map[x][35] = 1
map[38][105] = 2
map[37][105] = 2
map[34][105] = 2
map[34][104] = 2
map[34][102] = 1

map[39][101] = 2

map[38][101] = 2
# for y in range(len(map[0])):
#     for x in range(len(map)):
#         print(map[x][y], end=' ')
#     print()
# print(len(map), len(map[0]))
# print(map[400])
pg.init()
pg.font.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((750, 600), pg.RESIZABLE)
pg.display.set_caption("terraria")
