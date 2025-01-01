# -*- coding: utf-8 -*-
import pygame

BLUE = 0, 0, 255
DEEP_BLUE = 0, 0, 180
HIGH_BLUE = 0, 0, 205
WHITE = 255, 255, 255

pygame.font.init()
font = pygame.font.Font(None, 17)


class Button:
	def __init__(self, screen: pygame.surface, text: str, x: int, y: int, wide=200, high=50,
				color=DEEP_BLUE, coll_color=BLUE, click_color=HIGH_BLUE,
				text_color=WHITE):
		self.screen = screen
		self.wide = wide
		self.high = high
		self.text = str(text)
		self.x = x
		self.y = y
		self.color = color
		self.n_color = color
		self.coll_color = coll_color
		self.click_color = click_color
		self.text_color = text_color
		self.event = None 
		if self.event is None:
			raise "Button event is None"
		self.can_click = True

		self.Brect = pygame.Rect(self.x, self.y, self.wide, self.high)
		self.text_image = None
		self.text_image_rect = None
		self.prep_text(self.text)

	def prep_text(self, text):
		self.text_image = font.render(text, True, self.text_color, self.color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.Brect.center

	def draw_button(self):
		self.screen.fill(self.color, self.Brect)
		self.screen.blit(self.text_image, self.text_image_rect)

	def change_color(self, pos):
		if self.Brect.collidepoint(pos):
			self.color = self.coll_color
		else:
			self.color = self.n_color

	def set_event(self, func):
		self.event = func

	def update(self, pos):
		if self.Brect.collidepoint(pos) and self.can_click:
			self.color = self.click_color
			pygame.event.get()
			if self.event is not None:
				self.event()
