import pygame

from Tile import Tile
from Zombie import Zombie
# from random import randint  # imported, but not used
from Character import Direction

__author__ = 'William Fiset'


class Bullet(pygame.Rect):

    width, height = 7, 10
    list_ = []

    imgs = {'pistol': pygame.image.load('images/weapon/pistol_b.png'),
    'shotgun': pygame.image.load('images/weapon/shotgun_b.png'),
    'automatic': pygame.image.load('images/weapon/automatic_b.png')}

    gun_dmg = {'pistol': (Zombie.START_HEALTH / 3) + 1,
                'shotgun': Zombie.START_HEALTH / 2,
                'automatic': (Zombie.START_HEALTH / 6) + 1}

    def __init__(self, x, y, velx, vely, direction, type_):

        if type_ == 'shotgun' or type_ == 'pistol':
            try:

                last_item = -1
                dx = abs( Bullet.list_[last_item].x - x )
                dy = abs( Bullet.list_[last_item].y - y )

                if dx < 50 and dy < 50 and type_ == 'shotgun':
                    return

                if dx < 30 and dy < 30 and type_ == 'pistol':
                    return

            except:
                pass

        self.type = type_
        self.direction = direction
        self.velx, self.vely = velx, vely

        # Change the direction of the bullet
        if direction == Direction.NORTH:
            south = pygame.transform.rotate(Bullet.imgs[type_], 90)  # CCW
            self.img = pygame.transform.flip(south, False, True)

        elif direction == Direction.SOUTH:
            self.img = pygame.transform.rotate(Bullet.imgs[type_], 90)  # CCW

        elif direction == Direction.EAST:
            self.img = pygame.transform.flip(Bullet.imgs[type_], True, False)

        elif direction == Direction.WEST:
            self.img = Bullet.imgs[type_]

        pygame.Rect.__init__(self, x, y, Bullet.width, Bullet.height)

        Bullet.list_.append(self)

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
    def super_massive_jumbo_loop(screen):

        for bullet in Bullet.list_:

            bullet.x += bullet.velx
            bullet.y += bullet.vely

            screen.blit(bullet.img, (bullet.x, bullet.y))

            if bullet.offscreen(screen):
                Bullet.list_.remove(bullet)
                continue

            for zombie in Zombie.list_:
                if bullet.colliderect(zombie):

                    """
                    The same bullet cannot be used to kill
                    multiple zombies and as the bullet was
                    no longer in Bullet.list_ error was raised
                    """

                    zombie.health -= Bullet.gun_dmg[bullet.type]
                    Bullet.list_.remove(bullet)
                    break

            for tile in Tile.list_:

                if bullet.colliderect(tile) and not(tile.walkable):
                    try:
                        Bullet.list_.remove(bullet)
                    except:
                        break  # if bullet cannot be removed, then GTFO