import pygame
import random
from colors import *


def sgn(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    else:
        return -1


def mp(x, y, x0, y0):
    print(int(x) // TILE + x0, len(map), x, y, y0, x0)

    return map[int(x) // TILE + x0][int(y) // TILE + y0]


def mapping():
    for x in range(0, WIDTH, TILE):
        for y in range(0, HEIGHT, TILE):

            # if map[i // TILE][j // TILE]:
            # print(map[i // TILE][j // TILE])
            if map[x // TILE][y // TILE]:
                pass
                pygame.draw.rect(screen, GRAY, (x, y, TILE, TILE))
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
        for i in self.points():
            pygame.draw.line(screen, RED, i, i)

        if mp(self.pos[0], self.pos[1], 0, 3) or mp(self.pos[0], self.pos[1], 1, 3):

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
        if self.dir[0] >= 4: self.dir[0] = 4
        if self.dir[0] <= -4: self.dir[0] = -4
        if self.dir[1] >= 10: self.dir[1] = 10
        # if self.dir[1] <= -3: self.dir[1] = -3
        self.pos += self.dir
        if self.is_inb():
            self.pos -= self.dir

            # if self.pos[1]:
            #     while not self.is_inb():
            #         self.pos += (0, sgn(self.pos[1]))
            #     self.pos -= (0, sgn(self.pos[1]))
            # if self.pos[0]:
            #     while not self.is_inb():
            #         self.pos += (sgn(self.pos[0]), 0)
            #     self.pos -= (sgn(self.pos[0]), 0)

        self.rect.topleft = self.pos

    def is_inb(self):
        for i, j in self.points():
            if mp(i, j, 0, 0):
                return True
        return False


v = pygame.Vector2
WIDTH = 1365  # 136
HEIGHT = 700  # 70
FPS = 100
TILE = 10
map = [[0] * (2 * HEIGHT // TILE) for i in range(2 * WIDTH // TILE)]  # x,y
for x in range(len(map)):
    map[x][38] = 1
    map[x][39] = 1
    # map[i][35] = 1
map[38][35] = 1
map[37][35] = 1
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
