# coding=utf-8
import os

import pygame
import Core.Game.globalvar as gl

from Core.Game.Scene import Scene
from Core.Game.function import getImage, getJsonFile, singleText, floatRight, click, format_number, MultiText, \
    resolve_image, jumpScene, pause, showConfirm, closeConfirm, playSound, create_surface, saveFile
from Scripts.Model.Servant import Servant
from Scripts.Scenes.RandomMapScene import RandomMapScene
from Scripts.UI.Confirm import Confirm
from conf import resourcePath, servantPath, WHITE, fontYouyuanPath, windowSize


class Title(pygame.sprite.Sprite):
    def __init__(self, text, pos):
        super(Title, self).__init__()
        self.image = getImage(resourcePath + "image/create_title_background.png", type=1)
        self.text = singleText(text, path=fontYouyuanPath)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image.blit(self.text,
                        [(self.rect.w - self.text.get_rect().w) / 2, (self.rect.h - self.text.get_rect().h) / 2])


class TabBase(pygame.sprite.Sprite):
    def __init__(self, pos, servant, base_data, up_data, element, fight):
        super(TabBase, self).__init__()
        self.pos = pos

        self.image = create_surface([624, 278], alpha=0)
        b_title = getImage(resourcePath + "image/create_title_background.png", type=1)

        offset_w = 150
        # 基础
        text = singleText(u'基础', path=fontYouyuanPath)
        b_title.blit(text, [(b_title.get_rect().w - text.get_rect().w) / 2,
                            (b_title.get_rect().h - text.get_rect().h) / 2])
        stamina = singleText(u'耐力:{0}  +{1}'.format(format_number(int(base_data['stamina'])), up_data['stamina']))
        strength = singleText(u'力量:{0}  +{1}'.format(format_number(int(base_data['strength'])), up_data['strength']))
        agile = singleText(u'敏捷:{0}  +{1}'.format(format_number(int(base_data['agile'])), up_data['agile']))
        intelligence = singleText(
            u'智力:{0}  +{1}'.format(format_number(int(base_data['intelligence'])), up_data['intelligence']))
        spirit = singleText(u'精神:{0}  +{1}'.format(format_number(int(base_data['spirit'])), up_data['spirit']))
        memory = singleText(u'记忆:{0}  +{1}'.format(format_number(int(base_data['memory'])), up_data['memory']))
        memory = singleText(u'统御:{0}  +{1}'.format(format_number(int(base_data['rule'])), up_data['rule']))

        x, h, _h = 35, 21, 40
        self.image.blit(b_title, [x, 10])
        self.image.blit(stamina, [x, _h + h * 0])
        self.image.blit(strength, [x, _h + h * 1])
        self.image.blit(agile, [x, _h + h * 2])
        self.image.blit(intelligence, [x, _h + h * 3])
        self.image.blit(spirit, [x, _h + h * 4])
        self.image.blit(memory, [x, _h + h * 5])

        # 元素
        text = singleText(u'元素', path=fontYouyuanPath)
        e_title = getImage(resourcePath + "image/create_title_background.png", type=1)
        e_title.blit(text, [(e_title.get_rect().w - text.get_rect().w) / 2,
                            (e_title.get_rect().h - text.get_rect().h) / 2])
        fire = singleText(u'火:{0}'.format(element['fire']))
        water = singleText(u'水:{0}'.format(element['water']))
        thunder = singleText(u'雷:{0}'.format(element['thunder']))
        wind = singleText(u'风:{0}'.format(element['wind']))
        earth = singleText(u'土:{0}'.format(element['earth']))
        light = singleText(u'光:{0}'.format(element['light']))
        dark = singleText(u'暗:{0}'.format(element['dark']))

        x, h, _h = x + offset_w, 21, 20
        self.image.blit(e_title, [x, 10])
        self.image.blit(fire, [x, _h + h * 1])
        self.image.blit(water, [x, _h + h * 2])
        self.image.blit(thunder, [x, _h + h * 3])
        self.image.blit(wind, [x, _h + h * 4])
        self.image.blit(earth, [x, _h + h * 5])
        self.image.blit(light, [x, _h + h * 6])
        self.image.blit(dark, [x, _h + h * 7])

        # 攻击
        text = singleText(u'攻击', path=fontYouyuanPath)
        a_title = getImage(resourcePath + "image/create_title_background.png", type=1)
        a_title.blit(text, [(a_title.get_rect().w - text.get_rect().w) / 2,
                            (a_title.get_rect().h - text.get_rect().h) / 2])

        p_atk = singleText(u'物理攻击:{0}'.format(servant.p_atk))
        m_atk = singleText(u'魔法攻击:{0}'.format(servant.m_atk))
        fire = singleText(u'火穿:{0}'.format(110))
        water = singleText(u'水穿:{0}'.format(110))
        thunder = singleText(u'雷穿:{0}'.format(110))
        wind = singleText(u'风穿:{0}'.format(110))
        earth = singleText(u'土穿:{0}'.format(110))
        dark = singleText(u'暗穿:{0}'.format(110))

        x, h, _h = x + offset_w, 21, 20
        self.image.blit(a_title, [x, 10])
        self.image.blit(p_atk, [x, _h + h * 1])
        self.image.blit(m_atk, [x, _h + h * 2])
        self.image.blit(fire, [x, _h + h * 3])
        self.image.blit(water, [x, _h + h * 4])
        self.image.blit(thunder, [x, _h + h * 5])
        self.image.blit(wind, [x, _h + h * 6])
        self.image.blit(earth, [x, _h + h * 7])
        self.image.blit(dark, [x, _h + h * 8])

        # 防御
        text = singleText(u'防御', path=fontYouyuanPath)
        d_title = getImage(resourcePath + "image/create_title_background.png", type=1)
        d_title.blit(text, [(d_title.get_rect().w - text.get_rect().w) / 2,
                            (d_title.get_rect().h - text.get_rect().h) / 2])
        hp = singleText(u'生命:{0}'.format(110))
        defense = singleText(u'防御:{0}'.format(110))
        fire = singleText(u'火抗:{0}'.format(110))
        water = singleText(u'水抗:{0}'.format(110))
        thunder = singleText(u'雷抗:{0}'.format(110))
        wind = singleText(u'风抗:{0}'.format(110))
        earth = singleText(u'土抗:{0}'.format(110))
        dark = singleText(u'暗抗:{0}'.format(110))

        x, h, _h = x + offset_w, 21, 20
        self.image.blit(d_title, [x, 10])
        self.image.blit(hp, [x, _h + h * 1])
        self.image.blit(defense, [x, _h + h * 2])
        self.image.blit(fire, [x, _h + h * 3])
        self.image.blit(water, [x, _h + h * 4])
        self.image.blit(thunder, [x, _h + h * 5])
        self.image.blit(wind, [x, _h + h * 6])
        self.image.blit(earth, [x, _h + h * 7])
        self.image.blit(dark, [x, _h + h * 8])

        # 战斗
        text = singleText(u'战斗', path=fontYouyuanPath)
        f_title = getImage(resourcePath + "image/create_title_background.png", type=1)
        f_title.blit(text, [(f_title.get_rect().w - text.get_rect().w) / 2,
                            (f_title.get_rect().h - text.get_rect().h) / 2])
        speed = singleText(u'集气:{0}'.format(fight['speed']))
        parry = singleText(u'招架:{0}'.format(fight['parry']))
        dodge = singleText(u'闪避:{0}'.format(fight['dodge']))
        crit = singleText(u'暴击:{0}'.format(fight['crit']))
        combo = singleText(u'连击:{0}'.format(fight['combo']))
        hitback = singleText(u'反击:{0}'.format(fight['hitback']))
        chanting = singleText(u'吟唱:{0}'.format(fight['chanting']))
        speed_resist = singleText(u'抗压:{0}'.format(fight['speed_resist']))
        strong_chanting = singleText(u'强走:{0}'.format(fight['strong_chanting']))
        heal = singleText(u'战斗回复:{0}'.format(fight['heal']))
        notisdead = singleText(u'即死抵抗:{0}'.format(fight['notisdead']))

        x, y, h, _h, w = 35, 180, 21, 10, 100
        self.image.blit(f_title, [x, y])
        self.image.blit(speed, [x, y + _h + h * 1])
        self.image.blit(parry, [x + w * 1, y + _h + h * 1])
        self.image.blit(dodge, [x + w * 2, y + _h + h * 1])
        self.image.blit(crit, [x + w * 3, y + _h + h * 1])
        self.image.blit(combo, [x + w * 4, y + _h + h * 1])
        self.image.blit(hitback, [x + w * 5, y + _h + h * 1])
        self.image.blit(chanting, [x + w * 0, y + _h + h * 2])
        self.image.blit(speed_resist, [x + w * 1, y + _h + h * 2])
        self.image.blit(strong_chanting, [x + w * 2, y + _h + h * 2])
        self.image.blit(heal, [x + w * 3, y + _h + h * 2])
        self.image.blit(notisdead, [x + w * 4, y + _h + h * 2])

        pos = self.pos[0], self.pos[1]
        self.rect = pygame.Rect(pos, [626, 500])


class FeatureDes(pygame.sprite.Sprite):
    def __init__(self, title, des, pos, size, cur_w=35):
        super(FeatureDes, self).__init__()

        self.des_text = MultiText(des, 17, WHITE, size[0] - 30)

        if size[1] == "auto":
            size = size[0], self.get_h(35, 65)
        self.image = resolve_image(resourcePath + "image/create_feature_info.png", size, cur_w)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        title_bg = getImage(resourcePath + "image/create_feature_title_background.png", type=1)
        self.image.blit(title_bg, [(size[0] - title_bg.get_rect().w) / 2, 20])
        title_text = singleText(title, WHITE)
        self.image.blit(title_text, [(size[0] - title_text.get_rect().w) / 2, 20])

        self.image.blit(self.des_text, [(size[0] - self.des_text.get_rect().w) / 2, 60])

    def get_h(self, pt, pb):
        return self.des_text.get_rect().h + pt + pb


class Feature(pygame.sprite.Sprite):
    def __init__(self, scene, image, pos, title, des):
        super(Feature, self).__init__()
        self.scene = scene
        self.image = getImage(resourcePath + "image/create_feature_background.png", type=1)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image.blit(image, [(self.rect.w - image.get_rect().w) / 2, (self.rect.h - image.get_rect().h) / 2])
        size = 268, "auto"
        pos = windowSize
        self.fd = FeatureDes(title, des, pos, size)

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if not self.scene.has(self.fd):
                self.scene.add(self.fd)
            else:
                self.fd.rect.topleft = pos
        else:
            if self.scene.has(self.fd):
                self.scene.remove(self.fd)


class TabFeatures(pygame.sprite.LayeredUpdates):
    def __init__(self, scene, pos, data):
        super(TabFeatures, self).__init__()
        self.pos = pos
        self.data = data
        self.w = 125
        self.offer_x = 10
        self.offer_y = 10
        h = -1
        x = 0
        for key, feature in enumerate(data):
            image = singleText(feature['name'], WHITE, 12)
            if key % 5 == 0:
                h += 1
                x = 0
            pos = self.pos[0] + self.offer_x + self.w * x, self.offer_y + self.pos[1] + 40 * h
            x += 1
            self.add(Feature(scene, image, pos, feature['name'], feature['des']))


class LogoSprite(pygame.sprite.Sprite):
    def __init__(self, form, pos, thumb, index, focus):
        super(LogoSprite, self).__init__()
        self.index = index
        self.focus = focus
        self.form = form
        self.pos = pos
        self.thumb = getImage(thumb, [70, 70], type=1)
        self.hover = False

        self.hover_img = pygame.Surface([76, 76])
        self.hover_img.fill(WHITE)
        self.normal_img = create_surface([76, 76], alpha=0)

        self.set_hover()

    def set_hover(self):
        if self.focus:
            self.image = self.hover_img
        else:
            self.image = self.normal_img
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self._y = self.rect.y
        self.hover_y = self.rect.y - 5

    def set_focus(self):
        self.focus = True
        self.set_hover()

    def set_normal(self):
        self.focus = False

    def update(self):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(pos) and not self.focus:
            self.hover = True
        if not self.rect.collidepoint(pos) and not self.focus:
            self.hover = False

        if self.hover:
            self.rect.y = self.hover_y
        else:
            self.rect.y = self._y
        if self.focus:
            self.image = self.hover_img
            self.rect.y = self.hover_y
        else:
            self.image = self.normal_img
        self.image.blit(self.thumb, [3, 3])
        if click[0] and self.rect.collidepoint(pos) and not self.focus:
            playSound("sound6", 0, .1)
            self.form.set_focus(self.index)
            gl.set_value("SERVANT_ID", self.index + 1)
            pygame.event.wait()


class ArrowButton(pygame.sprite.Sprite):
    def __init__(self, form, pos, page):
        super(ArrowButton, self).__init__()
        self.form = form
        self.page = page
        self.image = getImage(resourcePath + "image/arrow.png", type=1)
        if page == 1:
            self.image = pygame.transform.flip(self.image, -1, 1)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        if click(self.rect):
            playSound("sound5", 0, .1)
            page = self.form.current_page + self.page
            if page < 1:
                page = self.form.last_page
            if page > self.form.last_page:
                page = 1
            self.form.scene.reset_page(page)
            pygame.event.wait()


class OkButton(pygame.sprite.Sprite):
    def __init__(self, scene):
        super(OkButton, self).__init__()
        self.scene = scene
        self.image = getImage(resourcePath + 'image/ok_button.png', type=1)
        self.rect = self.image.get_rect()

        btns = [u'是的就是我', u'不是']
        funs = [self.ok_fun, self.cancel_fun]
        self.confirm = Confirm(u'你是我的master吗?', u' 召唤に従い参上した.问おう,贵方は私のマスタか?', btns, funs, .8)

    def update(self):
        if click(self.rect):
            playSound("sound5", 0, .1)
            if not self.scene.has(self.confirm):
                showConfirm(self.confirm)
                pygame.event.wait()

    def ok_fun(self):
        playSound("sound6", 0, .1)
        closeConfirm(self.confirm)
        data = gl.get_value("USER_DATA")
        data['servant_id'] = gl.get_value("SERVANT_ID")
        saveFile(data, data['save_done'])
        jumpScene(RandomMapScene())

    def cancel_fun(self):
        playSound("sound5", 0, .1)
        closeConfirm(self.confirm)


class SelectServant(pygame.sprite.OrderedUpdates):
    def __init__(self, scene, pos, thumbs, page=1, page_size=13):
        super(SelectServant, self).__init__()
        self.scene = scene
        self.page_size = page_size
        self.current_page = page
        self.page = page - 1
        self.start_index = self.page * self.page_size
        if len(thumbs) % self.page_size:
            self.last_page = len(thumbs) / self.page_size + 1
        else:
            self.last_page = len(thumbs) / self.page_size
        self.thumbs = thumbs
        self.num = len(self.thumbs)
        self.pos = pos
        okbutton = OkButton(scene)
        okbutton.rect.topleft = 1050, 90
        self.add(okbutton)

        self.set_page(page)

    def set_arrow(self):
        y = 607
        pos = 110, y
        self.left_arrow_button = ArrowButton(self, pos, -1)
        pos = floatRight(self.left_arrow_button.rect.w) - 110, y
        self.right_arrow_button = ArrowButton(self, pos, 1)
        self.add(self.left_arrow_button)
        self.add(self.right_arrow_button)

    def set_focus(self, index):
        for logo in self.logos:
            logo.set_normal()
        self.logos[index - self.page * self.page_size + 1].set_focus()
        self.scene.resetUI(index + 1)
        self.scene.set_tab_current()

    def set_page(self, page):
        self.current_page = page
        self.page = page - 1
        start = self.page * self.page_size
        self.focus = start
        end = start + self.page_size - 1
        if self.num < end:
            end = self.num - 1
        self.logos = []
        i = 0
        for x in range(start, end + 1, 1):
            thumb = self.thumbs[x]
            focus = False
            _pos = [self.pos[0] + i * 78, self.pos[1]]
            if self.focus == x:
                focus = True
            logo = LogoSprite(self, _pos, thumb, x - 1, focus)
            self.logos.append(logo)
            self.add(logo)
            start += 1
            i += 1
        self.set_arrow()


class Text(pygame.sprite.Sprite):
    def __init__(self, text, pos=None):
        super(Text, self).__init__()
        self.text = text
        self.image = singleText(text, size=14, path=fontYouyuanPath)
        self.rect = self.image.get_rect()
        if pos:
            self.rect.topleft = pos

    def set_text(self, text, pos=None):
        self.text = text
        self.image = singleText(text, size=14, path=fontYouyuanPath)


class Tab(pygame.sprite.LayeredUpdates):
    def __init__(self, scene, servant, btns, pos, size, data, index=0):
        super(Tab, self).__init__()
        self.data = data
        self.servant = servant
        self.scene = scene
        self.pos = pos
        self.size = size

        self.tab_buttons = btns
        self.current_tab = index
        self.set_tabs()
        self.set_content()

    def set_content(self):
        pos = self.pos[0], self.pos[1] + 30
        if self.current_tab == 0:
            tab = TabBase(pos, self.servant, self.data['base'], self.data['up'], self.data['element'],
                          self.data['fight'])
        else:
            tab = TabFeatures(self.scene, pos, self.data['features'])
        self.add(tab)

    def set_tabs(self):
        tab_offer_x = 15
        tab_offer_y = 7
        tab_offer_w = 65
        for key, btn in enumerate(self.tab_buttons):
            pos = self.pos[0] + tab_offer_x + tab_offer_w * key, self.pos[1] + tab_offer_y
            focus = False
            if self.current_tab == key:
                focus = True
            self.add(TabButton(self.scene, key, btn, pos, focus))


class TabButton(pygame.sprite.Sprite):
    def __init__(self, scene, index, text, pos, focus=False):
        super(TabButton, self).__init__()
        self.index = index
        self.scene = scene
        self.focus = focus
        self.text = text
        self.pos = pos

        self.size = 60, 24
        self.image = create_surface(self.size, alpha=0)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.def_image = singleText(text, WHITE, path=fontYouyuanPath)
        self.focus_image = self.def_image.copy()
        self.x = (self.size[0] - self.def_image.get_rect().w) / 2
        self.y = (self.size[1] - self.def_image.get_rect().h) / 2
        self.image.blit(self.def_image, [self.x, self.y])

    def update(self):
        if click(self.rect):
            self.scene.set_tab_current(self.index)
            pygame.event.wait()
        if self.focus:
            pygame.draw.line(self.image, WHITE, [0, self.size[1] - 1], [self.size[0], self.size[1] - 1], 1)


class CreateNewGameScene(Scene):
    def __init__(self):
        super(CreateNewGameScene, self).__init__()

        self.background = pygame.sprite.Sprite()
        self.background.image = getImage(resourcePath + 'image/create_background.png', type=1)
        self.background.rect = self.background.image.get_rect()
        self.add(self.background)

        self.thumbs = []
        files = os.listdir(servantPath)

        for file in files:
            self.thumbs.append(servantPath + str(file) + '/image/logo.png')
        self.set_page()
        self.set_tab()

    def set_tab_current(self, index=0):
        self.remove(self.tabform)
        self.set_tab(index)

    def set_tab(self, index=0):
        pos = 555, 218
        size = 627, 310
        btns = [u'属性', u'特性', u'装备', u'战斗技能', u'环境技能', u'互动', u'生产', u'卡片', u'队伍']
        self.tabform = Tab(self, self.current_servant, btns, pos, size, self.current_servant_data, index)
        self.add(self.tabform)

    def clearUI(self):
        self.remove(self.thumb, self.name, self.sex, self.profession, self.identity, self.race, self.love,
                    self.team_location, self.weapon, self.mainparm, self.weight, self.stand, self.move, self.movetype,
                    self.features_num, self.interaction_num, self.production_num)

    def resetUI(self, index):
        self.clearUI()
        self.set_data(index)

    def set_data(self, index):
        self.current = index
        if self.current < 10:
            self.current = "0" + str(self.current)
        file = servantPath + str(self.current) + '/' + "data.json"
        self.current_servant_data = getJsonFile(file)
        self.current_servant = Servant(self.current_servant_data)
        self.loadUI()
        self.setUI()

    def loadUI(self):
        self.thumb = pygame.sprite.Sprite()
        self.thumb.image = getImage(servantPath + str(self.current) + '/image/thumb.png')
        self.thumb.rect = self.thumb.image.get_rect()
        self.thumb.rect.topleft = 110, 100
        self.name = Text(u'载入中...', [595, 108])
        self.sex = Text(u'载入中...', [595, 125])
        self.profession = Text(u'载入中...', [595, 144])
        self.identity = Text(u'载入中...', [595, 163])
        self.race = Text(u'载入中...', [595, 182])
        self.love = Text(u'载入中...', [595, 201])

        self.team_location = Text(u'载入中...', [790, 108])
        self.weapon = Text(u'载入中...', [790, 125])
        self.mainparm = Text(u'载入中...', [790, 144])
        self.weight = Text(u'载入中...', [790, 163])
        self.stand = Text(u'载入中...', [790, 182])

        self.move = Text(u'载入中...', [1000, 108])
        self.movetype = Text(u'载入中...', [1000, 125])
        self.features_num = Text(u'载入中...', [1000, 144])
        self.interaction_num = Text(u'载入中...', [1000, 163])
        self.production_num = Text(u'载入中...', [1000, 182])

        self.add(self.thumb, self.name, self.sex, self.profession, self.identity, self.race, self.love,
                 self.team_location, self.weapon, self.mainparm, self.weight, self.stand, self.move, self.movetype,
                 self.features_num, self.interaction_num, self.production_num)

    def setUI(self):
        self.name.set_text(self.current_servant.name)
        self.sex.set_text(self.current_servant.sex)
        self.profession.set_text(self.current_servant_data['profession'])
        self.identity.set_text(self.current_servant_data['identity'])
        self.race.set_text(self.current_servant.ract_str)
        self.love.set_text(self.current_servant_data['love'])

        self.team_location.set_text(self.current_servant_data['team_location'])
        self.weapon.set_text(self.current_servant.weapon_str)
        self.mainparm.set_text(self.current_servant_data['mainparm'])
        self.weight.set_text(str(self.current_servant_data['weight']))
        self.stand.set_text(self.current_servant.stand_str)

        self.move.set_text(str(self.current_servant_data['move']))
        self.movetype.set_text(str(self.current_servant_data['movetype']))
        self.features_num.set_text(str(self.current_servant_data['features_num']))
        self.interaction_num.set_text(str(self.current_servant_data['interaction_num']))
        self.production_num.set_text(str(self.current_servant_data['production_num']))

    def reset_page(self, page):
        self.clearUI()
        self.remove(self.servants)
        self.set_page(page)

    def set_page(self, page=1):
        self.servants = SelectServant(self, [133, 590], self.thumbs, page)
        self.add(self.servants)
        self.current = self.servants.start_index
        self.set_data(self.current)
