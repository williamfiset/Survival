"""
This is the startpoint of the application, build and run to execute program.

"""

import pygame
import miscellaneous
import worldCreator

from EventResponder import *
from Tile import Tile
from Zombie import Zombie
from Survivor import Survivor
from Bullet import Bullet
from AStar import AStar
from time import sleep



__author__ = 'William Fiset, Alex Mason'


# Initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Zombie - Survival")

# Startup game theme
# pygame.mixer.music.load('audio/zombie_theme.ogg')
# pygame.mixer.music.play(-1)

# Creates a world from the text file called map.txt
worldCreator.create_world("map.txt")

# Global Game constants
SCREEN_WIDTH = Tile.TILE_SIZE * 22
SCREEN_HEIGHT = Tile.TILE_SIZE * 14
WORLD_WIDTH, WORLD_HEIGHT = worldCreator.get_dimension()


# Local constants
PAUSE_TIME   = 2.5  # seconds
FPS          = 20

total_frames = 0
screen       = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock        = pygame.time.Clock()
survivor     = Survivor(Tile.TILE_SIZE * 2, Tile.TILE_SIZE * 4)


while survivor.health > 0:

    # USER INPUT

    EventResponder.userInteraction(screen, survivor)

    # UPDATE GAME

    AStar(survivor, total_frames, FPS)
    Zombie.spawn(total_frames, FPS)
    survivor.movement()

    # RENDING ACTIONS

    Tile.update(screen)
    Bullet.update(screen)
    Zombie.update(screen, survivor)
    survivor.draw(screen)
    miscellaneous.display_health_bar(screen, survivor.health , SCREEN_WIDTH)

    pygame.display.flip()
    clock.tick(FPS)

    total_frames += 1

miscellaneous.display_end_game_screen(screen, PAUSE_TIME)

sleep(PAUSE_TIME)





