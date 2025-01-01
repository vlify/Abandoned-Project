import os

import pygame
import Core.Game.globalvar as gl

from Core.Game.BaseGame import BaseGame
from Core.Game.Item import ItemBase
from Core.Game.function import getImage, floatRight, showDialog, pauseGameGroup, pause, singleText, play, playGameGroup, \
    getJsonFile
from Core.UI.Dialog import Dialog
from conf import resourcePath, WHITE


class MsgListDialog(Dialog):
    def __init__(self, name, size=[1260, 600]):
        # surface = getImage('Core/resource/image/alpha.png', size, type=1)
        surface = pygame.Surface(size)
        y = 0
        msglist = gl.get_value('MsgList')
        if msglist:
            for msg in reversed(msglist):
                txt = singleText(msg.msg, WHITE)
                y += 20
                surface.blit(txt, [10, y])
        super(MsgListDialog, self).__init__(name, surface, [10, 20], size, None)

    def destory(self):
        play()
        playGameGroup("isUIPlay")


class LiButton(pygame.sprite.Sprite):
    def __init__(self):
        super(LiButton, self).__init__()
        self.image = getImage(resourcePath + 'image/li.png', type=1)
        self.rect = self.image.get_rect()
        self.rect.x = floatRight(self.rect.w)

    def update(self):
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(pos):
            showDialog(MsgListDialog('d1'))
            pause()
            pauseGameGroup("isUIPlay")
            pygame.event.wait()


class Game(BaseGame):
    def __init__(self):
        super(Game, self).__init__()
        self.msgGroup = pygame.sprite.OrderedUpdates()
        self.uiGroup = pygame.sprite.OrderedUpdates()
        self.dialogGroup = pygame.sprite.OrderedUpdates()
        self.isUIPlay = True
        self.isMsgPlay = True
        self.isDialogPlay = True
        items = []
        path = "Data/Item"
        for file in os.listdir(path):
            data = getJsonFile(path + "/" + file)
            for item_data in data:
                items.append(ItemBase(item_data))
        gl.set_value("items", items)

    def group_run(self):
        self.uiGroup.draw(self.screen)
        self.dialogGroup.draw(self.screen)
        self.msgGroup.draw(self.screen)
        if self.isUIPlay:
            self.uiGroup.update()
        if self.isMsgPlay:
            self.msgGroup.update()
        if self.isDialogPlay:
            self.dialogGroup.update()
