# coding=utf-8
import pygame as pygame

import Core.Game.globalvar as gl
from Core.Game.function import set_scene
from conf import windowSize


class Scene(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super(Scene, self).__init__()
        set_scene(self)
        self.game = gl.get_value("Game")
        self.screen = self.game.screen


class Mask(pygame.sprite.Sprite):
    def __init__(self, speed=20):
        super(Mask, self).__init__()
        self.image = pygame.Surface(windowSize, 0, 32)
        self.rect = self.image.get_rect()
        self.type = type
        self.alpha = 255
        self.speed = speed

    def update(self, *args):
        super(Mask, self).update(*args)
        if self.alpha <= 0:
            self.kill()
        else:
            self.alpha -= self.speed
            self.image.set_alpha(self.alpha)
