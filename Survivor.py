"""
The Survivor file contorls the survivor and his or her movement and actions.
"""

import pygame
# from tile import Tile  # imported, but not used
from Character import Character
from Character import Direction


__author__ = 'William Fiset, Alex Mason'


class Survivor(Character):

    _velocity = 8

    GUN_IMAGES = [pygame.image.load('images/weapon/pistol.png'),
                pygame.image.load('images/weapon/shotgun.png'),
                pygame.image.load('images/weapon/automatic.png')]

    NUMBER_OF_GUNS = len(GUN_IMAGES)
    START_HEALTH = 1000

    def __init__(self, x, y):

        self.health = Survivor.START_HEALTH
        self.current = 0  # 0 -> pistol, 1 -> shotgun, 2 -> automatic
        self.direction = Direction.WEST
        self.img = pygame.image.load('images/survivor/survivor_w.png')

        Character.__init__(self, x, y)

    def get_bullet_type_based_on_weapon(self):

        if self.current == 0:
            return 'pistol'
        elif self.current == 1:
            return 'shotgun'
        elif self.current == 2:
            return 'automatic'

    """
    movement determines if the player should move,
    and what direction to move in
    """

    def movement(self):

        if self.isMoving():  # Target is set

            x_destination = self.x - self.dx
            y_destination = self.y - self.dy

            if x_destination < 0:  # --->
                self.x += Survivor._velocity

            elif x_destination > 0:  # <----
                self.x -= Survivor._velocity

            if y_destination > 0:  # up
                self.y -= Survivor._velocity

            elif y_destination < 0:  # dopwn
                self.y += Survivor._velocity

            if x_destination == 0 and y_destination == 0:
                self.dx, self.dy = 0, 0

    def draw(self, screen):

        screen.blit(self.img, (self.x, self.y))

        h = self.width / 2
        img = Survivor.GUN_IMAGES[self.current]

        if self.direction == Direction.WEST:
            screen.blit(img, (self.x, self.y + h))

        elif self.direction == Direction.EAST:
            img = pygame.transform.flip(img, True, False)
            screen.blit(img, (self.x + h, self.y + h))

        elif self.direction == Direction.SOUTH:
            img = pygame.transform.rotate(img, 90)  # CCW
            screen.blit(img, (self.x + h, self.y + h))

        elif self.direction == Direction.NORTH:
            south = pygame.transform.rotate(img, 90)
            img = pygame.transform.flip(south, False, True)
            screen.blit(img, (self.x + h, self.y - h))

    """ Changes player direction iamge"""
    def rotate(self, direction):

        path = 'images/survivor/survivor_'
        png = '.png'

        if direction == Direction.NORTH:
            if self.direction != Direction.NORTH:
                self.direction = Direction.NORTH
                self.img = pygame.image.load(path + self.direction + png)

        if direction == Direction.SOUTH:
            if self.direction != Direction.SOUTH:
                self.direction = Direction.SOUTH
                self.img = pygame.image.load(path + self.direction + png)

        if direction == Direction.EAST:
            if self.direction != Direction.EAST:
                self.direction = Direction.EAST
                self.img = pygame.image.load(path + self.direction + png)

        if direction == Direction.WEST:
            if self.direction != Direction.WEST:
                self.direction = Direction.WEST
                self.img = pygame.image.load(path + self.direction + png)

    def cycle_weapon(self):

        self.current += 1
        self.current %= Survivor.NUMBER_OF_GUNS

