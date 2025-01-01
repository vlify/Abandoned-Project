# coding:utf-8
import pygame as pg
from pygame.sprite import Sprite, Group
from pygame.locals import *

from Entity.Base import Base
from Entity.Barrack import Barrack
from Map import Map

import tool
from Setting import *

font = pg.font.Font("Font/微软雅黑Bbold.ttf", 30)


class World:
	"""控制整个游戏世界"""

	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((SCREEN_WHIGT, SCREEN_HIGHT))
		pg.display.set_caption("Map")

		# 实体队列
		self.entity_group = Group()

		# 设置地形
		self.maps = Map(self.screen, 'MapDate/map1.txt')
		self.maps.new()

		self.num = 0
		self.money = 500

	def game_object_init(self):
		# 游戏实体初始化
		barrack = Barrack(self.screen, self.maps, self, "barrack2", 7, 2)
		barrack.set_camp(-1)

	def get_entity(self, who=None, name=None):
		# 检查附近的实体
		if name is None:
			entity = pg.sprite.spritecollideany(who, self.entity_group, collided=collide_rect)
			if entity:
				return entity
		for entity in self.entity_group:
			if entity.name == name:
				distance = tool.get_distance([who.x, who.y], [entity.rect.x, entity.y])
				if distance == 1:
					return entity
		return None

	@staticmethod
	def collide_rect(sprite, other):
		return sprite.rect.colliderect(other.rect)

	def get_event(self):
		# 事件获取
		for event in pg.event.get():
			if event.type == QUIT:
				pg.quit()
				exit()
			if event.type == pg.KEYDOWN:
				self._key_down_event(event)
			elif event.type == pg.KEYUP:
				self._key_up_event(event)

	def _key_down_event(self, event):
		# 键盘落下触发事件
		if event.key == pg.K_RIGHT or event.key == pg.K_d:
			self.maps.moving_right = True
		elif event.key == pg.K_LEFT or event.key == pg.K_a:
			self.maps.moving_left = True
		elif event.key == pg.K_UP or event.key == pg.K_w:
			self.maps.moving_up = True
		elif event.key == pg.K_DOWN or event.key == pg.K_s:
			self.maps.moving_down = True

	def _key_up_event(self, event):
		# 键盘起触发事件
		if event.key == pg.K_RIGHT or event.key == pg.K_d:
			self.maps.moving_right = False
		elif event.key == pg.K_LEFT or event.key == pg.K_a:
			self.maps.moving_left = False
		elif event.key == pg.K_UP or event.key == pg.K_w:
			self.maps.moving_up = False
		elif event.key == pg.K_DOWN or event.key == pg.K_s:
			self.maps.moving_down = False

	def render(self):
		self.screen.fill((230, 230, 230))
		self.maps.map_update()
		self.entity_group.update()
		font_image = font.render(str(self.money) + "$", True, (0, 0, 0))
		self.screen.blit(font_image, (600, 0))
		pg.draw.line(self.screen, (0, 0, 0), (SCREEN_WHIGT - 100, 100), (SCREEN_WHIGT, 100), 5)
		pg.display.update()

	def run_game(self):
		# 世界更新
		self.game_object_init()
		while True:
			self.get_event()
			self.render()
			pg.display.update()


if __name__ == "__main__":
	w = World()
	w.run_game()
