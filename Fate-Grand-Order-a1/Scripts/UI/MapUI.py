# coding=utf-8
import pygame, time
import Core.Game.globalvar as gl

from Core.Game.function import create_surface, MultiText, resolve_image, bottom, get_game, getImage, singleText, \
    pause, floatRight, get_scene, get_system
from Core.UI.UIBase import UIBase, Container, Label, Button, View
from Scripts.UI.SysUI import SysUI
from Scripts.function import destory_say, get_resource, get_material, set_resource, empty_ui, add_ui
from conf import fontYouyuanPath, resourcePath, WHITE, servantPath


class Say(pygame.sprite.Sprite):
    def __init__(self, msg, delty=200, speed=1):
        super(Say, self).__init__()
        w = 255
        self.image = create_surface([255, 0], alpha=0)
        sp_msg = MultiText(msg, 16, width=w - 20, font=fontYouyuanPath)
        h = sp_msg.get_rect().h + 20
        size = 255, h
        self.image = resolve_image(resourcePath + "image/say.png", size, 20)
        self.image.blit(sp_msg, [13, 10])
        self.rect = self.image.get_rect()
        self.rect.topleft = 80, bottom(self.rect.h) - 155

        self.t = 0
        self.delty = delty
        self.speed = speed
        self.game = get_game()

    def update(self):
        self.t += self.speed
        if self.t >= self.delty:
            destory_say()


class TopBar(Container):
    def __init__(self, ui):
        super(TopBar, self).__init__()
        self.add(Label(2, getImage(resourcePath + "image/map_top_background.png", type=1), 'topbar_background'))
        self.add(TopBar.Time())
        self.add(TopBar.ResourceBar(), layer="resource_bar")
        self.add(TopBar.SysBar(ui), layer="sys_bar")

    class Time(Label):
        def __init__(self):
            now = time.localtime()
            super(TopBar.Time, self).__init__(3, singleText(
                "{0}-{1}-{2} {3}:{4}:{5}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,
                                                 now.tm_sec),
                WHITE), 'topbar_now_time')
            self.set_position(5, 5)

        def update(self):
            now = time.localtime()
            self.image = singleText(
                "{0}-{1}-{2} {3}:{4}:{5}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,
                                                 now.tm_sec), WHITE)

    class ResourceBar(Container):
        def __init__(self):
            super(TopBar.ResourceBar, self).__init__()
            _list = [
                TopBar.ResourceBar.ResourceIcon(6, 'gold', resourcePath + "image/map_top_gold_icon.png",
                                                get_resource('gold')),
                TopBar.ResourceBar.ResourceIcon(7, 'store', resourcePath + "image/map_top_store_icon.png",
                                                get_material('store')),
                TopBar.ResourceBar.ResourceIcon(8, 'wood', resourcePath + "image/map_top_wood_icon.png",
                                                get_material('wood')),
                TopBar.ResourceBar.ResourceIcon(9, 'cloth', resourcePath + "image/map_top_cloth_icon.png",
                                                get_material('cloth')),
                TopBar.ResourceBar.ResourceIcon(10, 'metal', resourcePath + "image/map_top_metal_icon.png",
                                                get_material('metal')),
                TopBar.ResourceBar.ResourceIcon(11, 'gem', resourcePath + "image/map_top_gem_icon.png",
                                                get_material('gem'))
            ]
            for i, icon in enumerate(_list):
                icon.rect.topleft = 550 + 100 * i + 5, 0
            self.add(_list)

        class ResourceIcon(Label):
            def __init__(self, id, name, icon, text):
                super(TopBar.ResourceBar.ResourceIcon, self).__init__(id, create_surface([100, 30], alpha=0), name)
                self.icon = icon
                self.image.blit(getImage(self.icon, type=1), [5, 5])
                self.image.blit(singleText(text, WHITE), [25, 5])

            def reload(self, text):
                self.image.fill([0, 0, 0, 0])
                self.image.blit(getImage(self.icon, type=1), [5, 5])
                self.image.blit(singleText(text, WHITE), [25, 5])

    class SysBar(Container):
        def __init__(self, ui):
            super(TopBar.SysBar, self).__init__()
            sysBtn = Button(13, 'sys_button', [self.sysui, ui.reloadResource])
            sysBtn.image = singleText(u'系', WHITE)
            sysBtn.rect = sysBtn.image.get_rect()
            sysBtn.rect.topleft = 1165, 5
            self.add(sysBtn)

        def sysui(self):
            pause()
            set_resource('gold', int(get_resource('gold')) + 10)
            empty_ui()
            add_ui(SysUI())


class BottomBar(Container):
    def __init__(self, ui):
        super(BottomBar, self).__init__()
        bg = Label(12, getImage(resourcePath + "image/map_bottom_background.png", type=1), "bottom_bar")
        bg.rect.topleft = 5, bottom(bg.rect.h) - 5
        self.add(bg)
        servant_id = gl.get_value("USER_DATA")['servant_id']
        if gl.get_value("USER_DATA")['servant_id'] < 10:
            servant_id = "0" + str(servant_id)
        else:
            servant_id = str(servant_id)

        path = servantPath + servant_id + "/image/thumb.png"
        thumb = Label(13, getImage(path, [129, 129], type=1), 'thumb')
        thumb.rect.topleft = bg.rect.x + 5, bg.rect.y + 5
        self.add(thumb)
        move = BottomBar.Field(14, 'move', u'移动：' + str(get_system().move_num))
        move.rect.topleft = thumb.rect.x + thumb.rect.w + 10, thumb.rect.y
        self.add(move)
        self.add(BottomBar.OverTurnButton())

    class Field(View):
        def __init__(self, id, name, text):
            super(BottomBar.Field, self).__init__(id, name)
            self.image = create_surface([65, 24], alpha=0)
            self.image.blit(singleText(text, WHITE, 12), [5, 5])
            self.rect = self.image.get_rect()

        def update(self):
            self.image = create_surface([65, 24], alpha=0)
            self.image.blit(singleText(u'移动：' + str(get_system().move_num), WHITE, 12), [5, 5])

    class OverTurnButton(Button):
        def __init__(self):
            super(BottomBar.OverTurnButton, self).__init__(15, 'over_button')
            self.image = getImage(resourcePath + "image/map_over_turn_button.png", type=1)
            self.rect = self.image.get_rect()
            self.rect.topleft = floatRight(self.rect.w) - 5, bottom(self.rect.h) - 5
            self.event.append(self.overTurn)

        def overTurn(self):
            get_system().over_turn()


class MapUI(UIBase):
    def __init__(self):
        super(MapUI, self).__init__()
        self.add(TopBar(self), layer="topbar")
        self.add(BottomBar(self), layer="bottombar")
        print get_scene()

    def reloadResource(self):
        self.get_sprite_by_name('gold').reload(get_resource('gold'))
        self.get_sprite_by_name('store').reload(get_material('store'))
        self.get_sprite_by_name('wood').reload(get_material('wood'))
        self.get_sprite_by_name('cloth').reload(get_material('cloth'))
        self.get_sprite_by_name('metal').reload(get_material('metal'))
        self.get_sprite_by_name('gem').reload(get_material('gem'))
