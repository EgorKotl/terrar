import pygame as pg
import random
from colors import *
from terrar_mobs import *
from terrar_inventory import *

all_sprites = pg.sprite.Group()
spawn = [SC_WIDTH / 2, SC_HEIGHT / 2]
player = Player(spawn[0], spawn[1])
all_sprites.add(player)
running = True
camera = pg.Vector2(0, 0)
mode = 0
kdinv = 10
invent = inventory()
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
        # if event.type == pygame.MOUSEMOTION:
        #     print(pygame.Vector2(event.pos), player.pos,'aa')
    all_sprites.update()
    camera += player.now
    for s in all_sprites:
        screen.blit(s.image, s.rect.move(camera))
    # all_sprites.draw(screen)
    mapping(camera, player)
    invent.draw(screen)
    contur(f"Здоровье: {player.hp}/{player.maxhp}", WHITE, BLACK, SC_WIDTH - 200, 1, 1.5)
    pg.display.flip()

pg.quit()
