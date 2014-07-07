








"""

William Fiset


This is the startpoint of the application, build and run to execute program

"""



import pygame, sys, funk

from tile import Tile
from zombie import Zombie
from survivor import Survivor
from bullet import Bullet

import eventResponder 
from aStar import AStar
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

    # USER INPUT

    eventResponder.userInteraction(screen, survivor)

    # UPDATE GAME

    AStar(survivor, total_frames, FPS)
    Zombie.spawn(total_frames, FPS)
    survivor.movement()
    
    # RENDING ACTIONS

    screen.blit(dungeon, (0, 0) )
    Bullet.super_massive_jumbo_loop(screen)
    Zombie.update(screen, survivor)
    survivor.draw(screen)
    funk.text_to_screen(screen, 'Health: {0}'.format(survivor.health), 0,0)

    pygame.display.flip()

    clock.tick(FPS)
    total_frames += 1

    if survivor.health <= 0:

        sleep(2.5)
        screen.blit(pygame.image.load('images/dead.jpg'), (0,0))
        pygame.display.update()

        break

sleep(2.5)












































