
import pygame

__author__ = 'William Fiset'

class Weapon():

	SHOTGUN = 'shotgun'
	AUTOMATIC = 'automatic'
	PISTOL = 'pistol'

	weapon_bullet_velocites = {
		SHOTGUN : 7,
		AUTOMATIC : 13,
		PISTOL : 10
	}

	WEAPON_IMAGES = { 
		PISTOL : pygame.image.load('images/weapon/pistol.png'),
		SHOTGUN : pygame.image.load('images/weapon/shotgun.png'),
		AUTOMATIC : pygame.image.load('images/weapon/automatic.png')
	}

	def __init__(self, weapon_type):

		if weapon_type not in (Weapon.SHOTGUN, Weapon.PISTOL, Weapon.AUTOMATIC):
			raise ValueError("Not a valid weapon, see the weapon class for available weapons")

		self.weapon_type = weapon_type
		self.bullet_velocity = Weapon.weapon_bullet_velocites[weapon_type]

	def get_weapon_image(self):
		return Weapon.WEAPON_IMAGES[ self.weapon_type ]
    



