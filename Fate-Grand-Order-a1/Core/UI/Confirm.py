import pygame

from Core.Game.function import getImage, centerXY, singleText
from conf import resourcePath, windowSize, BLACK, WHITE, fontYouyuanPath


class ConfirmButton(pygame.sprite.Sprite):
    def __init__(self, name):
        super(ConfirmButton, self).__init__()


class Confirm(pygame.sprite.OrderedUpdates):
    def __init__(self, title, msg, btns, funs, alpha=1):
        super(Confirm, self).__init__()
        mask = pygame.sprite.Sprite()
        mask.image = pygame.Surface(windowSize).convert()
        mask.image.set_alpha(255 * alpha)
        mask.rect = mask.image.get_rect()
        self.add(mask)

        background = pygame.sprite.Sprite()
        background.image = getImage(resourcePath + "image/create_confirm.png", type=1)
        background.rect = background.image.get_rect()
        background.rect.topleft = centerXY(background.rect.size)
        self.add(background)

        sp_title = pygame.sprite.Sprite()
        sp_title.image = singleText(title, BLACK, 18, fontYouyuanPath)
        sp_title.rect = sp_title.image.get_rect()
        sp_title.rect.topleft = background.rect.x + 50, background.rect.y + 100
        self.add(sp_title)

        sp_msg = pygame.sprite.Sprite()
        sp_msg.image = singleText(msg, BLACK, 16, fontYouyuanPath)
        sp_msg.rect = sp_msg.image.get_rect()
        sp_msg.rect.topleft = centerXY(sp_msg.rect.size)
        self.add(sp_msg)
        for btn in btns:
            self.add(ConfirmButton(btn))
