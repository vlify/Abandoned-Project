import pygame

from Core.Game.AI import AI
from Core.Game.function import get_scene
from conf import windowSize


class AiMove(AI):
    def __init__(self, sprite):
        super(AiMove, self).__init__()
        self.sprite = sprite
        self.image = self.sprite.image
        self.rect = self.sprite.image.get_rect()

    @staticmethod
    def floow(sprite, pos):
        speed = pygame.math.Vector2(pos) - pygame.math.Vector2(sprite.rect.topleft)
        if not speed == [0, 0]:
            speed.scale_to_length(sprite.speed)
            sprite.rect.move_ip(speed)

    @staticmethod
    def posMove(sprite):
        sprite.rect.move_ip(sprite.vectorSpeed)

    @staticmethod
    def outWindowDestory(sprite):
        rect = sprite.rect
        if rect.x <= 0 - rect.w or rect.y <= 0 or rect.x - rect.h >= windowSize[0] or rect.y >= windowSize[1]:
            get_scene().remove(sprite)

    @staticmethod
    def move_ip(sprite, moveIp):
        sprite.rect.move_ip(moveIp)
