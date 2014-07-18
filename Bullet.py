import pygame

from Tile import Tile
from Zombie import Zombie
from Character import Direction

__author__ = 'William Fiset, Alex Mason, Gabriel Antao'


class Bullet(pygame.Rect):
    # Why this default width and height values here?
    # width, height = 7, 10
    list_ = []

    SHOTGUN_BULLET_DISTANCE = 50
    PISTOL_BULLET_DISTANCE  = 30

    LAST_BULLET_INDEX = -1

    _weapon_bullet_images = {'pistol': pygame.image.load('images/weapon/pistol_b.png'),
    'shotgun': pygame.image.load('images/weapon/shotgun_b.png'),
    'automatic': pygame.image.load('images/weapon/automatic_b.png')}

    _gun_damage = {'pistol': (Zombie.START_HEALTH / 3) + 1,
                'shotgun': Zombie.START_HEALTH / 2,
                'automatic': (Zombie.START_HEALTH / 6) + 1}

    def __init__(self, x, y, velx, vely, direction, type_):

        # Restricts the firing rate of the shotgun and the pistol
        if Bullet.__firing_rate_check(x, y, type_):

            self.type = type_
            self.direction = direction
            self.velx, self.vely = velx, vely

            self.__rotation_transformation(direction, type_)

            pygame.Rect.__init__(self, x, y, self.img.get_width(), self.img.get_height())
            Bullet.list_.append(self)


    # Check if the last bullet fired was far enough from the
    # previous bullet to shoot another one
    @staticmethod
    def __firing_rate_check(x, y, gun_type):

        # We have some existing bullets
        if len(Bullet.list_) > 0:

            # Get the x & y differences to the last bullet created
            dx = abs( Bullet.list_[Bullet.LAST_BULLET_INDEX].x - x )
            dy = abs( Bullet.list_[Bullet.LAST_BULLET_INDEX].y - y )

            # Since the Bullet is either moving in the x or y plane, thus either dy or dx will be zero.
            # Grab whichever is NOT zero
            distance_to_last_bullet = max(dy, dx)

            if gun_type == 'shotgun':

                if distance_to_last_bullet < Bullet.SHOTGUN_BULLET_DISTANCE:
                    return False

            elif gun_type == 'pistol':

                if distance_to_last_bullet < Bullet.PISTOL_BULLET_DISTANCE:
                    return False

        return True

    # Change the image direction of the bullet
    def __rotation_transformation(self, direction, type_):

        if direction == Direction.NORTH:
            # Just rotate clockwise 90 degrees is enough
            self.img = pygame.transform.rotate(Bullet._weapon_bullet_images[type_], -90)

        elif direction == Direction.SOUTH:
            self.img = pygame.transform.rotate(Bullet._weapon_bullet_images[type_], 90)  # CCW

        elif direction == Direction.EAST:
            self.img = pygame.transform.flip(Bullet._weapon_bullet_images[type_], True, False)

        elif direction == Direction.WEST:
            self.img = Bullet._weapon_bullet_images[type_]

    # Returns a boolean value on whether or not the bullet is off the screen
    def offscreen(self, screen):

        if self.x < 0: # left side
            return True
        elif self.y < 0: # up
            return True
        elif self.x + self.width > screen.get_width():  # right edge
            return True
        elif self.y + self.height > screen.get_height(): # down
            return True

        return False

    @staticmethod
    def update(screen):
        for bullet in Bullet.list_:

            # update bullet position
            bullet.x += bullet.velx
            bullet.y += bullet.vely

            # draw bullet on screen
            screen.blit(bullet.img, (bullet.x, bullet.y))

            if bullet.offscreen(screen):
                Bullet.list_.remove(bullet)
                continue

            # Check if any bullet has hit a zombie
            for zombie in Zombie.list_:
                if bullet.colliderect(zombie):

                    zombie.health -= Bullet._gun_damage[bullet.type]
                    Bullet.list_.remove(bullet)
                    break

            # Check if a bullet has hit a wall
            for tile in Tile.list_:
                rect = pygame.Rect(bullet.x + bullet.velx, bullet.y + bullet.vely, bullet.width, bullet.height)

                if rect.colliderect(tile) and not(tile.walkable):

                    # I think the try block is because we might have already removed this bullet
                    # when it hit a zombie?
                    try:
                        Bullet.list_.remove(bullet)
                    except:
                        break


