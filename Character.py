import pygame
from Tile import Tile

__author__ = 'William Fiset'

"""
Direction class is meant to act as an Enum
for the different directions you're facing
"""


class Direction():

    EAST = 'e'
    WEST = 'w'
    NORTH = 'n'
    SOUTH = 's'


"""
The Character class serves as a base class structure:

Hierarchy:

Character:
    Zombie
    Survivor
"""


class Character(pygame.Rect):

    WIDTH, HEIGHT = 32, 32

    def __init__(self, x, y):
        """
        targetX and targetY are the x & y
        positions the character is moving towards
        """
        self.targetX, self.targetY = 0, 0

        self.dy, self.dx = 0, 0

        pygame.Rect.__init__(self, x, y, Character.WIDTH, Character.HEIGHT)

    def __str__(self):
        outStr = "X: {0}  Y: {1}  dx: {2} dy: {3}"
        return outStr.format(self.x, self.y, self.dx, self.dy)

    def set_target(self, next_tile):
        if not self.isMoving():
            self.dx = next_tile.x
            self.dy = next_tile.y

    def get_number(self):
        #TODO -- make this more explicit
        return (((self.x / self.WIDTH) + Tile.H) +
            ((self.y / self.HEIGHT) * Tile.V))

    def get_tile(self):
        return Tile.get_tile(self.get_number())

    def rotate(self, direction, original_img):
        if direction == Direction.NORTH:
            if self.direction != Direction.NORTH:
                self.direction = Direction.NORTH
                south = pygame.transform.rotate(original_img, 90)  # CCW
                self.img = pygame.transform.flip(south, False, True)

        if direction == Direction.SOUTH:
            if self.direction != Direction.SOUTH:
                self.direction = Direction.SOUTH
                self.img = pygame.transform.rotate(original_img, 90)  # CCW

        if direction == Direction.EAST:
            if self.direction != Direction.EAST:
                self.direction = Direction.EAST
                self.img = pygame.transform.flip(original_img, True, False)

        if direction == Direction.WEST:
            if self.direction != Direction.WEST:
                self.direction = Direction.WEST
                self.img = original_img

    # Boolean method to determine if the character is moving or not
    def isMoving(self):
        return self.dy > 0 or self.dx > 0