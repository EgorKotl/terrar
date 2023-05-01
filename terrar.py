import pygame as pg
import random
from colors import *
from terrar_mobs import *
from terrar_inventory import *


def place_block(type):
    x, y = player.pos + mouse_pos - (SC_WIDTH / 2, SC_HEIGHT / 2)
    global map
    # print(x, y, player.pos)
    if (player.pos[0] - x) ** 2 + (player.pos[1] - y) ** 2 <= 10000:
        if not map[int(x) // TILE][int(y) // TILE]:
            map[int(x) // TILE][int(y) // TILE] = type


all_sprites = pg.sprite.Group()
spawn = [SC_WIDTH / 2, SC_HEIGHT / 2]
player = Player(spawn[0], spawn[1])
all_sprites.add(player)
running = True
camera = pg.Vector2(0, 0)
mode = 0
kdinv = 10
is_placing = False
invent = inventory()
mouse_pos = [0, 0]

while running:
    clock.tick(FPS)
    screen.fill(LIGHT_BLUE)
    pressed = pg.key.get_pressed()
    kdinv += 1
    if kdinv >= 10 and pressed[pg.K_ESCAPE]:
        mode += 1
        mode %= 2
        kdinv = 0
        invent.change_mode(mode)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_placing = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                is_placing = False
    if is_placing:
        place_block(invent.get_element(0, invent.tec)[0])
    mouse_pos = pg.mouse.get_pos()
    all_sprites.update()
    camera += player.now
    for s in all_sprites:
        screen.blit(s.image, s.rect.move(camera))
    # all_sprites.draw(screen)
    mapping(camera, player)
    pg.draw.rect(screen, YELLOW,
                 ((mouse_pos[0] - camera[0] % TILE) // TILE * TILE + camera[0] % TILE,
                  (mouse_pos[1] - camera[1] % TILE) // TILE * TILE + camera[1] % TILE, TILE,
                  TILE), 2)
    invent.draw(screen)
    contur(f"Здоровье: {player.hp}/{player.maxhp}", WHITE, BLACK, SC_WIDTH - 200, 1, 1.5)
    pg.display.flip()

pg.quit()
