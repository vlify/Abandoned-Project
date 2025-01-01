import pygame

from Core.Game.Page import Page
from Core.Game.function import getImage, getFont
from Core.UI.UIBase import ScaleButton
from conf import resourcePath, WHITE


class PageSprite(pygame.sprite.LayeredUpdates):
    def __init__(self, pageSize, maxNumber, pos):
        super(PageSprite, self).__init__()
        self.page = Page(pageSize, maxNumber)
        self.background = pygame.sprite.Sprite()
        self.background_surface = getImage(resourcePath + "image/sys_page_background.png")
        self.background.image = self.background_surface.copy()
        self.background.rect = self.background.image.get_rect()
        self.background.rect.topleft = pos
        surface = getImage(resourcePath + "image/sys_page_arrow.png", type=1)
        y = (self.background.rect.h - surface.get_rect().h) / 2 + pos[1]
        pos = 10 + pos[0], y
        self.prevButton = ScaleButton(surface, pos, 1.3, event=[self.prevPage])
        surface = pygame.transform.flip(surface, True, False)
        pos = pos[0] + self.background.rect.w - self.prevButton.rect.w - 20, y
        self.nextButton = ScaleButton(surface, pos, 1.3, event=[self.nextPage])

        surface = self.page.pages(getFont(size=14), WHITE)
        self.pagePos = (self.background.rect.w - surface.get_rect().w) / 2, (
            self.background.rect.h - surface.get_rect().h) / 2
        self.background.image.blit(surface, self.pagePos)

        self.add(self.background, self.prevButton, self.nextButton)

    def prevPage(self):
        self.background.image = self.background_surface.copy()
        self.page.prevPage()
        self.background.image.blit(self.page.pages(getFont(size=14), WHITE), self.pagePos)

    def nextPage(self):
        self.background.image = self.background_surface.copy()
        self.page.nextPage()
        self.background.image.blit(self.page.pages(getFont(size=14), WHITE), self.pagePos)
