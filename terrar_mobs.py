import pygame
import random
import math
from colors import *


def sgn(x):
    if abs(x) < 1e-6:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


# print(sgn(-3))

def mp(x, y, x0, y0):
    # print(int(x) // TILE + x0, len(map), x, y, y0, x0)

    return map[int(x + 0.0001) // TILE + x0][int(y + 0.0001) // TILE + y0]


def mapping(cam, pl):
    for x in range(int(pl.pos[0] - SC_WIDTH / 2) // TILE * TILE, int(pl.pos[0] + SC_WIDTH / 2), TILE):
        for y in range(int(pl.pos[1] - SC_HEIGHT / 2) // TILE * TILE, int(pl.pos[1] + SC_HEIGHT / 2), TILE):

            # if map[i // TILE][j // TILE]:
            # print(map[i // TILE][j // TILE])
            if map[(x) // TILE][(y) // TILE]:
                pass
                # print(int(pl.pos[0] - SC_WIDTH / 2))
                pygame.draw.rect(screen, GRAY, (x + cam[0], y + cam[1], TILE, TILE))
            else:
                pass
                # pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE), 1)


class Player(pygame.sprite.Sprite):
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
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.Vector2((x, y))
        self.dir = pygame.Vector2((0, 0))

        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pressed = pygame.key.get_pressed()
        # for i in self.points():
        # pygame.draw.line(screen, RED, i, i)
        # print(i, mp(i[0], i[1], 0, 0), end=' ')
        # pygame.draw.rect(screen, BLUE, (i[0] // TILE * TILE, i[1] // TILE * TILE, TILE, TILE), 1)
        # print()
        if mp(self.pos[0], self.pos[1], 0, 3) or mp(self.pos[0], self.pos[1], 1, 3) or mp(self.pos[0] + TILE - 1,
                                                                                          self.pos[1], 1, 3):
            self.dir[1] = 0
            if pressed[pygame.K_SPACE]:
                self.dir -= (0, 7)
        else:
            self.dir += (0, 0.5)
        if pressed[pygame.K_a]:
            self.dir += (-0.5, 0)
        elif pressed[pygame.K_d]:
            self.dir += (0.5, 0)
        else:
            self.dir -= (self.dir[0] / 6, 0)
            if abs(self.dir[0]) < 0.01:
                self.dir[0] = 0
        if self.dir[0] >= 4: self.dir[0] = 4
        if self.dir[0] <= -6: self.dir[0] = -6
        if self.dir[1] >= 10: self.dir[1] = 10
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


v = pygame.Vector2
WIDTH = 13650  # 136
HEIGHT = 7000  # 70

SC_WIDTH = 1365  # 1365
SC_HEIGHT = 700  # 700
FPS = 100
TILE = 10
map = [[0] * (2 * HEIGHT // TILE) for i in range(2 * WIDTH // TILE)]  # x,y
for x in range(len(map)):
    map[x][38] = 1
    # map[x][39] = 1
    # map[x][35] = 1
map[38][35] = 1
map[37][35] = 1
map[34][35] = 1
map[34][34] = 1

map[39][31] = 1

map[38][31] = 1
# for y in range(len(map[0])):
#     for x in range(len(map)):
#         print(map[x][y], end=' ')
#     print()
# print(len(map), len(map[0]))
# print(map[400])
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((750, 600), pygame.RESIZABLE)
pygame.display.set_caption("terraria")
