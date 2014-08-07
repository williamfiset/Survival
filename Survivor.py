"""
The Survivor file contorls the survivor and his or her movement and actions.
"""

import pygame
from Character import Character
from Character import Direction
from Weapon import Weapon


__author__ = 'William Fiset, Alex Mason'


class Survivor(Character):

    _velocity = 8

    START_HEALTH = 1000

    def __init__(self, x, y):

        self.health = Survivor.START_HEALTH
        self.current_weapon = Weapon(Weapon.PISTOL) 
        self.direction = Direction.WEST
        self.img = pygame.image.load('images/survivor/survivor_w.png')

        Character.__init__(self, x, y)

    def get_bullet_type_based_on_weapon(self):

        return self.current_weapon.weapon_type


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

            elif y_destination < 0:  # down
                self.y += Survivor._velocity

            if x_destination == 0 and y_destination == 0:
                self.dx, self.dy = 0, 0

    def draw(self, screen):

        gun_img = Weapon.get_weapon_image( self.current_weapon )

        if self.direction == Direction.WEST:
            screen.blit(gun_img, (self.centerx - gun_img.get_rect().width, self.centery))

        elif self.direction == Direction.EAST:
            gun_img = pygame.transform.flip(gun_img, True, False)
            screen.blit(gun_img, (self.centerx, self.centery))

        elif self.direction == Direction.SOUTH:
            gun_img = pygame.transform.rotate(gun_img, 90)  # CCW
            screen.blit(gun_img, (self.centerx, self.centery))
        
        # weapon drawn below survivor
        elif self.direction == Direction.NORTH:
            south = pygame.transform.rotate(gun_img, 90)
            gun_img = pygame.transform.flip(south, False, True)
            screen.blit(gun_img, (self.centerx, self.centery - gun_img.get_rect().height))

        screen.blit(self.img, (self.x, self.y))


    """ Changes player direction image"""
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

    # Cycle through the weapons 
    def cycle_weapon(self):

        if self.current_weapon.weapon_type == Weapon.PISTOL:
            self.current_weapon = Weapon(Weapon.SHOTGUN)

        elif self.current_weapon.weapon_type == Weapon.SHOTGUN:
            self.current_weapon = Weapon(Weapon.AUTOMATIC)

        elif self.current_weapon.weapon_type == Weapon.AUTOMATIC:
            self.current_weapon = Weapon(Weapon.PISTOL)
        











