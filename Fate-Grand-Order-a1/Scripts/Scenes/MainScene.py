# coding=utf-8
import pygame
import Core.Game.globalvar as gl

from Core.UI.Button import Button
from Core.UI.Input import Input
from Core.Game.Scene import Scene
from Core.Game.function import playMusic, centerXY, getImage, toast, getJsonFile, jumpScene, playSound
from Scripts.Game import LiButton
from Scripts.Scenes.SaveDoneScene import SaveDoneScene
from Scripts.function import add_ui
from conf import resourcePath, windowSize, userPath


class MainScene(Scene):
    def __init__(self):
        super(MainScene, self).__init__()
        # playMusic("mainMusic.mp3", .2)
        self.bg = pygame.sprite.Sprite()
        self.bg.image = getImage(resourcePath + 'image/background.jpg', windowSize)
        self.bg.rect = self.bg.image.get_rect()
        self.field = LoginField(centerXY([100, 30]))
        add_ui(LiButton())
        self.add(self.bg)
        self.add(self.field)

    def update(self, *args):
        super(MainScene, self).update(*args)
        self.field.update()


class LoginButton(Button):
    def __init__(self, field):
        super(LoginButton, self).__init__(u'登录')
        self.field = field
        self.isLogin = False

    def click(self):
        user_data = getJsonFile(userPath)
        for data in user_data:
            nickname = data['nickname']
            username = data['username']
            password = data['password']
            if self.field.username.get_text() == username and self.field.password.get_text() == password:
                playSound("click", 0, .2)
                gl.set_value('User', data)
                jumpScene(SaveDoneScene())
                self.isLogin = nickname
                break
        if self.isLogin:
            str = u"{0} 登录成功".format(self.isLogin)
        else:
            str = u"登录错误"
        toast(str)


class LoginField(pygame.sprite.Group):
    def __init__(self, pos):
        super(LoginField, self).__init__()
        self.loginbtn = LoginButton(self)
        self.username = Input(pos, text=u'用户名')
        pos = pos[0], pos[1] + 40
        self.password = Input(pos, text=u'密码', str='*')
        self.loginbtn.rect.topleft = pos[0], pos[1] + 35
        self.add(self.username)
        self.add(self.password)
        self.add(self.loginbtn)
        self.username.text = 'admin'
        self.password.text = '123456'
