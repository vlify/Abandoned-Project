# -*- coding: utf-8 -*-
import pygame

BLUE=0,0,255
DEEP_BLUE=0,0,180
HIGH_BLUE=0,0,205
WHITE=255,255,255

pygame.font.init()
font=pygame.font.Font("Font/微软雅黑Bbold.ttf",17)

class Button(object):
    def __init__(self,screen,text,x,y,wide=200,high=50,\
                 color=DEEP_BLUE,coll_color=BLUE,click_color=HIGH_BLUE,\
                 text_color=WHITE):
        super(Button,self).__init__()
        #屏幕
        self.screen=screen
        #按钮的宽与高
        self.high=high
        self.wide=wide
        #按钮显示的内容
        self.text=str(text)
        #按钮的位置
        self.x=x
        self.y=y
        #按钮颜色
        self.color=color
        self.n_color=color
        self.coll_color=coll_color
        self.click_color=click_color
        self.text_color=text_color
        #按钮所要执行的事件
        self.event=None
        self.Brect=pygame.Rect(self.x,self.y,self.wide,self.high)
        self.prep_text(text)
        self.can_click=True

    #显示按钮
    def draw_button(self):
        self.screen.fill(self.color,self.Brect)
        self.screen.blit(self.text_image,self.text_image_rect)
        self.prep_text(self.text)
    #执行事件
    def update(self,pos):
        if self.Brect.collidepoint(pos) and self.can_click:
            self.color=self.click_color
            pygame.event.wait()
            self.event()

    def chage_color(self,pos):
        if self.Brect.collidepoint(pos):
            self.color=self.n_color
        else:
            self.color=self.coll_color
        
    def set_elist(self,func):
        self.event=func

    #标签渲染
    def prep_text(self,text):
        self.text_image=font.render(text,True,self.text_color,self.color)
        self.text_image_rect=self.text_image.get_rect()
        self.text_image_rect.center=self.Brect.center
