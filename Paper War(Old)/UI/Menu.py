# coding:utf-8
import pygame as pg

from UI.Button import Button

pg.font.init()
font = pg.font.Font("Font/微软雅黑Bbold.ttf", 10)

"""菜单栏"""


class Menu(object):
	BUTTON_WIDTH = 85

	def __init__(self, screen, hight=40):
		self.screen = screen
		self.width = self.screen.get_width()
		self.hight = hight
		self.msur = pg.Surface((self.width, self.hight))
		self.msur.fill((255, 255, 255))
		self.rect = self.msur.get_rect()
		self.rect.topleft = (0, 0)
		self.dmlist = []
		self.Blist = []
		self.now_button = None

	def get_event(self, pos):
		self.pos = pos
		for dm in self.dmlist:
			dm.get_event(pos)
		for b in self.Blist:
			b.update(pos)

	def button_chage_color(self, pos):
		for b in self.Blist:
			b.chage_color(pos)
		for dm in self.dmlist:
			dm.button_chage_color(pos)

	def updata(self):
		self.screen.blit(self.msur, self.rect)
		for b in self.Blist:
			b.draw_button()
		for dm in self.dmlist:
			dm.draw()

	def add_cascade(self, label, command):
		if self.Blist:
			x = self.Blist[-1].x + self.Blist[-1].wide
		else:
			x = 0
		button = Button(self.msur, label, x, 0, Menu.BUTTON_WIDTH, self.hight)

		if isinstance(command, DropMenu):
			button.set_elist(command.call)
			command.init(button)
			self.dmlist.append(command)
		else:
			button.set_elist(command)
		self.Blist.append(button)


'''下拉菜单'''


class DropMenu(object):
	def __init__(self, screen):
		self.screen = screen
		self.dmsur = pg.Surface((200, 0))
		self.width = self.dmsur.get_width()
		self.hight = self.dmsur.get_height()
		self.rect = self.dmsur.get_rect()
		self.Bdict = {}
		self.Blist = []
		self.cried = False

	def call(self):
		if not self.cried:
			self.cried = True
		else:
			self.cried = False

	def draw(self):
		if self.cried:
			self.screen.blit(self.dmsur, self.rect)
			self.button_updata()

	def button_chage_color(self, pos):
		for b in self.Blist:
			b.chage_color((pos[0] - self.rect.x, pos[1] - self.rect.y))

	def add_command(self, label, command=None):
		self.Bdict[label] = command

	def init(self, b):
		self.dmsur = pg.Surface((200, len(self.Bdict.keys()) * 40))
		self.rect = self.dmsur.get_rect()
		self.rect.x = b.x
		self.rect.y = b.high
		for text, fuc in self.Bdict.items():
			if self.Blist:
				x = self.Blist[-1].x
				y = self.Blist[-1].y + self.Blist[-1].high
			else:
				x = 0
				y = 0
			button = Button(self.dmsur, text, x, y, self.width, 40)
			button.set_elist(fuc)
			self.Blist.append(button)

	def button_updata(self):
		for b in self.Blist:
			b.draw_button()

	def get_event(self, pos):
		if self.cried and self.rect.collidepoint(pos):
			for b in self.Blist:
				b.update((pos[0] - self.rect.x, pos[1] - self.rect.y))
