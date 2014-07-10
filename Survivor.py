
"""

The Survivor file contorls the survivor and his or her movement and actions.

"""

__author__ = 'William Fiset'



import pygame
from tile import Tile
from character import Character, Direction


class Survivor(Character):

	velocity = 8

	guns_img = [pygame.image.load('images/weapon/pistol.png'),
	pygame.image.load('images/weapon/shotgun.png'),
	pygame.image.load('images/weapon/automatic.png')]

	def __init__(self, x, y):

		self.health = 1000
		self.current = 0 # 0 -> pistol, 1 -> shotgun, 2 -> automatic
		self.direction = Direction.WEST
		self.img = pygame.image.load('images/survivor/survivor_w.png')

		Character.__init__(self, x, y)

	def get_bullet_type(self):

		if self.current == 0:
			return 'pistol'
		elif self.current == 1:
			return 'shotgun'
		elif self.current == 2:
			return 'automatic'

	# movement determines if the player should move, and what direction to move in
	def movement(self):

		if self.isMoving(): # Target is set

			xDestination = self.x - self.dx
			yDestination = self.y - self.dy

			if xDestination < 0: # --->
				self.x += Survivor.velocity

			elif xDestination > 0: # <----
				self.x -= Survivor.velocity


			if yDestination > 0: # up
				self.y -= Survivor.velocity

			elif yDestination < 0: # dopwn
				self.y += Survivor.velocity

			if xDestination == 0 and yDestination == 0:
				self.dx, self.dy = 0, 0


	def draw(self, screen):

		screen.blit(self.img, (self.x, self.y))

		h = self.width / 2
		img = Survivor.guns_img[self.current]

		if self.direction == Direction.WEST:
		    screen.blit(img, (self.x, self.y + h))

		elif self.direction == Direction.EAST:
		    img = pygame.transform.flip(img, True, False)
		    screen.blit(img, (self.x + h, self.y + h))            

		elif self.direction == Direction.SOUTH:
		    img = pygame.transform.rotate(img, 90) # CCW
		    screen.blit(img, (self.x + h, self.y + h))            

		elif self.direction == Direction.NORTH:
		    south = pygame.transform.rotate(img, 90)
		    img = pygame.transform.flip(south, False, True)
		    screen.blit(img, (self.x + h, self.y - h))

	"""
	changes player direction
	"""

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




