# coding=utf-8
import pygame

from conf import WHITE, btnFontSize, fontYaHeiPath


class Button(pygame.sprite.Sprite):
    def __init__(self, text=u"按钮", wait=True, image1=pygame.Surface([100, 30], 0, 32),
                 image2=pygame.Surface([100, 30], 0, 32),
                 textPos=None, textColor=WHITE):
        super(Button, self).__init__()
        self.name = text
        self.wait = wait

        self.once = True

        self.img1 = image1
        self.img2 = image2
        self.image = self.img1
        self.rect = self.image.get_rect()

        font = pygame.font.Font(fontYaHeiPath, btnFontSize)

        self.text = font.render(text, True, textColor)
        if textPos is None:
            self.textPos = (self.rect.w - self.text.get_rect().w) / 2, (self.rect.h - self.text.get_rect().h) / 2 - 5
        else:
            self.textPos = textPos
        self.img1.blit(self.text, self.textPos)
        self.img2.blit(self.text, self.textPos)

    def click(self, *args):
        pass

    def update(self, *args):
        click = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if click[0] and self.rect.collidepoint(pos):
            if self.wait:
                pygame.event.wait()
                self.click(*args)
            else:
                self.click(*args)
        if self.rect.collidepoint(pos):
            self.image = self.img2
            self.mouseOver(*args)
        else:
            self.once = True
            self.image = self.img1

    def mouseOver(self, *args):
        if self.once:
            self.once = False
