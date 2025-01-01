import pygame

from Core.Game.Scene import Scene
from Core.Game.function import create_surface
from Core.UI.UIBase import Button
from conf import WHITE


class Button1(Button):
    def __init__(self, id, name):
        super(Button1, self).__init__(id, name)
        size = 20, 20
        self.image = create_surface(size, WHITE)
        self.rect = self.image.get_rect()
        self.pos = self.rect.topleft
        self.speed = 3

    def create_self(*args):
        print args

    def update(self, *args):
        super(Button1, self).update()
        keys = pygame.key.get_pressed()
        if 1 in keys:
            if keys[pygame.K_w]:
                self.rect.move_ip(0, -self.speed)
            if keys[pygame.K_s]:
                self.rect.move_ip(0, self.speed)
            if keys[pygame.K_a]:
                self.rect.move_ip(-self.speed, 0)
            if keys[pygame.K_d]:
                self.rect.move_ip(self.speed, 0)

    def request(self, *args):
        if args:
            print args


class TestScene(Scene):
    def __init__(self):
        super(TestScene, self).__init__()
        self.btns = [Button1(0, "n1"), Button1(0, "n1"), Button1(0, "n1"), Button1(0, "n1")]
        self.add(self.btns)
