











































import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction
from A_Star import A_Star
from time import sleep

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load('audio/zombie_theme.ogg')
# pygame.mixer.music.play(-1)


SCREEN_WIDTH, SCREEN_HEIGHT = Tile.TILE_SIZE * 22, Tile.TILE_SIZE * 14
FPS = 20

total_frames = 0

screen   = pygame.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT))
clock    = pygame.time.Clock()
dungeon  = pygame.image.load('images/dungeon.jpg')
survivor = Survivor(Tile.TILE_SIZE * 2, Tile.TILE_SIZE * 4)

Tile.pre_init(screen)


while True:

    # Drawing to Screen

    screen.blit(dungeon, (0, 0) )

    Zombie.spawn(total_frames, FPS)
    Zombie.update(screen, survivor)

    survivor.movement()

    Bullet.super_massive_jumbo_loop(screen)

    A_Star(screen, survivor, total_frames, FPS)
    interaction(screen, survivor)

    survivor.draw(screen)

    Funk.text_to_screen(screen, 'Health: {0}'.format(survivor.health), 0,0)

    pygame.display.flip()
    clock.tick(FPS)
    total_frames += 1

    if survivor.health <= 0:

        sleep(2.5)
        screen.blit(pygame.image.load('images/dead.jpg'), (0,0))
        pygame.display.update()

        break

sleep(4)












































