import pygame

class Tile(pygame.Rect):

    # Define all the different kinds of tiles that exist
    class Type:
        FLOOR = '-'
        WALL = 'w'

    list_ = []
    TILE_SIZE = 32
    width, height = 32, 32
    total_tiles = 1
    H, V = 1, 22

    @staticmethod
    def pre_init(screen):
        for y in range(0, screen.get_height(), Tile.TILE_SIZE):
            for x in range(0, screen.get_width(), Tile.TILE_SIZE):
                if Tile.total_tiles in Tile.invalids:
                    Tile(x, y, Tile.Type.WALL)
                else:
                    Tile(x, y, Tile.Type.FLOOR)

    def __init__(self, x, y, tileType):

        self.parent = None
        self.H, self.G, self.F = 0, 0, 0

        self.type = tileType
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        if tileType == Tile.Type.FLOOR:
            self.walkable = True
        elif tileType == Tile.Type.WALL:
            self.walkable = False
        

        pygame.Rect.__init__(self, (x, y), (Tile.width, Tile.height))

        Tile.list_.append(self)

    @staticmethod
    def get_tile(number):
        for tile in Tile.list_:
            if tile.number == number:
                return tile