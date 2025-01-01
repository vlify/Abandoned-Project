# coding:utf-8
import pygame
import math
import time

from pygame.sprite import Sprite

from Setting import *

'''基地类'''


class Base(Sprite):
	def __init__(self, screen, world, camp=1):
		self.group = world.entity_group
		pygame.sprite.Sprite.__init__(self, self.group)

		self.screen = screen
		self.gameover = False
		self.win = False
		self.image = pygame.image.load("image//Base.bmp").convert()
		self.rect = self.image.get_rect()
		self.world = world
		self.name = "Base"
		self.camp = camp

		self.rect.x = 240
		self.rect.y = 540

		if self.camp == -1:
			self.rect.x = 240
			self.rect.y = 0
			new_image = pygame.transform.rotate(self.image, 180)
			self.image = new_image

	def update(self):
		self.is_over_or_not()
		if self.gameover:
			print("You lose")
			print("Game Over!")
			pygame.quit()
			time.sleep(3)
			exit()
		elif self.win:
			print("You Win!")
			print("Game over!")
			pygame.quit()
			time.sleep(3)
			exit()
		else:
			self.screen.blit(self.image, self.rect)

	def is_over_or_not(self):
		entity = self.world.get_entity(who=self)
		if entity != None:
			if self.camp > 0:
				if entity.camp == self.camp:
					pass
				else:
					self.gameover = True
			elif self.camp < 0:
				if entity.camp == self.camp:
					pass
				else:
					self.win = True

	def get_mouse_state(pos, click):
		pass
