# coding=utf-8
from random import randint

import numpy as np
import pygame

from Core.Game.function import getImage, cutImage, toOneArray, click, getJsonFile, near, \
    set_attr_matrix_coords, get_coords_in_matrix_for_val, set_attr_matrix, set_attr_matrix_all, showDialog, pause, \
    toast, get_system
from Scripts.Model.Servant import Servant
from Scripts.Type import TerrainType, ResourceType
from Scripts.UI.ChooseDialog import ChooseDialog
from Scripts.function import set_enemy_team
from conf import resourcePath, servantPath, dialogPath

__all__ = ['Map', 'Player', 'Camera']


class Camera(object):
    def __init__(self, size, blockSize, coods):
        super(Camera, self).__init__()
        self.size = size
        self.blockSize = blockSize
        self.coods = coods

    def center(self):
        return self.size[0] / 2 - self.blockSize[0] / 2 - self.coods[0], \
               self.size[1] / 2 - self.blockSize[1] / 2 - self.coods[1]

    def set_map_coods(self, coods):
        self.coods = coods


class Player(object):
    def __init__(self, pos, tileSize, surface, offer_pos=[0, 0]):
        super(Player, self).__init__()

        file = servantPath + '00/' + "data.json"
        data = getJsonFile(file)
        level = 1
        self.servant = Servant(data, level)

        self.move_speed = self.servant.move
        self.move_type = self.servant.movetype
        self.surface = surface
        self.surface_rect = pygame.Rect(pos[0] - (surface.get_rect().w - tileSize[0]) / 2 + offer_pos[0],
                                        pos[1] - (surface.get_rect().h - tileSize[1]) + offer_pos[1],
                                        surface.get_rect().w, surface.get_rect().h)
        self.pos = pos[0] + (self.surface_rect.w - tileSize[0]) / 2, pos[1] - (self.surface_rect.h - tileSize[1]) / 2
        self.tileSize = tileSize
        self.rect = pygame.Rect(pos, tileSize)

    def get_sprite(self):
        sp = pygame.sprite.Sprite()
        sp.image = self.surface
        sp.rect = self.surface_rect
        return sp


class Block(pygame.sprite.Sprite):
    def __init__(self, scene, terrain, pos, tileSize, fog=2, inPlayer=False, build=None, canAct=False, move=0):
        super(Block, self).__init__()
        self.scene = scene
        self.tileSize = tileSize
        self.pos = pos
        self.tile_pos = self.pos[0] * tileSize[0], self.pos[1] * tileSize[1]
        self.terrain = terrain

        self.fog = fog
        self.inPlayer = inPlayer
        self.build = build
        self.canAct = canAct
        self.move = move

        self.rect = pygame.Rect(self.tile_pos, self.tileSize)

        self.resource = self.create_resource(terrain)

        self.arr = toOneArray(cutImage(getImage(resourcePath + "image/terrain.png"), 32, 2, [32, 32]))

        self.image = self.arr[self.terrain - 1]

        self.set_image()

    def set_image(self):
        self.define_image = self.image.copy()
        self.hover_image = self.image.copy()
        self.hover_image.set_alpha(150)

        self.fog_image1 = self.image.copy()
        self.fog_image1.set_alpha(100)

        self.fog_image2 = self.image.copy()
        self.fog_image2.set_alpha(10)

    def create_resource(self, terrain):
        _dict = {}
        metal = randint(0, 10)
        wood = randint(0, 10)
        clot = randint(0, 10)
        # 草地
        if terrain == TerrainType.MEADOW:
            metal = randint(0, 10)
            wood = randint(20, 50)
            clot = randint(10, 60)
        _dict[ResourceType.METAL] = metal
        _dict[ResourceType.WOOD] = wood
        _dict[ResourceType.CLOT] = clot
        return _dict

    def update(self, *args):
        if not self.inPlayer:
            if self.fog == 1:
                self.image = self.fog_image1
            elif self.fog == 2:
                self.image = self.fog_image2
            else:
                self.image = self.define_image
        else:
            self.image = self.define_image
        mouse = pygame.mouse
        if self.canAct:
            if self.rect.collidepoint(mouse.get_pos()):
                self.image = self.hover_image
            else:
                self.image = self.define_image
            if click(self.rect):
                if get_system().can_move():
                    self.scene.move_player(self.rect.topleft, self.pos)
                    get_system().reduce_move(1)
                    if isinstance(self, BlockEnemy):
                        path = dialogPath + "map_enemy.json"
                        info = getJsonFile(path)
                        dialog = ChooseDialog(info, 1)
                        showDialog(dialog)
                        pause()
                        set_enemy_team(self.enemys)
                else:
                    if not get_system().state is 'player':
                        toast(u'这不是您的回合！')
                    else:
                        toast(u'您已经没有移动次数了！')
                pygame.event.wait()


class BlockEnemy(Block):
    def __init__(self, scene, enemys, terrain, pos, tileSize):
        super(BlockEnemy, self).__init__(scene, terrain, pos, tileSize)
        self.enemys = enemys
        self.image = self.define_image.copy()
        iconSize = 15, 15
        icon = getImage(resourcePath + "image/map_enemy.png", iconSize, type=1)
        self.define_image.blit(icon, [tileSize[0] - iconSize[1], 0])


class MapEnemy(object):
    def __init__(self, enemys, coord=[], terrain=''):
        super(MapEnemy, self).__init__()
        self.enemys = enemys
        self.coord = coord
        if terrain:
            self.terrain = terrain


class Map(pygame.sprite.LayeredUpdates):
    def __init__(self, scene, blockSizeNum, tileSize, enemy_blocks=[]):
        super(Map, self).__init__()
        self.scene = scene
        self.w, self.h = blockSizeNum
        self.tileSize = tileSize

        self.terrain = np.random.randint(1, 7, [self.w, self.h], 'int8')
        self.matrix_block = []

        enemy_coords = []
        for enemy in enemy_blocks:
            enemy_coords.append(enemy.coord)

        for x in range(self.h):
            l = []
            for y in range(self.w):
                pos = x, y
                terrain = self.terrain[x][y]
                if pos in enemy_coords:
                    enemys = [enemy_blocks[enemy_coords.index(pos)]]
                    b = BlockEnemy(self.scene, enemys, terrain, pos, tileSize)
                else:
                    b = Block(self.scene, terrain, pos, tileSize)
                l.append(b)
            self.matrix_block.append(l)

        for y in range(self.h):
            for x in range(self.w):
                self.add(self.matrix_block[x][y])

    def set_pos(self, pos):
        for y in range(self.h):
            for x in range(self.w):
                block = self.matrix_block[x][y]
                block.rect.topleft = pos[0] + block.rect.x, pos[1] + block.rect.y

    def move_area(self, player_coords, player_distance, type):
        return near(self.matrix_block, player_coords, player_distance, type)

    def set_player(self, coords):
        set_attr_matrix_coords(self.matrix_block, coords, 'inPlayer', True, False)

    def set_player_move_area(self, speed_num, type):
        coords = get_coords_in_matrix_for_val(self.matrix_block, 'inPlayer', True)
        areas, all = near(self.matrix_block, coords, speed_num, type)
        set_attr_matrix_all(self.matrix_block, 'move', 0)
        for move, area in areas.items():
            for x, y in area:
                block = self.matrix_block[x][y]
                block.move = move
        set_attr_matrix_coords(self.matrix_block, all, "canAct", True, False)
        set_attr_matrix(self.matrix_block, all, "canAct", True)

    def set_fog(self):
        for y in range(len(self.matrix_block)):
            for x in range(len(self.matrix_block[y])):
                block = self.matrix_block[x][y]
                if block.fog == 0:
                    block.fog = 1

    def reset_map(self):
        self.set_player_move_area(1, self.scene.player.servant.movetype)

    def set_fog_area(self, coords, see, type=2):
        areas, all = near(self.matrix_block, coords, see, type)
        set_attr_matrix(self.matrix_block, all, "fog", 0)
        self.set_fog()
