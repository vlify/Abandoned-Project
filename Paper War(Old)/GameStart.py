# coding:utf-8
import pygame
from pygame.locals import *

from UI.Button import Button

pygame.init()
'''鍒涘缓灞忓箷'''
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Paper War")
font = pygame.font.Font("Font/微软雅黑Bbold.ttf", 115)
font_image = font.render("纸上战争", True, (0, 0, 0))

b1 = Button(screen, "开始游戏", 250, 300)
b2 = Button(screen, "退出", 250, 400)

while True:
	click = pygame.mouse.get_pressed()
	pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	screen.fill((230, 230, 230))
	b1.draw_button()
	if click[0] and b1.Brect.collidepoint(pos):
		screen.fill((0, 0, 0))
	b2.draw_button()
	if click[0] and b2.Brect.collidepoint(pos):
		pygame.quit()
		exit()
	screen.blit(font_image, (150, 100))
	pygame.display.update()
