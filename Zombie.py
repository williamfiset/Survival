import pygame
from Tile import Tile
from random import randint
from Character import Character
from Character import Direction

__author__ = 'William Fiset'

"""
The Zombie class defines a zombie NPC for this game
"""

class Zombie(Character):

    # Character definition in map.txt
    SPAWN_ZONE = "!"

    ORIGINAL_ZOMBIE_IMAGE = pygame.image.load('images/zombie.png')
    START_HEALTH = 100

    list_ = []
    spawn_tiles = [] 
    _velocity = 4

    def __init__(self, x, y):

        self.direction = Direction.WEST
        self.health = Zombie.START_HEALTH
        self.img = Zombie.ORIGINAL_ZOMBIE_IMAGE

        # Character.__init__(self, x, y)
        super(Character, self).__init__(x, y)
        Zombie.list_.append(self)

    @staticmethod
    def update(screen, survivor):

        for zombie in Zombie.list_:

            # Draws the zombie image on the screen
            screen.blit(zombie.img, (zombie.x, zombie.y))


            if survivor.x % Tile.width == 0 and survivor.y % Tile.height == 0:
                if zombie.x % Tile.width == 0 and zombie.y % Tile.height == 0:

                    survivor_tile_number = survivor.get_number()

                    N = survivor_tile_number - (Tile.V)
                    S = survivor_tile_number + (Tile.V)
                    E = survivor_tile_number + (Tile.H)
                    W = survivor_tile_number - (Tile.H)

                    # Tests if the zombie is either on the tile number of the survivor
                    # or any other adjacent tiles
                    if zombie.get_number() in [N, S, E, W, survivor_tile_number]:
                        survivor.health -= 5

            if zombie.health <= 0:
                Zombie.list_.remove(zombie)

            zombie.__movement()

    # This method is responsible for the zombie's rotation and movement
    def __movement(self):

        if self.dx != 0 and self.dy != 0:  # Target is set

            X = self.x - self.dx
            Y = self.y - self.dy

            if X < 0:  # --->
                self.x += Zombie._velocity
                self.rotate(Direction.EAST, Zombie.ORIGINAL_ZOMBIE_IMAGE)

            elif X > 0:  # <----
                self.x -= Zombie._velocity
                self.rotate(Direction.WEST, Zombie.ORIGINAL_ZOMBIE_IMAGE)

            if Y > 0:  # up
                self.y -= Zombie._velocity
                self.rotate(Direction.NORTH, Zombie.ORIGINAL_ZOMBIE_IMAGE)

            elif Y < 0:  # down
                self.y += Zombie._velocity
                self.rotate(Direction.SOUTH, Zombie.ORIGINAL_ZOMBIE_IMAGE)

            if X == 0 and Y == 0:
                self.dx, self.dy = 0, 0

    @staticmethod
    def spawn(total_frames, FPS):
        
        # spawn a new zombie every FPS frames
        if total_frames % (FPS) == 0:

            # Perform a sound effect somewhat periodically 
            if total_frames % (FPS * 6) == 0:

                random_sound_effect = randint(0, 2)
                # TURNED OFF SOUND FOR DEBUGGING
                """
                sounds = [pygame.mixer.Sound('audio/zs1.ogg'),
                          pygame.mixer.Sound('audio/zs2.ogg'),
                          pygame.mixer.Sound('audio/zs3.ogg')]
                sound = sounds[ random_sound_effect ]
                sound.play()
                """

            # Get the spawn tile number, get the tile itself and create a zombie there
            random_spawn_zone = randint(0, len(Zombie.spawn_tiles) - 1)
            tile_num = Zombie.spawn_tiles[random_spawn_zone]
            spawn_node = Tile.get_tile(tile_num)

            Zombie(spawn_node.x, spawn_node.y)




