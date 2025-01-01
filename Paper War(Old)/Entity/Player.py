# -*- coding: utf-8 -*-
import pygame as pg
from pygame.sprite import Sprite
import threading

from Setting import*

class Player(Sprite):
    def __init__(self,screen,world,x,y):
        self.group=world.entity_group
        Sprite.__init__(self,self.group)

        self.name="player"

        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.image=pg.Surface((50,50))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.color=(0,0,0)
        
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        self.kt=threading.Thread(target=self.keydowm)
        self.kt.start()
        pg.draw.rect(self.screen,self.color,self.rect)

    def keydowm(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.centerx-=1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery-=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
             self.centery+=1
        # 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
