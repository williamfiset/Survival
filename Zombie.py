



































































































import pygame
from Tile import Tile
from random import randint 


class Zombie(Character):

    List = []
    spawn_tiles = (9,42,91,134,193,219,274)
    original_img = pygame.image.load('images/zombie.png')
    health = 100


    def __init__(self, x, y):

        self.direction = Direction.West
        self.health = Zombie.health
        self.img = Zombie.original_img
        Character.__init__(self, x, y)
        Zombie.List.append(self)

    @staticmethod
    def update(screen, survivor):

        for zombie in Zombie.List:
            
            screen.blit(zombie.img, (zombie.x, zombie.y))

            if survivor.x % Tile.width == 0 and survivor.y % Tile.height == 0:
                if zombie.x % Tile.width == 0 and zombie.y % Tile.height == 0:

                    tn = survivor.get_number()

                    N = tn + -(Tile.V)
                    S = tn +  (Tile.V)
                    E = tn +  (Tile.H)
                    W = tn + -(Tile.H)

                    NSEW = [N, S, E, W, tn]

                    if zombie.get_number() in NSEW:
                        survivor.health -= 5

            if zombie.health <= 0:
                Zombie.List.remove(zombie)

            if zombie.tx != None and zombie.ty != None: # Target is set

                X = zombie.x - zombie.tx
                Y = zombie.y - zombie.ty

                vel = 4
                if X < 0: # --->
                    zombie.x += vel
                    zombie.rotate('e', Zombie.original_img)

                elif X > 0: # <----
                    zombie.x -= vel
                    zombie.rotate('w', Zombie.original_img)

                if Y > 0: # up
                    zombie.y -= vel
                    zombie.rotate('n', Zombie.original_img)

                elif Y < 0: # dopwn
                    zombie.y += vel
                    zombie.rotate('s', Zombie.original_img)

                if X == 0 and Y == 0:
                    zombie.tx, zombie.ty = None, None
 
    @staticmethod
    def spawn(total_frames, FPS):
        if total_frames % (FPS) == 0:

            if total_frames % (FPS * 6) == 0:

                r = randint(0, 2)
                sounds = [pygame.mixer.Sound('audio/zs1.ogg'),
                        pygame.mixer.Sound('audio/zs2.ogg'),
                        pygame.mixer.Sound('audio/zs3.ogg')]
                sound = sounds[ r ]
                sound.play()

            r = randint(0, len(Zombie.spawn_tiles) - 1)
            tile_num = Zombie.spawn_tiles[r]
            spawn_node = Tile.get_tile(tile_num)
            Zombie(spawn_node.x, spawn_node.y)





