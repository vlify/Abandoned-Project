# coding:utf-8
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite
import math

from Setting import *
import tool

font = pygame.font.Font("Font/微软雅黑Bbold.ttf", 17)


class GameObject(Sprite):
	"""兵种基类"""

	def __init__(self, screen, map, x, y, name, world, entity_id):
		self.group = world.entity_group
		pygame.sprite.Sprite.__init__(self, self.group)

		# 实体基本数据
		self.HP = 0
		self.max_HP = 0
		self.name = name
		self.screen = screen
		self.map = map
		self.screen_rect = self.screen.get_rect()
		self.world = world
		self.entity_id = entity_id
		self.camp = 1
		self.price = 0

		# 图像数据
		self.flie_name1 = "image//Player1.bmp"
		self.flie_name2 = "image//Player2.bmp"
		self.image = pygame.image.load(self.flie_name1).convert()
		self.rect = self.image.get_rect()
		self.crect = self.image.get_rect()

		# 位置数据
		self.screen_x = x * RECT_WHIGT
		self.screen_y = y * RECT_WHIGT
		self.map_x = x
		self.map_y = y

		# 玩家相对位置
		self.rect.x = x * RECT_WHIGT
		self.rect.y = y * RECT_WHIGT
		self.target_x = None
		self.target_y = None

		self.is_click = 1

		# 移动速度
		self.speed = 60
		self.move_num = 0
		self.moving = False

		# 攻击范围
		self.attack_block_list = None

		tool.playsound("Entity_setup", volume=1.8)

	def can_click(self):
		if self.is_click > 0:
			return True
		else:
			return False

	def set_camp(self, camp):
		self.camp = camp

	def get_camp(self):
		return self.get_camp

	def get_move_num(self):
		return self.move_num

	def set_move_num(self, num):
		self.move_num = num

	def minus_move_num(self):
		self.move_num -= 1

	def can_move(self):
		if self.move_num > 0:
			return True
		else:
			return False

	def update(self):
		# 总更新
		if self.HP > 0:
			self.image_change()
			self.__mouse_down()
			self.font_print()
			self.attack()
			self.__move()
			self.map().blit(self.image, self.map.apply(self))
		else:
			self.world.entity_group.remove(self)
			tool.send_messge(self.screen, self.name + "死了", (0, SCREEN_HIGHT - 100), RED)
			if self.camp == -1:
				self.world.money += self.price

	def __move(self):
		if not self.can_move():
			return

		if self.target_y is None or self.is_click < 0:
			return

		dx = self.target_x - self.map_x
		dy = self.target_y - self.map_y
		distance = math.sqrt(dx ** 2 + dy ** 2)

		if distance > 0:
			nx = dx / distance
			ny = dy / distance
			move_x = nx * self.speed
			move_y = ny * self.speed

			if abs(dx) < abs(move_x):
				self.map_x = self.target_x
			else:
				self.map_x += int(move_x)

			if abs(dy) < abs(move_y):
				self.map_y = self.target_y
			else:
				self.map_y += int(move_y)

		if self.map_x == self.target_x and self.map_y == self.target_y:
			self.target_x = None
			self.target_y = None
			self.is_click *= -1
			self.minus_move_num()

	def __mouse_down(self):
		# 鼠标点击处理
		pos = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if self.can_click() is False:
			self.target_x = None
			self.target_y = None

		# 如果是鼠标右键摁下(选定玩家)
		if click[2] and self.crect.collidepoint(pos):
			pygame.event.wait()
			self.is_click *= -1

		# 鼠标左键摁下(选定目标)
		if click[0] and self.can_click() and self.can_move():
			if self.target_x is None and self.is_click > 0:
				# 目标坐标转化
				self.target_x = pos[0] // RECT_WHIGT
				self.target_y = pos[1] // RECT_HIGHT
				tool.playsound(self.name + "_move")
				'''

				if self.target_x*RECT_WHIGT>SCREEN_WHIGT or self.target_y*RECT_WHIGT>SCREEN_HIGHT :
					self.target_x =None
					self.target_y =None
					'''

	def image_change(self):
		# 实体图像转换
		self.rect.x = -self.map.rect.x + self.screen_x
		self.rect.y = -self.map.rect.y + self.screen_y

		# print(self.rect.x,self.rect.y)
		self.crect.x = self.map.rect.x + self.screen_x
		self.crect.y = self.map.rect.y + self.screen_y

		if self.can_click():
			self.image = pygame.image.load(self.flie_name2)
			if self.camp == -1:
				new_image = pygame.transform.rotate(self.image, 180)
				self.image = new_image
		else:
			self.image = pygame.image.load(self.flie_name1)
			if self.camp == -1:
				new_image = pygame.transform.rotate(self.image, 180)
				self.image = new_image

		if not self.can_move():
			self.image.set_alpha(150)
		else:
			self.image.set_alpha(255)

	def font_print(self):
		# 实体信息输出
		if self.can_click():
			self.screen.blit(pygame.image.load(self.flie_name1), (SCREEN_WHIGT - 80, 20))
			if self.camp < 0:
				tool.send_messge(self.screen, "敌人", (SCREEN_WHIGT - 100, 120), RED)

			tool.send_messge(self.screen, "生命值:" + str(self.HP) + "/" + str(self.max_HP), (SCREEN_WHIGT - 100, 150),
							 BLACK)
			tool.send_messge(self.screen, "攻击力:5", (SCREEN_WHIGT - 100, 180), BLACK)

		if self.HP > 0:
			line = pygame.draw.line(self.image, (255, 0, 0), (0, 60), (60, 60), 8)
			line.center = self.rect.center
			b = float(self.HP) / self.max_HP
			line = pygame.draw.line(self.image, (0, 255, 0), (0, 60), (60 * b, 60), 8)
			line.center = self.rect.center

	def attack(self):
		# 攻击函数
		pass

	def be_attacked(self, damage):
		# 被攻击函数
		pass
