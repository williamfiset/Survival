import pygame
from Tile import Tile
from random import randint
from Character import Character
from Character import Direction

__author__ = 'William Fiset'

"""
The Zombie class defines the zombie NPC's for the game
"""


class Zombie(Character):

    ORIGINAL_ZOMBIE_IMAGE = pygame.image.load('images/zombie.png')
    START_HEALTH = 100

    list_ = []
    spawn_tiles = [] # (24 , 26) # (9, 42, 91, 134, 193, 219, 274)
    _velocity = 4

    def __init__(self, x, y):

        self.direction = Direction.WEST
        self.health = Zombie.START_HEALTH
        self.img = Zombie.ORIGINAL_ZOMBIE_IMAGE

        Character.__init__(self, x, y)
        Zombie.list_.append(self)

    @staticmethod
    def update(screen, survivor):

        for zombie in Zombie.list_:

            screen.blit(zombie.img, (zombie.x, zombie.y))

            if survivor.x % Tile.width == 0 and survivor.y % Tile.height == 0:
                if zombie.x % Tile.width == 0 and zombie.y % Tile.height == 0:

                    tn = survivor.get_number()

                    N = tn - (Tile.V)
                    S = tn + (Tile.V)
                    E = tn + (Tile.H)
                    W = tn - (Tile.H)

                    NSEW = [N, S, E, W, tn]

                    if zombie.get_number() in NSEW:
                        survivor.health -= 5

            if zombie.health <= 0:
                Zombie.list_.remove(zombie)

            if zombie.dx != 0 and zombie.dy != 0:  # Target is set

                X = zombie.x - zombie.dx
                Y = zombie.y - zombie.dy

                if X < 0:  # --->
                    zombie.x += Zombie._velocity
                    zombie.rotate(Direction.EAST, Zombie.ORIGINAL_ZOMBIE_IMAGE)

                elif X > 0:  # <----
                    zombie.x -= Zombie._velocity
                    zombie.rotate(Direction.WEST, Zombie.ORIGINAL_ZOMBIE_IMAGE)

                if Y > 0:  # up
                    zombie.y -= Zombie._velocity
                    zombie.rotate(Direction.NORTH, Zombie.ORIGINAL_ZOMBIE_IMAGE)

                elif Y < 0:  # dopwn
                    zombie.y += Zombie._velocity
                    zombie.rotate(Direction.SOUTH, Zombie.ORIGINAL_ZOMBIE_IMAGE)

                if X == 0 and Y == 0:
                    zombie.dx, zombie.dy = 0, 0

    @staticmethod
    def spawn(total_frames, FPS):
        if total_frames % (FPS) == 0:

            if total_frames % (FPS * 6) == 0:

                r = randint(0, 2)
                # TURNED OFF SOUND FOR DEBUGGING
                """
                sounds = [pygame.mixer.Sound('audio/zs1.ogg'),
                          pygame.mixer.Sound('audio/zs2.ogg'),
                          pygame.mixer.Sound('audio/zs3.ogg')]
                sound = sounds[ r ]
                sound.play()
                """

            r = randint(0, len(Zombie.spawn_tiles) - 1)
            tile_num = Zombie.spawn_tiles[r]
            spawn_node = Tile.get_tile(tile_num)

            Zombie(spawn_node.x, spawn_node.y)