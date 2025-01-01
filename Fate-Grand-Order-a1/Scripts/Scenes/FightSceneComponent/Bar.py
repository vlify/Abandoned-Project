import pygame

from Core.Game.Progress import Progress
from Core.Game.function import getFont, getImage, shadowFont
from conf import resourcePath, fontYouyuanPath, WHITE


class Bar(pygame.sprite.LayeredUpdates):
    def __init__(self, hp, max_hp, pos):
        super(Bar, self).__init__()
        self.hp = hp
        self.max_hp = max_hp
        self.pos = pos
        self.background = pygame.sprite.Sprite()
        self.background.image = getImage(resourcePath + "image/fight_bar_background.png", type=1)
        self.background.rect = self.background.image.get_rect()
        self.background.rect.topleft = pos
        self.add(self.background)

        self.font = getFont(fontYouyuanPath, 12)

        self.bar = Bar.Bar(self.hp, self.max_hp, self.pos)
        self.add(self.bar)

        pos = self.background.rect.x + self.background.rect.w, self.background.rect.y
        self.text = Bar.Text(self.font, self.hp, pos)
        self.add(self.text)

    def set_hp(self, value):
        self.hp = value
        self.bar.hp = value
        self.text.hp = value

    class Bar(pygame.sprite.Sprite):
        def __init__(self, hp, max_hp, pos):
            super(Bar.Bar, self).__init__()
            self.pos = pos
            self.hp = hp
            self.max_hp = max_hp
            self.surface = getImage(resourcePath + "image/fight_bar_hp.png", type=1)
            self.init()

        def init(self):
            if self.hp <= 0:
                self.hp = 0
            self.progress = Progress(self.hp, self.max_hp)
            size = [int(self.progress.getPoint(2) * self.surface.copy().get_rect().w / 100),
                    self.surface.copy().get_rect().h]
            self.image = pygame.transform.scale(self.surface.copy(), size)
            self.rect = self.image.get_rect()
            self.rect.topleft = self.pos[0] + 12, self.pos[1] + 3

        def update(self):
            super(Bar.Bar, self).update()
            self.init()

    class Text(pygame.sprite.Sprite):
        def __init__(self, font, hp, pos):
            super(Bar.Text, self).__init__()
            self.font = font
            self.hp = hp
            self.pos = pos
            self.init()

        def init(self):
            if self.hp <= 0:
                self.hp = 0
            surface = shadowFont(self.font, str(self.hp), WHITE)
            self.image = surface.copy()
            self.rect = surface.get_rect()
            self.rect.topleft = self.pos[0] + 5, self.pos[1] + 1

        def update(self):
            super(Bar.Text, self).update()
            self.init()
