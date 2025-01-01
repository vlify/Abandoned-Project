import pygame

from Core.DataType.Delay import Delay
from Core.Game.function import numberSurface, get_game


class HitSprite(pygame.sprite.Sprite):
    def __init__(self, value, pos=[], centerPos=[], boom=False, type=1):
        super(HitSprite, self).__init__()
        self.value = value
        self.image = numberSurface(value)
        self.rect = self.image.get_rect()
        if pos:
            self.rect.topleft = pos
        if centerPos:
            self.rect.center = centerPos
        self.offer_y = 30
        self.focus_y = self.rect.y - self.offer_y
        self.delay = Delay(30)
        self.speed = 2

    def update(self):
        super(HitSprite, self).update()
        self.delay.update(get_game().mTime)
        if self.rect.y > self.focus_y:
            if self.delay.loopRound(1):
                self.rect.y -= self.speed
        else:
            self.kill()
