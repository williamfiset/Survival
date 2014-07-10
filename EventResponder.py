
"""

The eventResponder module takes care of all user input (mouse & keyboard)

"""



import pygame, sys
from tile import Tile
from bullet import Bullet


def userInteraction(screen, survivor):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:

                survivor.current += 1
                survivor.current %= 3

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: # North
        future_tile_number = survivor.get_number() - Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('n')
                # survivor.y -= survivor.height                   

    if keys[pygame.K_s]: # South
        future_tile_number = survivor.get_number() + Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('s')
                # survivor.y += survivor.height 

    if keys[pygame.K_a]: # West
        future_tile_number = survivor.get_number() - Tile.H

        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)    
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('w')
                # survivor.x -= survivor.width 

    if keys[pygame.K_d]: # East
        future_tile_number = survivor.get_number() + Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('e')
                # survivor.x += survivor.width 

    if keys[pygame.K_LEFT]:
        survivor.rotate('w')
        Bullet(survivor.centerx, survivor.centery, -10, 0, 'w', survivor.get_bullet_type() )

    elif keys[pygame.K_RIGHT]:
        survivor.rotate('e')
        Bullet(survivor.centerx, survivor.centery, 10, 0, 'e', survivor.get_bullet_type() )
    
    elif keys[pygame.K_UP]:
        survivor.rotate('n')
        Bullet(survivor.centerx, survivor.centery, 0, -10, 'n', survivor.get_bullet_type() )
    
    elif keys[pygame.K_DOWN]:
        survivor.rotate('s')
        Bullet(survivor.centerx, survivor.centery, 0, 10, 's', survivor.get_bullet_type() )




