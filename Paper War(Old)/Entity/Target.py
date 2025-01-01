# coding:utf-8
import pygame
from pygame.sprite import Sprite
import time
import math

from Setting import *

class Target(Sprite):
    def __init__(self,screen,x,y,world,entity_id,name):
        self.group=world.entity_group
        super().__init__(self,self.group)
        
        self.HP=15
        self.screen=screen
        self.entity_id=entity_id
        self.name=name
       
        
        self.image=pygame.image.load("image//Target.bmp").convert_alpha()
        self.rect=self.image.get_rect()
        
        self.rect.x=x*RECT_WHIGT
        self.rect.y=y*RECT_HIGHT

        self.world=world

#自我渲染
    def update(self):

        if self.HP<=0:
            print (self.name,"死了")
            self.world.remove(self)
        else:
            self.screen.blit(self.image,self.rect)
            

