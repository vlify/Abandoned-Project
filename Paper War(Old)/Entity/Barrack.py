# coding:utf-8
import pygame as pg
import math
import tool

from pygame.sprite import Sprite

from Entity.Tank import Tank
from Entity.Medic import Medic
from UI.Button import Button


from Setting import *

font=pg.font.Font("Font/微软雅黑Bbold.ttf",20)


class Barrack(Sprite):
    '''兵营类'''
    def __init__(self,screen,map,world,name,x,y,camp=1):
        self.group=world.entity_group
        pg.sprite.Sprite.__init__(self,self.group)
        #基础信息
        self.screen=screen
        self.map=map
        self.world=world
        self.name=name
        self.camp=camp

        #图像信息
        self.image=pg.image.load("image//Barrack1.bmp").convert()
        if self.camp==-1:
            self.image=pg.transform.rotate(pg.image.load("image//Barrack1.bmp"),180).convert()
        self.rect=self.image.get_rect()
        self.crect=self.image.get_rect()

        #位置信息
        self.screen_x=x*RECT_WHIGT
        self.screen_y=y*RECT_HIGHT
        self.map_x=x
        self.map_y=y
        self.rect.x=self.screen_x
        self.rect.y=self.screen_y

        #实体信息
        self.pos=tuple()
        self.click=list()
        self.is_click=-1
        self.state=-1

        
    def get_camp(self):
        return self.camp
    
    def set_camp(self,camp):
        self.camp=camp

    def update(self):
    #总更新
        self.font_print()
        self.mouse_down()
        self.chage_image()
        self.generate_entity()
        self.map().blit(self.image,self.map.apply(self))

    def mouse_down(self):
    #鼠标选中
        pos=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        #如果是鼠标右键摁下(选定玩家)
        if click[2]:
            if self.crect.collidepoint(pos):
                        pg.event.wait()
                        self.is_click*=-1

    def generate_entity(self):
    #生成实体
        screen_pos = pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        map_pos=((screen_pos[0]-self.map.rect.x)//RECT_WHIGT,(screen_pos[1]-self.map.rect.y)//RECT_WHIGT)
        distance= tool.get_distance(map_pos,[self.map_x,self.map_y])
        
        #print(map_pos[0],map_pos[1])
        if click[0] and distance==1 and self.is_click>0:
            if self.world.money-100<0:
                print ("你没钱了，弟弟")
                self.is_click*=-1
                return  
            self.is_click*=-1
            
            if self.state==0:
                tank=Tank(self.screen,self.map,map_pos[0],map_pos[1],"tank",self.world,self.world.num)
                if self.camp == -1:
                    tank.set_camp(-1)
                #self.world.money-=tank.price
                self.world.entity_group.add(tank)
            if self.state==1:
                medic=Medic(self.screen,self.map,map_pos[0],map_pos[1],"medic",self.world,self.world.num)
                if self.camp == -1:
                    medic.set_camp(-1)
                #self.world.money-=medic.price
                self.world.entity_group.add(medic) 
            self.state=-1
            

    def chage_image(self):
    #选中实体图像更改
        self.rect.x=-self.map.rect.x +self.screen_x
        self.rect.y=-self.map.rect.y +self.screen_y
        self.crect.x=self.map.rect.x +self.screen_x
        self.crect.y=self.map.rect.y +self.screen_y
        
        if self.is_click>0:
            self.image=pg.image.load("image//Barrack2.bmp").convert()
            if self.camp ==-1:
                new_image=pg.transform.rotate(self.image,180)
                self.image=new_image

        else:
            self.image=pg.image.load("image//Barrack1.bmp").convert()
            if self.camp ==-1:
                new_image=pg.transform.rotate(self.image,180)
                self.image=new_image
                
    def font_print(self):
    #打印实体基本信息
        pos=pg.mouse.get_pos()
        click=pg.mouse.get_pressed()
        if self.is_click>0:
            self.screen.blit(pg.image.load("image//Barrack1.bmp").convert_alpha(),(SCREEN_WHIGT-80,20))
            if self.camp==-1:
                tool.send_messge(self.screen,"敌人",(SCREEN_WHIGT-100,120),RED)
                
            tool.send_messge(self.screen,self.name,(SCREEN_WHIGT-100,150),BLACK)
                
            b1=Button(self.screen,"坦克",SCREEN_WHIGT-100,180,high=25,wide=90)
            b1.draw_button()
            if click[0] and b1.Brect.collidepoint(pos):
                self.state=0
                
            b2=Button(self.screen,"医疗兵",SCREEN_WHIGT-100,210,high=25,wide=90)
            b2.draw_button()
            if click[0] and b2.Brect.collidepoint(pos):
                self.state=1
