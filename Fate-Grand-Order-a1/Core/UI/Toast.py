import pygame
import Core.Game.globalvar as gl

from Core.DataType.Delay import Delay
from conf import WHITE


class Toast(pygame.sprite.Sprite):
    def __init__(self, msg, pos, size, delay):
        super(Toast, self).__init__()
        self.msgGroup = gl.get_value('Game').msgGroup

        self.msg = msg
        self.pos = pos
        from Core.Game.function import singleText
        self.text = singleText(self.msg, WHITE)
        if size:
            self.size = size
        else:
            self.size = self.text.get_rect().size
        self.surface_text = self.text
        self.image = pygame.Surface(self.size)
        self.delay = Delay(delay)
        self.image.blit(self.surface_text, [10, 10])

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self, *args):
        self.delay.update(17)
        if self.msgGroup.has(self) and self.delay.atRound(1):
            self.msgGroup.remove(self)
