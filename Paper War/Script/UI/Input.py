# coding:utf-8
import pygame as pg
from pygame.locals import *

from Setting import *

pg.font.init()
font = pg.font.Font("Font/微软雅黑Bbold.ttf", 32)


class Input(object):
	def __init__(self, screen, x, y, callback, wide=150, high=40):
		self.screen = screen
		self.wide = wide
		self.high = high
		self.rect = pg.Rect(x, y, wide, high)
		self.text = ""
		self.font = pg.font.Font("Font/微软雅黑Bbold.ttf", 32)
		self.color = WHITE
		self.callback = callback
		if callback is None:
			raise RuntimeError("InputBox callback func is None")
		self.active = False
		self.inactive_color = BLACK
		self.active_color = DEEP_BLUE

	def draw(self):
		# 绘制背景
		pg.draw.rect(self.screen, self.inactive_color, self.rect)
		# 绘制文本
		text_surf = self.font.render(self.text, True, self.color)
		text_rect = text_surf.get_rect()
		text_rect.center = self.rect.center
		self.screen.blit(text_surf, text_rect)

	def update(self):
		self.draw()

	def get_event(self, event):
		if event.type == pg.MOUSEBUTTONDOWN:
			# 如果用户单击了输入框，则激活它
			if self.rect.collidepoint(event.pos):
				self.active = True
			else:
				self.active = False
			# 将输入框颜色更改为激活状态
			self.color = self.active_color if self.active else WHITE
		elif event.type == pg.KEYDOWN and self.active:
			# 如果用户按下回车键，则调用回调函数
			if event.key == K_RETURN and self.callback:
				self.callback(self.text)
			# 如果用户按下退格键，则删除最后一个字符
			elif event.key == K_BACKSPACE:
				self.text = self.text[:-1]
			# 如果用户输入的是可显示字符，则添加到文本末尾
			elif event.unicode and self.active:
				self.text += event.unicode
