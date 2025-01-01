# coding=utf-8
import os

import pygame
import pyscroll
from pytmx.util_pygame import load_pygame
from Core.Game.Scene import Scene
from Core.Game.function import getImage
from Scripts.function import empty_ui
from conf import windowSize, resourcePath


class Sword(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Sword, self).__init__()
        self.image = getImage(resourcePath + "image/sword.png", type=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.size = 32, 32
        if os.path.exists("Data/Servant/04/image/player.png"):
            self.image = self.flip_image_left = getImage("Data/Servant/04/image/player.png", [32, 32], 1)
        else:
            self.image = self.flip_image_left = getImage(resourcePath + "image/player.png", type=1)

        self.flip_image_right = pygame.transform.flip(self.image, True, False)
        self.image = self.flip_image_left
        self.rect = self.image.get_rect()
        self.speed = 5


class MapScene(Scene):
    def __init__(self):
        super(MapScene, self).__init__()
        empty_ui()

        file = "Data/Map/000.tmx"
        # file = "Data/Map/test/grasslands.tmx"
        tmx_data = load_pygame(file)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.walls = []
        for object in tmx_data.objects:
            self.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))
        self.map_layer = pyscroll.BufferedRenderer(map_data, windowSize, clamp_camera=True, tall_sprites=1)
        self.map_layer.zoom = 1
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=4)
        self.player = Player()

        w, h = 20, 30
        self.player.rect.topleft = w * 32, h * 32
        self.group.add(self.player)

        self.swordGroup = pygame.sprite.OrderedUpdates()
        self.sword = Sword(self.player.rect.center)
        self.swordGroup.add(self.sword)
        self.add(self.group)
        # add_ui(MapUI())

    def update(self, *args):
        super(MapScene, self).update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.group.update()
        # self.uiGruop.draw(self.screen) # 18-11-23
        self.swordGroup.draw(self.screen)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.rect.x -= self.player.speed
            self.player.image = self.player.flip_image_left
            if self.player.rect.collidelist(self.walls) > -1:
                self.player.rect.x += self.player.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.rect.x += self.player.speed
            self.player.image = self.player.flip_image_right
            if self.player.rect.collidelist(self.walls) > -1:
                self.player.rect.x -= self.player.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player.rect.y -= self.player.speed
            if self.player.rect.collidelist(self.walls) > -1:
                self.player.rect.y += self.player.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player.rect.y += self.player.speed
            if self.player.rect.collidelist(self.walls) > -1:
                self.player.rect.y -= self.player.speed
