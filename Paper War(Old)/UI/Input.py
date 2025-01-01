# coding:utf-8
import pygame as pg
from pygame.locals import *

from Setting import *

pg.font.init()
font=pg.font.Font("Font/微软雅黑Bbold.ttf",32)


class Input(object):
    def __init__(self,screen,x,y,wide=150,high=40,callback=None):
        self.screen=screen
        self.sur=pg.Surface((wide,high))
        self.wide=wide
        self.high=high
        self.sur.fill(BLACK)
        self.text=" "
        self.rect=self.sur.get_rect()
        self.rect.center=(x,y)

    def update(self):
        text_surf = font.render(self.text, True, (255, 255, 255))
        self.screen.blit(self.sur, self.rect)
        self.screen.blit(text_surf, (self.rect.x, self.rect.y+(self.high - text_surf.get_height())),
                       (0, 0, self.wide, self.high))
    def get_event(self,event):
        unicode = event.unicode
        key = event.key
        # 退位键
        if key == K_BACKSPACE:
            self.text = self.text[:-1]
            return
        
        if key == K_TAB:
            return
            
        # 切换大小写键
        if key == K_CAPSLOCK or key== K_LSHIFT or key == K_RSHIFT:
            return
 
        # 回车键
        if key == K_KP_ENTER or key == K_RETURN:
            return self.get_text()
 
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
 
        self.text += char

    def get_text(self):
        text=self.text
        return text






