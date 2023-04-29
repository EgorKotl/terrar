import pygame as pg
import random
from colors import *
from terrar_mobs import *

all_sprites = pg.sprite.Group()
spawn = [SC_WIDTH / 2, SC_HEIGHT / 2]
player = Player(spawn[0], spawn[1])
all_sprites.add(player)
running = True
camera = pg.Vector2(0, 0)

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

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
    pg.display.flip()
    dt = clock.tick(60)

pg.quit()
