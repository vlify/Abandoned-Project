# coding:utf-8
import pygame as pg
from pygame.locals import *

from UI.MessageBox import MessageBox

pg.init()
'''鍒涘缓灞忓箷'''
screen=pg.display.set_mode((700,600))
pg.display.set_caption("测试")

pg.key.set_repeat(400,50)
Mb=MessageBox(screen,200,200,"InputBox"," ",250,150)
while True:
    for event in pg.event.get():
        if event.type== QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEMOTION:
            pos=pg.mouse.get_pos()
            rel=pg.mouse.get_rel()
            Mb.move(event,pos,rel)
            Mb.button_chage_color(pos)
            
        if event.type == MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            
            Mb.button_get_event(pos)
        if event.type == KEYDOWN:
            Mb.input_get_event(event)        
                
    screen.fill((230,230,230))
    Mb.update()
    pg.display.update()
                

