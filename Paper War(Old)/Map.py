# coding:utf-8
import pygame as pg
from pygame.sprite import Sprite

from Setting import *


class Land(Sprite):
	def __init__(self, map_surface, land_id, x, y, color, *groups: AbstractGroup):
		super().__init__(*groups)
		self.image = pg.Surface((RECT_WIDTH, RECT_HEIGHT))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = (x - 1) * RECT_WIDTH
		self.rect.y = (y - 1) * RECT_HEIGHT
		self.map_surface = map_surface
		self.map_surface.blit(self.image, self.rect)

	def draw(self):
		self.map_surface.blit(self.image, self.rect)


class Map:
	def __init__(self, screen, filename):
		self.screen = screen
		self.width = SCREEN_WIDTH
		self.height = SCREEN_HEIGHT
		self.data = []
		self.map_surface = pg.Surface((self.width, self.height))
		self.rect = self.map_surface.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.map_surface.fill((255, 255, 255))
		self.moving_directions = [False, False, False, False]
		self.move_speed = 1
		self.tile_colors = {
			OCEAN_ID: (127, 255, 212),
			FATLAND_ID: (124, 252, 0),
			MOUNTAIN_ID: (115, 74, 18)
		}

		with open(filename, 'rt') as f:
			for line in f:
				self.data.append(line.strip("\n"))

	def new(self):
		self.land_objects = [
			Land(self.map_surface, tile, c, r, self.tile_colors[tile])
			for r, tiles in enumerate(self.data, 1)
			for c, tile in enumerate(tiles, 1)
		]

	def move(self):
		if self.moving_directions[0] and self.rect.x > -SCREEN_WIDTH // 3:
			self.rect.x -= self.move_speed
		if self.moving_directions[1] and self.rect.x < SCREEN_WIDTH // 3:
			self.rect.x += self.move_speed
		if self.moving_directions[2] and self.rect.y < SCREEN_HEIGHT // 3:
			self.rect.y += self.move_speed
		if self.moving_directions[3] and self.rect.y > -SCREEN_HEIGHT // 3:
			self.rect.y -= self.move_speed

	def map_update(self):
		self.move()
		self.screen.blit(self.map_surface, self.rect)

	def __getindex__(self, x, y):
		return self.data[x][y]

	def __call__(self):
		return self.map_surface

	def get_rect_d(self):
		return self.rect.x, self.rect.y

	def apply(self, entity):
		return entity.rect.move(self.rect.topleft)

	def tapply(self, entity):
		return entity.move(self.rect.topleft)
