# coding:utf-8
import math
import pygame as pg

from Setting import *

pg.init()
font = pg.font.Font("Data/Font/微软雅黑Bbold.ttf", 17)


def get_distance(start_point, end_point):
	dx = (max(start_point[0], end_point[0]) - min(start_point[0], end_point[0])) ** 2
	dy = (max(start_point[1], end_point[1]) - min(start_point[1], end_point[1])) ** 2
	return int(math.sqrt(dx + dy))


def playmusic(file, volume=.4, loop=-1):
	file = MusicPath + file
	pg.mixer.music.load(file)
	pg.mixer.music.play(loop, 0)
	pg.mixer.music.set_volume(volume)


def playsound(file, loop=0, volume=1):
	pg.mixer.init()
	filePath = SoundPath + file + ".wav"
	sound = pg.mixer.Sound(filePath)
	sound.set_volume(volume)
	s = sound.play(loop)
	return s.get_busy()


def send_messge(sur, text, pos, color=BLACK):
	font_image = font.render(text, True, color)
	sur.blit(font_image, pos)
