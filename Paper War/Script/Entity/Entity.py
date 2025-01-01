import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Entity(Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = None
		self.rect = None

	def update(self):
		pass
