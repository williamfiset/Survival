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

    invalids = [1, 2, 3, 4, 5, 6, 7, 8,
        10, 11, 12, 13, 14,
        20, 21, 22, 23, 26, 28, 29,
        30, 32, 35, 36, 41, 44, 45,
        58, 59,
        61, 62, 64, 66, 67,
        70, 77, 78,
        88, 89,
        92, 94, 95, 99,
        100, 102, 103, 105, 106, 107, 108,
        110, 111, 112, 113, 117, 119,
        124, 128,
        133, 139,
        141, 142, 143, 146,
        152, 154, 155, 156, 157, 158, 159,
        168,
        172, 174, 176, 177,
        181, 182, 184, 187, 188, 189,
        190, 191, 192, 194, 197, 198, 199,
        204, 206, 208, 209, 212, 214, 215,
        220, 221,
        241, 242, 243,
        251,
        264, 265,
        270, 273, 275, 278,
        280, 281, 283, 285, 286, 287, 288, 289,
        290, 291, 292, 293, 294, 295, 296, 297, 298, 299,
        300, 301, 302, 303, 304, 305, 306, 307, 308]

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