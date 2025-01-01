import pygame

from Core.Game.function import create_surface
from conf import windowSize


class MaskSprite(pygame.sprite.Sprite):
    def __init__(self, alpha=200):
        super(MaskSprite, self).__init__()
        self.image = create_surface(windowSize, alpha=alpha)
        self.rect = self.image.get_rect()
