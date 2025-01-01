# coding:utf-8
import pygame as pg
from pygame.locals import *

from Setting import *
from UI.Button import Button
from UI.Input import Input

pg.font.init()
font = pg.font.Font("Font/微软雅黑Bbold.ttf", 20)


class MessageBox:
	def __init__(self, screen, x, y, mtype=None, text=" ", wide=200, high=50, callback=None, input_w=150, input_h=40):
		self.screen = screen
		self.high = high
		self.wide = wide
		self.color = BLUE
		self.text_color = 255, 255, 255
		self.sur = pg.Surface((wide, high))
		self.sur.fill(self.color)
		self.rect = self.sur.get_rect()
		self.rect.center = (x, y)
		self.Blist = []  # 按钮列表
		self.control = None
		self.callback = callback
		self.control_init(mtype, text, input_w, input_h)
		self.call = True

	def control_init(self, mtype, text, input_w, input_h):
		self.prep_text(text)
		b_size = 30
		b = Button(self.sur, "X", self.wide - b_size, 0, b_size, b_size, RED, DEEP_RED, HIGH_RED, text_color=BLACK)
		b.set_elist(self.quit)
		if mtype == "TextBox":
			b = Button(self.sur, "确定", self.wide // 3, self.high * 2 // 3, 75, 40, (215, 215, 215), GRAY,
					   text_color=BLACK)
			b.Brect.center = (self.wide // 2, self.high * 3 // 4)
			b.text_image_rect.center = b.Brect.center
			b.set_elist(self.quit)
			self.Blist.append(b)
		if mtype == "InputBox":
			self.Blist.append(b)
			i = Input(self.sur, self.wide // 2, self.high // 2, callback=self.callback, wide=input_w, high=input_h)
			self.control = i

	def update(self):
		if self.call:
			self.screen.blit(self.sur, self.rect)
			self.sur.blit(self.text_image, self.text_image_rect)
			if self.control:
				self.control.update()
			for b in self.Blist:
				b.draw_button()

	def input_get_event(self, event):
		if self.control:
			t = self.control.get_event(event)
			if t != None:
				return t

	def button_get_event(self, pos):
		for b in self.Blist:
			b.update((pos[0] - self.rect.x, pos[1] - self.rect.y))

	def move(self, event, pos, rel):
		if self.call:
			self.rect_pos_chage()
			if event.buttons[0] and self.collide_rect(pos) and self.rect.x >= 0 and self.in_screen():
				self.rect.x += rel[0]
				self.rect.y += rel[1]

	def button_chage_color(self, pos):
		for b in self.Blist:
			b.chage_color((pos[0] - self.rect.x, pos[1] - self.rect.y))

	def quit(self):
		self.call = False
		del self

	def collide_rect(self, pos):
		if self.rect.collidepoint(pos):
			return True
		else:
			return False

	def in_screen(self):
		if self.rect.x >= 0 and self.rect.x <= self.screen.get_width() - self.wide \
				and self.rect.y >= 0 and self.rect.y <= self.screen.get_height() - self.high:
			return True
		else:
			return False

	def rect_pos_chage(self):
		if self.rect.x < 0:
			self.rect.x = 0
		if self.rect.x > self.screen.get_width() - self.wide:
			self.rect.x = self.screen.get_width() - self.wide
		if self.rect.y < 0:
			self.rect.y = 0
		if self.rect.y > self.screen.get_height() - self.high:
			self.rect.y = self.screen.get_height() - self.high

	def prep_text(self, text):
		self.text_image = font.render(text, True, self.text_color, self.color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = (self.wide // 2, self.high // 3)
