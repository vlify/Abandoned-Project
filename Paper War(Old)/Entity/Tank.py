# coding:utf-8
import pygame

from Game_object import GameObject
from Setting import *
import tool


class Tank(GameObject):
	def __init__(self, screen, map, x, y, name, world, entity_id, camp=1):
		super(Tank, self).__init__(screen, map, x, y, name, world, entity_id)
		self.HP = 20
		self.max_HP = 20

		self.flie_name1 = 'image//Tank1.bmp'
		self.flie_name2 = "image//Tank2.bmp"

		self.image = pygame.image.load(self.flie_name1).convert()
		self.rect = self.image.get_rect()
		if camp == -1:
			new_image = pygame.transform.rotate(self.image, 180)
			self.image = new_image
			self.rect = self.image.get_rect()

		self.camp = camp
		self.price = 100
		self.move_num = 3

		# 设置玩家相对位置
		self.rect.x = x * RECT_WHIGT
		self.rect.y = y * RECT_HIGHT

	def attack(self):
		# 实时更新攻击范围
		self.attack_block_list = {(self.rect.x, self.rect.y - 60),
								  (self.rect.x, self.rect.y - 120),
								  (self.rect.x + 60, self.rect.y),
								  (self.rect.x - 60, self.rect.y),
								  (self.rect.x, self.rect.y + 60)}
		click = pygame.mouse.get_pressed()
		pos = pygame.mouse.get_pos()

		target_list = self.world.entity_group
		for target in target_list:
			# 如果目标在攻击范围内
			if target.name != "Base" and "barrack" not in target.name:
				if (target.rect.x, target.rect.y) in self.attack_block_list:
					if click[0] and target.rect.collidepoint(pos) and self.is_click > 0:
						if target.name == "Base" or "barrack" in target.name or target.camp == self.camp:
							print(("不是一个有效单位"))
							self.target_x = None
							self.target_y = None
							self.is_click *= -1
							return
						self.target_x = None
						self.target_y = None
						self.is_click *= -1
						target.HP -= 5
						tool.playsound(self.name + "_attack")
						if target.HP < 0:
							self.world.money += target.price
