import pygame
import random
from colors import *
from terrar_mobs import *




running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEMOTION:
        #     print(pygame.Vector2(event.pos), player.pos)
    all_sprites.draw(screen)
    all_sprites.update()
    mapping()
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
