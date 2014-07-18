"""

This File is intended to handle everything to do with create a world

"""

from Tile import Tile
from Zombie import Zombie

__author__ = 'William Fiset'

WORLD_WIDTH, WORLD_HEIGHT = 0, 0

# CharacterNotDefined simply means that map.txt file contains a character we have not defined  
class CharacterNotDefined(Exception): pass


def create_world(world_text_file):

	global WORLD_HEIGHT, WORLD_WIDTH

	map_ = open(world_text_file)

	# Loop through the entire level file, reading each line at a time
	for column, line in enumerate(map_.readlines()):

		WORLD_HEIGHT += 1
		WORLD_WIDTH = len(line)

		for row, character in enumerate(line):

			if character == '\n': continue

			tile_type = None

			# Checks for each block Type
			if character == Tile.Type.WALL:
				Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.WALL)

			elif character == Tile.Type.FLOOR:
				Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.FLOOR)

			# Marks a zombie spawn tile
			elif character == Zombie.SPAWN_ZONE:
				Zombie.spawn_tiles.append(Tile.total_tiles)
				Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.FLOOR)
			
			else:
				errorStr = "\n\nCharacter '{0}' is not defined in Tile.Type.* \n"
				raise CharacterNotDefined(errorStr.format(character))

	print WORLD_WIDTH, WORLD_HEIGHT

	# Might not be a bad idea to close a file after you open it ;P
	map_.close()

def get_dimension():
	
	if WORLD_WIDTH != 0 and WORLD_HEIGHT != 0:
		return (WORLD_WIDTH, WORLD_HEIGHT)
	else:
		raise Exception("World not yet created")

	















