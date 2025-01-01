# coding:utf-8
import pygame
import math

from Entity.Game_object import Game_object
from pygame.sprite import Sprite

from Setting import *
import tool

class Medic(Game_object):
    def __init__(self,screen,map,x,y,name,world,entity_id,camp=1):
        super(Medic,self).__init__(screen,map,x,y,name,world,entity_id)
        self.HP=15
        self.max_HP=15

        self.flie_name1="image//Medic1.bmp"
        self.flie_name2="image//Medic2.bmp"
        
        self.image=pygame.image.load(self.flie_name1).convert()
        self.rect=self.image.get_rect()

        self.camp=camp
        self.price=150
        
        self.rect.x=x*RECT_WHIGT
        self.rect.y=y*RECT_HIGHT

        self.move_num=2

        self.attack_block_list=None
        
    def attack(self):#实时更新攻击范围
        self.attack_block_list={(self.rect.x,self.rect.y-60),
                                (self.rect.x,self.rect.y-120),
                                (self.rect.x+60,self.rect.y),
                                (self.rect.x-60,self.rect.y),
                                (self.rect.x,self.rect.y+60)}
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        
        target_list=self.world.entity_group
        for target in target_list:
            #如果距离为一(就是在附近)
            if (target.rect.x,target.rect.y) in self.attack_block_list:
                if click[0]and target.rect.collidepoint(pos)and self.is_click>0:
                    if target.camp==self.camp:
                        if target.HP+5>target.max_HP:
                            self.target_x =None
                            self.target_y =None
                            self.is_click*=-1
                            return
                        if target.name=="Base" or "barrack" in target.name or target.camp!=self.camp:
                            print("不是一个有效的目标")
                            self.target_x =None
                            self.target_y =None
                            self.is_click*=-1
                            return
                        tool.playsound(self.name+"_attack")
                        target.HP+=5
                        self.target_x =None
                        self.target_y =None
                        self.is_click*=-1
