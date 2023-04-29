import pygame as pg
import random
from colors import *
from terrar_mobs import *

all_sprites = pygame.sprite.Group()
player = Player(WIDTH // 2 // TILE * TILE, HEIGHT // 2 // TILE * TILE)
all_sprites.add(player)
running = True
camera = pg.Vector2(0, 0)
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEMOTION:
        #     print(pygame.Vector2(event.pos), player.pos,'aa')
    all_sprites.update()
    camera += player.now
    for s in all_sprites:
        screen.blit(s.image, s.rect.move(camera))
    # all_sprites.draw(screen)

    mapping(camera,player)
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
