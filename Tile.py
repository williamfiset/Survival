"""

The Tile class is an object representation of a tile on the screen 

"""

__author__ = 'William Fiset'

import pygame

class Tile(pygame.Rect):

    floor_tile_img = pygame.image.load('images/tiles/surface_tile_gray.png')
    wall_tile_img = pygame.image.load("images/tiles/dark_wall.png")

    # Define all the different kinds of tiles that exist
    class Type:
        FLOOR = '-'
        WALL = 'w'

    list_ = []
    TILE_SIZE     = 32
    total_tiles   = 1
    H, V          = 1, 22

    def __init__(self, x, y, tileType):

        # AStar Variables
        self.parent = None
        self.H, self.G, self.F = 0, 0, 0

        # Tile object specific variables
        self.type = tileType
        self.number = Tile.total_tiles

        # Determine if this tile will be walkable or not
        if tileType == Tile.Type.FLOOR:
            self.walkable = True
        elif tileType == Tile.Type.WALL:
            self.walkable = False
        
        pygame.Rect.__init__(self, (x, y), (Tile.TILE_SIZE, Tile.TILE_SIZE))
        Tile.list_.append(self)
        Tile.total_tiles += 1

    @staticmethod
    def get_tile(number):
        for tile in Tile.list_:
            if tile.number == number:
                return tile

    @staticmethod
    def update(screen):

        for tile in Tile.list_:
            if tile.type == Tile.Type.FLOOR:
                screen.blit(Tile.floor_tile_img, (tile.x, tile.y))

            elif tile.type == Tile.Type.WALL:
                screen.blit(Tile.wall_tile_img, (tile.x, tile.y))










