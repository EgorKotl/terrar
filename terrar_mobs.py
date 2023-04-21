import pygame
import random
from colors import *


def mp(i, j, x, y):
    return map[int(i) // TILE + x][int(j) // TILE + y]


def mapping():
    for i in range(0, WIDTH, TILE):
        for j in range(0, HEIGHT, TILE):
            # if map[i // TILE][j // TILE]:
            # print(map[i // TILE][j // TILE])
            if map[i // TILE][j // TILE]:
                pass
                pygame.draw.rect(screen, GRAY, (i, j, TILE, TILE))
            else:
                pass
                # pygame.draw.rect(screen, GRAY, (i, j, TILE, TILE), 1)


class Player(pygame.sprite.Sprite):
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
        # print(int(self.pos[1]) // TILE, self.pos[0])
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
        if mp(self.pos[0], self.pos[1], 0, 0) or mp(self.pos[0], self.pos[1], 0, 1) or \
                mp(self.pos[0], self.pos[1], 1, 0) or mp(self.pos[0], self.pos[1], 1, 1) or \
                mp(self.pos[0], self.pos[1], 2, 0) or mp(self.pos[0], self.pos[1], 2, 1):
            self.pos -= self.dir
            
        self.rect.topleft = self.pos


WIDTH = 1365  # 136
HEIGHT = 700  # 70
FPS = 100
TILE = 10
map = [[0] * (2 * WIDTH // TILE) for i in range(2 * HEIGHT // TILE)]
for i in range(len(map)):
    map[i][38] = 1
    map[i][39] = 1
    # map[i][35] = 1
map[38][35] = 1
map[37][35] = 1
# print(map[400])
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((750, 600), pygame.RESIZABLE)
pygame.display.set_caption("terraria")
all_sprites = pygame.sprite.Group()
player = Player(WIDTH // 2 // TILE * TILE, HEIGHT // 2 // TILE * TILE)
all_sprites.add(player)
