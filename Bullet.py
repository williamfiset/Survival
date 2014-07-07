


import pygame

from tile import Tile
from zombie import Zombie
from random import randint 


class Bullet(pygame.Rect):
    
    width, height = 7, 10
    List = []

    imgs = { 'pistol' : pygame.image.load('images/weapon/pistol_b.png'),
            'shotgun' : pygame.image.load('images/weapon/shotgun_b.png'),
            'automatic' : pygame.image.load('images/weapon/automatic_b.png') }

    gun_dmg = {'pistol' : (Zombie.health / 3) + 1,
                'shotgun' : Zombie.health / 2,
                'automatic' : (Zombie.health / 6) + 1 }

    def __init__(self, x, y, velx, vely, direction, type_):

        if type_ == 'shotgun' or type_ == 'pistol':
            try:
                
                dx = abs(Bullet.List[-1].x - x)
                dy = abs(Bullet.List[-1].y - y)

                if dx < 50 and dy < 50 and type_ == 'shotgun':
                    return

                if dx < 30 and dy < 30 and type_ == 'pistol':
                    return

            except: pass


        self.type = type_
        self.direction = direction
        self.velx, self.vely = velx, vely

        if direction == 'n':
            south = pygame.transform.rotate(Bullet.imgs[type_], 90) # CCW
            self.img = pygame.transform.flip(south, False, True)

        if direction == 's':
            self.img = pygame.transform.rotate(Bullet.imgs[type_], 90) # CCW

        if direction == 'e':
            self.img = pygame.transform.flip(Bullet.imgs[type_], True, False)

        if direction == 'w':
            self.img = Bullet.imgs[type_]

        pygame.Rect.__init__(self, x, y, Bullet.width, Bullet.height)

        Bullet.List.append(self)


    def offscreen(self, screen):

        if self.x < 0:
            return True
        elif self.y < 0:
            return True
        elif self.x + self.width > screen.get_width(): # -->
            return True
        elif self.y + self.height > screen.get_height():
            return True
        return False


    @staticmethod
    def super_massive_jumbo_loop(screen):
        
        for bullet in Bullet.List:

            bullet.x += bullet.velx
            bullet.y += bullet.vely

            screen.blit(bullet.img, (bullet.x , bullet.y))

            if bullet.offscreen(screen):
                Bullet.List.remove(bullet)
                continue

            for zombie in Zombie.List:
                if bullet.colliderect(zombie):

                    """
                    The same bullet cannot be used to kill
                    multiple zombies and as the bullet was 
                    no longer in Bullet.List error was raised
                    """

                    zombie.health -= Bullet.gun_dmg[bullet.type]                
                    Bullet.List.remove(bullet)
                    break

            for tile in Tile.List:
                
                if bullet.colliderect(tile) and not(tile.walkable):
                    try:
                        Bullet.List.remove(bullet)
                    except:
                        break # if bullet cannot be removed, then GTFO



