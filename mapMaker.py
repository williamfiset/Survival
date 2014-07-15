

"""

This class is intended to construct a world from a text file.

"""

from Tile import Tile
from Zombie import Zombie

__author__ = 'William Fiset'


# CharacterNotDefined simply means that map.txt file contains a character we have not defined  
class CharacterNotDefined(Exception): pass

class MapMaker:

	def __init__(self, world_text_file):

		try:

			# Loop through the entire level file, reading each line at a time
			for column, line in enumerate(open(world_text_file).readlines()):
				for row, character in enumerate(line):

					if character == '\n': continue

					tile_type = None

					# Checks for each block Type
					if character == Tile.Type.WALL:
						Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.WALL)

					elif character == Tile.Type.FLOOR:
						Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.FLOOR)

					# Zombie Spawn zone
					elif character == "!":
						Zombie.spawn_tiles.append(Tile.total_tiles)
						Tile(row * Tile.TILE_SIZE, column * Tile.TILE_SIZE, Tile.Type.FLOOR)
					

					else:
						raise CharacterNotDefined("\n\nCharacter '{0}' is not defined in Tile.Type.* \n".format(character))

		
		except Exception, error:
			raise error
		











