"""
The eventResponder module takes care of all user input (mouse & keyboard)
"""

import pygame
import sys
from Tile import Tile
from Bullet import Bullet
from Character import Direction 

__author__ = 'William Fiset, Alex Mason'


class EventResponder:

    def __init__(self):
        pass

    @staticmethod
    def userInteraction(screen, survivor):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # Press 'e' to cycle character weapon
                if event.key == pygame.K_e:
                    
                    # Change weapon
                    survivor.cycle_weapon()

        # Grab a list containing all the pressed keys
        keys = pygame.key.get_pressed()



        """ Character rotation with w,a,s,d keys """

        if keys[pygame.K_w]:  # North
            future_tile_number = survivor.get_number() - Tile.V
            
            if future_tile_number in range(1, Tile.total_tiles + 1):
                future_tile = Tile.get_tile(future_tile_number)
                
                if future_tile.walkable:
                    survivor.set_target(future_tile)
                    survivor.rotate(Direction.NORTH)
                    # survivor.y -= survivor.height

        if keys[pygame.K_s]:  # South
            future_tile_number = survivor.get_number() + Tile.V
            
            if future_tile_number in range(1, Tile.total_tiles + 1):
                future_tile = Tile.get_tile(future_tile_number)
                
                if future_tile.walkable:
                    survivor.set_target(future_tile)
                    survivor.rotate(Direction.SOUTH)
                    # survivor.y += survivor.height

        if keys[pygame.K_a]:  # West
            future_tile_number = survivor.get_number() - Tile.H

            if future_tile_number in range(1, Tile.total_tiles + 1):
                future_tile = Tile.get_tile(future_tile_number)

                if future_tile.walkable:
                    survivor.set_target(future_tile)
                    survivor.rotate(Direction.WEST)
                    # survivor.x -= survivor.width

        if keys[pygame.K_d]:  # East
            future_tile_number = survivor.get_number() + Tile.H

            if future_tile_number in range(1, Tile.total_tiles + 1):
                future_tile = Tile.get_tile(future_tile_number)

                if future_tile.walkable:
                    survivor.set_target(future_tile)
                    survivor.rotate(Direction.EAST)
                    # survivor.x += survivor.width



        """ Character firing Bullet with arrow keys  """

        bullet_velocity = survivor.current_weapon.bullet_velocity

        if keys[pygame.K_LEFT]:
            survivor.rotate(Direction.WEST)
            Bullet(survivor.centerx, survivor.centery, -bullet_velocity, 0,
                Direction.WEST, survivor.get_bullet_type_based_on_weapon())

        elif keys[pygame.K_RIGHT]:
            survivor.rotate(Direction.EAST)
            Bullet(survivor.centerx, survivor.centery, bullet_velocity, 0,
                Direction.EAST, survivor.get_bullet_type_based_on_weapon())

        elif keys[pygame.K_UP]:
            survivor.rotate(Direction.NORTH)
            Bullet(survivor.centerx, survivor.centery, 0, -bullet_velocity,
                Direction.NORTH, survivor.get_bullet_type_based_on_weapon())

        elif keys[pygame.K_DOWN]:
            survivor.rotate(Direction.SOUTH)
            Bullet(survivor.centerx, survivor.centery, 0, bullet_velocity,
                Direction.SOUTH, survivor.get_bullet_type_based_on_weapon())




