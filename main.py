"""
This is the startpoint of the application, build and run to execute program.

"""

import pygame
# import sys  # imported, but not used
from Funk import *

from EventResponder import *
from Tile import Tile
from Zombie import Zombie
from Survivor import Survivor
from Bullet import Bullet
from AStar import AStar
from time import sleep
from mapMaker import MapMaker

__author__ = 'William Fiset'


# Initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()


# Startup game theme
# pygame.mixer.music.load('audio/zombie_theme.ogg')
# pygame.mixer.music.play(-1)


# Global Game constants
SCREEN_WIDTH = Tile.TILE_SIZE * 22
SCREEN_HEIGHT = Tile.TILE_SIZE * 14

# Local constants
DUNGEON_IMAGE = pygame.image.load('images/dungeon.jpg')
PAUSE_TIME = 2.5  # seconds
FPS = 20


total_frames = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
survivor = Survivor(Tile.TILE_SIZE * 2, Tile.TILE_SIZE * 4)

# Sets up game grid by creating the tiles
Tile.pre_init(screen)


# Displays the 'zombies ate your brain credits'
def display_end_game_screen():

    sleep(PAUSE_TIME)
    screen.blit(pygame.image.load('images/dead.jpg'), (0, 0))

    # Actually updates the screen
    pygame.display.update()


while survivor.health > 0:

    # USER INPUT

    EventResponder.userInteraction(screen, survivor)

    # UPDATE GAME

    AStar(survivor, total_frames, FPS)
    Zombie.spawn(total_frames, FPS)
    survivor.movement()

    # RENDING ACTIONS

    screen.blit(DUNGEON_IMAGE, (0, 0))
    Bullet.super_massive_jumbo_loop(screen)
    Zombie.update(screen, survivor)
    survivor.draw(screen)
    Funk.text_to_screen(screen, 'Health: {0}'.format(survivor.health), 0, 0)

    pygame.display.flip()

    clock.tick(FPS)
    total_frames += 1

display_end_game_screen()

sleep(PAUSE_TIME)
