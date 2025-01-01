# coding=utf-8
import pygame
import Core.Game.globalvar as gl

from Core.Game.Scene import Scene
from Core.Game.function import singleText, centerX, getImage, getJsonFile, jumpScene, click, playSound, \
    saveFile, removeFile
from Scripts.Scenes.CreateNewGameScene import CreateNewGameScene
from Scripts.Scenes.RandomMapScene import RandomMapScene
from conf import WHITE, resourcePath, windowSize, SavePath, fileType, servantPath


class SaveDoneScene(Scene):
    def __init__(self):
        super(SaveDoneScene, self).__init__()
        self.sprite_bg = pygame.sprite.Sprite()
        self.sprite_bg.image = getImage(resourcePath + 'image/save_done_background.jpg', windowSize)
        self.sprite_bg.rect = self.sprite_bg.image.get_rect()
        self.sprite_text = pygame.sprite.Sprite()
        self.sprite_text.image = singleText(u'选择存档', WHITE)
        self.sprite_text.rect = self.sprite_text.image.get_rect()
        self.sprite_text.rect.x = centerX(self.sprite_text.rect.w)
        self.sprite_text.rect.y = 80
        self.add(self.sprite_bg)
        self.add(self.sprite_text)

        data = {
            'id': 0
        }
        gl.set_value('User', data)
        self.user_id = gl.get_value('User')['id']

        save_num = 3
        _x = centerX(230 * save_num)

        for i in range(save_num):
            x = _x + 230 * i
            layer = LoadDoneLayer(x, 150, self.user_id, i)
            self.add(layer)


class SaveThumb(pygame.sprite.Sprite):
    def __init__(self, thumb, x, y):
        super(SaveThumb, self).__init__()
        self.image = thumb
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y


class NewButton(pygame.sprite.Sprite):
    def __init__(self, file, x, y):
        super(NewButton, self).__init__()
        self.file = file
        self.image = getImage(resourcePath + "image/new_button.png", type=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        if click(self.rect):
            playSound("click", 0, .2)
            jumpScene(CreateNewGameScene())
            user_id = gl.get_value('User')['id']
            file = str(user_id) + "/" + str(self.file)
            data = {
                'user_id': user_id,
                'save_done': file,
                'resources': {
                    'gold': 1000,
                    'prestige': 0
                },
                'material': {
                    'wood': 1000,
                    'store': 1000,
                    'cloth': 1000,
                    'metal': 1000,
                    'gem': 100,
                    'refine': 100
                },
                'package': [1, 1, 1, 1, 1, 2, 2, 3, 4, 5],
                'cards': [1, 1, 1, 1, 2]
            }
            gl.set_value("USER_DATA", data)
            saveFile(data, file)
            pygame.event.wait()


class LoadButton(pygame.sprite.Sprite):
    def __init__(self, fileData, x, y):
        super(LoadButton, self).__init__()
        self.fileData = fileData
        self.image = getImage(resourcePath + "image/load_button.png", type=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        if click(self.rect):
            gl.set_value("USER_DATA", self.fileData)
            jumpScene(RandomMapScene())
            pygame.event.wait()


class DelButton(pygame.sprite.Sprite):
    def __init__(self, fileData, x, y):
        super(DelButton, self).__init__()
        self.fileData = fileData
        self.image = getImage(resourcePath + "image/del_button.png", type=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        if click(self.rect):
            file = SavePath + self.fileData['save_done'] + ".json"
            removeFile(file)
            jumpScene(SaveDoneScene())
            pygame.event.wait()


class LoadDoneLayer(pygame.sprite.LayeredUpdates):
    def __init__(self, x, y, user_id, file):
        super(LoadDoneLayer, self).__init__()
        self.bg = pygame.sprite.Sprite()
        self.bg.image = getImage(resourcePath + 'image/save_background.png', type=1)
        self.bg.rect = self.bg.image.get_rect()
        self.bg.rect.topleft = x, y
        self.add(self.bg)

        filePath = SavePath + str(user_id) + "/" + str(file) + fileType
        btn_y = y + 190

        isFile = getJsonFile(filePath)

        if not isFile == False:
            data = getJsonFile(SavePath + str(user_id) + "/" + str(file) + ".json")
            servant_id = data['servant_id']
            if servant_id < 10:
                servant_id = "0" + str(servant_id)
            else:
                servant_id = str(servant_id)
            print servant_id
            thumb = getImage(servantPath + servant_id + "/image/thumb.png", [100, 100], type=1)
            thumb = SaveThumb(thumb, self.bg.rect.x + 35, 240)
            btn_y += 40
            lb = LoadButton(isFile, self.bg.rect.x + 30, btn_y)
            db = DelButton(isFile, lb.rect.x + lb.rect.w - 5, btn_y)

            self.add(thumb)
            self.add(lb)
            self.add(db)
        else:
            nb = NewButton(file, self.bg.rect.x + 48, btn_y)
            self.add(nb)
