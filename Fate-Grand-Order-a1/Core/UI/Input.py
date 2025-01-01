# coding=utf-8
import pygame

from Core.DataType.Delay import Delay
from Core.Game.function import singleText
from Core.conf import alphaImage
from conf import WHITE


class Input(pygame.sprite.Sprite):
    def __init__(self, pos, size=[100, 30], text=u'输入框', str=False, color=WHITE, borderColor=WHITE,
                 background=alphaImage):
        super(Input, self).__init__()
        self.pos = pos
        self.size = size
        self.bg = background
        self.text = text
        self.mo = text
        self.def_text = text
        self.str = str
        self.text_color = color
        self.borderColor = borderColor

        self.draw()

        self.focus = False
        self.delay = Delay()

    def draw(self):
        self.image = pygame.Surface(self.size)
        self.rect = pygame.rect.Rect([self.pos, self.size])

        self.text_surface = singleText(self.mo, self.text_color)
        self.image.blit(self.text_surface, [5, 5])
        pygame.draw.rect(self.image, self.borderColor, pygame.rect.Rect(0, 0, self.size[0], self.size[1]), 1)

    def update(self, *args):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if mouse[0]:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos[0], pos[1]):
                self.focus = True
            else:
                self.focus = False
        if self.focus:
            if self.text == self.def_text:
                self.text = ''
                self.mo = ''
            if 1 in keys:
                key = keys.index(1)
                if keys[pygame.K_BACKSPACE]:
                    self.text = self.text[:-1]
                    if self.str:
                        num = int(len(str(self.str)))
                        self.mo = self.mo[:-num]
                    else:
                        self.mo = self.mo[:-1]
                # a-z 0-9
                elif (key >= 97 and key <= 122) or (key >= 48 and key <= 57):
                    name = pygame.key.name(key)
                    self.text += str(name)
                    if self.str:
                        self.mo += str(self.str)
                    else:
                        self.mo = self.text
                # 小键盘1-0
                elif (key >= 256 and key <= 265):
                    name = pygame.key.name(key)[1:-1]
                    self.text += str(name)
                    if self.str:
                        self.mo += str(self.str)
                    else:
                        self.mo = self.text
                pygame.event.wait()
        else:
            if self.text == '':
                self.text = self.def_text
                self.mo = self.def_text
        self.draw()

    def get_text(self):
        if self.text == self.def_text:
            return ''
        else:
            return self.text
