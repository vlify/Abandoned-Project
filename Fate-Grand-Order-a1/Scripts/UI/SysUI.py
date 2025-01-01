# coding=utf-8
import os

import pygame

import Core.Game.globalvar as gl
from Core.Game.function import singleText, getImage, get_game, create_surface, centerX, resolve_image, play, click, \
    MultiText
from Core.UI.UIBase import UIBase, Button, Label, Container
from Scripts.function import empty_ui, add_ui
from conf import WHITE, resourcePath, fontYouyuanPath

selected = "Person"
menu_data = [
    {"id": 0, "name": "Person", "title": u"状态", "btn_id": 2, "content": 1},
    {"id": 1, "name": "Refine", "title": u"精炼", "btn_id": 3, "content": 1},
    {"id": 2, "name": "Package", "title": u"背包", "btn_id": 4, "content": 1},
    {"id": 3, "name": "Skill", "title": u"技能", "btn_id": 5, "content": 1},
    # {"id": 4, "name": "Talent", "title": u"天赋", "btn_id": 6, "content": 0},
    {"id": 4, "name": "Team", "title": u"队伍", "btn_id": 7, "content": 1},
    # {"id": 5, "name": "Card", "title": u"卡牌", "btn_id": 8, "content": 1},
    # {"id": 7, "name": "Create", "title": u"打造", "btn_id": 9, "content": 0},
    {"id": 5, "name": "Exit", "title": u"返回", "btn_id": 10, "content": 0}
]
package_data = [
    {"package": "item", "icon": "0/001", "num": 1, "stack": 10},
    {"package": "item", "icon": "0/002", "num": 2, "stack": 10},
    {"package": "item", "icon": "0/003", "num": 3, "stack": 10},
    {"package": "item", "icon": "0/004", "num": 4, "stack": 10},
    {"package": "item", "icon": "0/005", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/006", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/007", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/008", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/009", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/010", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/011", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/012", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/013", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/014", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/015", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/016", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/017", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/018", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/019", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/020", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/021", "num": 5, "stack": 10},
    {"package": "item", "icon": "0/022", "num": 5, "stack": 10},

    {"package": "item", "icon": "1/001", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/002", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/003", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/004", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/005", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/006", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/007", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/008", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/009", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/000", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/011", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/012", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/013", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/014", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/015", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/016", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/017", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/018", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/019", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/020", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/021", "num": 5, "stack": 10},
    {"package": "item", "icon": "1/022", "num": 5, "stack": 10},

    {"package": "skill", "icon": "0/000", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/001", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/002", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/003", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/004", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/005", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/006", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/007", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/008", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/009", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/010", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/011", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/012", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/013", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/014", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/015", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/016", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/017", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/018", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/019", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/020", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/021", "num": 5, "stack": 10},
    {"package": "skill", "icon": "0/022", "num": 5, "stack": 10},
]


def content_box():
    size = 1220, 600
    sp = pygame.sprite.Sprite()
    sp.image = resolve_image(resourcePath + "image/sys_content_background.png", size)
    sp.rect = sp.image.get_rect()
    y = 80
    sp.rect.topleft = centerX(size[0]), y
    return sp


def emptyIcon():
    return create_surface([55, 55], WHITE, 120)


class Page(Container):
    def __init__(self):
        super(Page, self).__init__()


class Item(pygame.sprite.Sprite):
    def __init__(self, id, package, icon, num, stack):
        super(Item, self).__init__()
        self.id = id
        path = resourcePath + "image/icon/" + package + "/" + icon + ".png"
        if not os.path.exists(path):
            path = resourcePath + "image/icon/" + package + "/" + icon + ".jpg"
        icon = getImage(path, [50, 50], type=1)
        self.image = getImage(resourcePath + "image/sys_item_background.png", type=1)
        self.rect = self.image.get_rect()
        self.image.blit(icon, [(self.rect.w - icon.get_rect().w) / 2,
                               (self.rect.h - icon.get_rect().h) / 2])
        self.num = num
        self.stack = stack
        offer = 8
        if self.num > 1:
            sp_num = singleText("X" + str(self.num), WHITE, 16)
            pos = self.rect.w - sp_num.get_rect().w - offer, self.rect.h - sp_num.get_rect().h - offer
            self.image.blit(sp_num, pos)


class Player(object):
    def __init__(self):
        super(Player, self).__init__()
        self.name = 'damao'
        self.hp = self.max_hp = 100
        self.mp = self.max_mp = 100

    def reduce(self, num):
        self.hp -= num

    def get_hp(self):
        return str(self.hp)


class Person(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Person, self).__init__()
        equips = [content_box(), Person.Equip(), Person.Treasure(), Person.Dress(), Person.Head(), Person.Head(),
                  Person.Body(), Person.Hand(), Person.OffHand(), Person.Foot()]

        self.add(equips)

        self.items = Person.Items()
        self.add(self.items)

    class Equip(Label):
        def __init__(self):
            super(Person.Equip, self).__init__(1, getImage(resourcePath + "image/sys_person_left.png", type=1), 'equip')
            self.rect.topleft = 70, 170

    class Treasure(Label):
        def __init__(self):
            super(Person.Treasure, self).__init__(2, emptyIcon(), 'treasure')
            self.rect.topleft = 89, 212

    class Dress(Label):
        def __init__(self):
            super(Person.Dress, self).__init__(3, emptyIcon(), 'dress')
            self.rect.topleft = 89, 319

    class Head(Label):
        def __init__(self):
            super(Person.Head, self).__init__(4, emptyIcon(), 'head')
            self.rect.topleft = 401, 201

    class Body(Label):
        def __init__(self):
            super(Person.Body, self).__init__(5, emptyIcon(), 'body')
            self.rect.topleft = 399, 290

    class Hand(Label):
        def __init__(self):
            super(Person.Hand, self).__init__(6, emptyIcon(), 'hand')
            self.rect.topleft = 340, 380

    class OffHand(Label):
        def __init__(self):
            super(Person.OffHand, self).__init__(7, emptyIcon(), 'off_hand')
            self.rect.topleft = 457, 378

    class Foot(Label):
        def __init__(self):
            super(Person.Foot, self).__init__(8, emptyIcon(), 'foot')
            self.rect.topleft = 400, 468

    class Button(Button):
        def __init__(self, id, name, text, icon, event=[]):
            super(Person.Button, self).__init__(id, name, event)
            size = 48, 20
            def_image = create_surface(size, WHITE, 0)
            def_image.blit(singleText(text, WHITE, 12, fontYouyuanPath), [17, 4])
            self.def_image = def_image

            self.clicked_image = create_surface(size, WHITE, 0)
            self.clicked_image.blit(singleText(text, WHITE, 12, fontYouyuanPath), [17, 4])
            self.clicked_image.blit(getImage(icon, type=1), [0, 2])

            self.clicked = False

            self.image = self.def_image
            self.rect = self.image.get_rect()

            self.event.append(self.onClick)

        @classmethod
        def by_pos(cls, id, name, text, icon, pos, event=[]):
            sp = cls(id, name, text, icon, event)
            sp.rect.topleft = pos
            return sp

        def onClick(self):
            self.clicked = True

        def update(self, *args):
            super(Person.Button, self).update(*args)
            if self.clicked:
                self.image = self.clicked_image
            else:
                self.image = self.def_image

    class Items(Container):
        def __init__(self):
            super(Person.Items, self).__init__()
            self.add(Label.create_by_pos(9, 'items_bg',
                                         resolve_image(resourcePath + "image/sys_person_right.png", [650, 480]),
                                         [560, 170]))
            w = 43
            off_w = 560
            y = 145
            self.cate_buttons = [
                Person.Button.by_pos(10, 'treasure_button', u'宝具', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 0, y], [self.clearCateButton]),
                Person.Button.by_pos(11, 'dress_button', u'礼装', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 1, y], [self.clearCateButton]),
                Person.Button.by_pos(12, 'hand_button', u'武器', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 2, y], [self.clearCateButton]),
                Person.Button.by_pos(13, 'off_hand_button', u'副手', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 3, y], [self.clearCateButton]),
                Person.Button.by_pos(14, 'head_button', u'头部', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 4, y], [self.clearCateButton]),
                Person.Button.by_pos(15, 'body_button', u'胸部', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 5, y], [self.clearCateButton]),
                Person.Button.by_pos(16, 'foot_button', u'腿部', resourcePath + "image/sys_person_clicked_0.png",
                                     [off_w + w * 6, y], [self.clearCateButton])
            ]
            self.cate_buttons[0].clicked = True
            self.add(self.cate_buttons)
            off_w = 1080
            self.filter_buttons = [
                Person.Button.by_pos(17, 'order_button', u'默认', resourcePath + "image/sys_person_clicked_1.png",
                                     [off_w + w * 0, y], [self.clearFilterButton]),
                Person.Button.by_pos(18, 'level_button', u'等级', resourcePath + "image/sys_person_clicked_1.png",
                                     [off_w + w * 1, y], [self.clearFilterButton]),
                Person.Button.by_pos(19, 'quality_button', u'品质', resourcePath + "image/sys_person_clicked_1.png",
                                     [off_w + w * 2, y], [self.clearFilterButton]),
            ]
            self.filter_buttons[0].clicked = True
            self.add(self.filter_buttons)

            x = 560
            y = 170
            self.items = [
                Person.Items.PersonItem.by_position(20, "item", "0/003", 1, 1, [x + 98 * 0, y]),
                Person.Items.PersonItem.by_position(21, "item", "0/004", 1, 1, [x + 98 * 1, y])
            ]
            self.add(self.items)

        def clearCateButton(self):
            for button in self.cate_buttons:
                button.clicked = False
            self.clearFilterButton()
            self.filter_buttons[0].clicked = True

        def clearFilterButton(self):
            for button in self.filter_buttons:
                button.clicked = False

        class PersonItem(Item):
            def __init__(self, id, package, icon, num, stack):
                super(Person.Items.PersonItem, self).__init__(id, package, icon, num, stack)

            @classmethod
            def by_position(cls, id, package, icon, num, stack, pos):
                sp = cls(id, package, icon, num, stack)
                sp.rect.topleft = pos
                cls.pos = pos
                return sp

            def update(self, *args):
                global focus_item
                super(Person.Items.PersonItem, self).update()


class Refine(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Refine, self).__init__()
        self.add(content_box())
        background = Label(1, getImage(resourcePath + "image/sys_refine_background.png", type=1), 'refind_background')
        background.rect.topleft = 150, 150
        self.add(background)
        content = Label(2, resolve_image(resourcePath + "image/sys_content_background.png", [685, 510]))
        content.rect.topleft = 535, 125
        self.add(content)
        content = Label(3, resolve_image(resourcePath + "image/sys_content_background.png", [428, 105]))
        content.rect.topleft = 95, 530
        self.add(content)


class Package(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Package, self).__init__()
        global package_data
        self.add(content_box())
        # 当前页
        self.current_page = 1
        # 总页
        self.page = 1
        x_size = 11
        y_size = 11
        x = 0
        y = -1
        for id, item in enumerate(package_data):
            x += 1
            if id % x_size == 0:
                x = 0
                y += 1
            item = Item(id + 1, item['package'], item['icon'], item['num'], item['stack'])
            item.rect.topleft = 50 + (item.rect.w + 10) * x, 95 + (item.rect.h) * y
            self.add(item)


class Skill(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Skill, self).__init__()
        self.add(content_box())
        items = [
            {"name": u"领导力[B]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[A]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[C]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[C]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[C]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[C]", "desc": u'己方全体攻击力提升3回合'},
            {"name": u"领导力[C]", "desc": u'己方全体攻击力提升3回合'},
        ]
        x = 0
        y = -1
        max_x = 4
        max_y = 3
        sp_items = []
        selected_list = [1, 3, 4, 7]
        for index, item in enumerate(items):
            x += 1
            if index % max_x == 0:
                x = 0
                y += 1
            pos = 100 + (232 + 50) * x, 120 + (90 + 25) * y
            name = "item_" + str(index)
            selected = False
            if index in selected_list:
                selected = True
            sp_items.append(Skill.Item(index, name, item, [], pos, selected))
        self.add(sp_items)

    class Item(Button):
        def __init__(self, id, name, data, event, pos, selected):
            super(Skill.Item, self).__init__(id, name, event)
            self.selected = selected
            self.name = data['name']
            self.desc = data['desc']
            if self.selected:
                path = resourcePath + "image/sys_skill_item.png"
            else:
                path = resourcePath + "image/sys_selected_skill_item.png"
            self.image = getImage(path, type=1)
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            self.image.blit(singleText(self.name, WHITE), [10, 10])
            self.image.blit(MultiText(self.desc, 10, WHITE, 150), [10, 35])

        def update(self):
            if self.selected:
                path = resourcePath + "image/sys_skill_item.png"
            else:
                path = resourcePath + "image/sys_selected_skill_item.png"
            self.image = getImage(path, type=1)
            self.image.blit(singleText(self.name, WHITE), [10, 10])
            self.image.blit(MultiText(self.desc, 10, WHITE, 150), [10, 35])
            if click(self.rect):
                if self.selected:
                    self.selected = False
                else:
                    self.selected = True
                pygame.event.wait()

    class SelectedItem(Button):
        def __init__(self, id, name, data, event, pos):
            super(Skill.SelectedItem, self).__init__(id, name, event)
            self.image = getImage(resourcePath + "image/sys_selected_skill_item.png", type=1)
            self.rect = self.image.get_rect()
            self.rect.topleft = pos
            self.image.blit(singleText(data['name'], WHITE), [10, 10])
            self.image.blit(MultiText(data['desc'], 10, WHITE, 150), [10, 35])


class Team(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Team, self).__init__()
        self.add(content_box())


class Card(pygame.sprite.OrderedUpdates):
    def __init__(self):
        super(Card, self).__init__()
        self.add(content_box())


class MenuButton(Button):
    def __init__(self, id, name, title, event=[]):
        super(MenuButton, self).__init__(id, name)
        self.image = getImage(resourcePath + "image/sys_menu_background.png", type=1)
        self.hover_image = getImage(resourcePath + "image/sys_menu_hover_background.png", type=1)
        self.sp_text = singleText(title, WHITE, 16)
        self.image.blit(self.sp_text, [(self.image.get_rect().w - self.sp_text.get_rect().w) / 2,
                                       (self.image.get_rect().h - self.sp_text.get_rect().h) / 2])
        self.def_image = self.image.copy()
        self.hover_image.blit(self.sp_text, [(self.image.get_rect().w - self.sp_text.get_rect().w) / 2,
                                             (self.image.get_rect().h - self.sp_text.get_rect().h) / 2])
        self.rect = self.image.get_rect()
        self.selected = False

        self.event = [self.select, self.set_selected_id]
        if event:
            self.event = event

    def select(self):
        self.selected = True

    def set_selected_id(self):
        global selected
        selected = self.name

    def update(self, *args):
        super(MenuButton, self).update(*args)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) or self.selected:
            self.image = self.hover_image
        else:
            self.image = self.def_image


class TopMenu(Container):
    def __init__(self, ui, focus=0):
        super(TopMenu, self).__init__()
        offer = 30, 19
        w, o_w = 53, 20

        global menu_data
        for menu in menu_data:
            event = []
            if menu['name'] == "Exit":
                event.append(ui.exit)
            btn = MenuButton(menu['btn_id'], menu['name'], menu['title'], event)
            if menu['content']:
                btn.event.insert(0, self.clear_select)
                btn.event.append(ui.show_content)
            btn.rect.topleft = offer[0] + (o_w + w) * menu['id'], offer[1]
            if menu["id"] == focus:
                btn.selected = True
            self.add(btn)

    def clear_select(self):
        for sp in get_game().uiGroup.sprites():
            if isinstance(sp, MenuButton):
                sp.selected = False


class SysUI(UIBase):
    def __init__(self):
        super(UIBase, self).__init__()
        self.game = gl.get_value("Game")

        self.add(Label(1, getImage(resourcePath + "image/sys_background.png")))
        self.add(TopMenu(self))

        self.layers = self.create_layers()
        self.add(self.current_content())

    def create_layers(self):
        layers = []
        for menu in menu_data:
            if menu['content']:
                content = eval(menu["name"] + '()')
                layers.append(content)
        return layers

    def current_content(self):
        for layer in self.layers:
            if layer.__class__.__name__ is selected:
                return layer

    def show_content(self):
        empty_ui()
        self.remove(self.layers)
        content = self.current_content()
        if content:
            self.add(content)
        add_ui(self)

    def exit(self):
        global selected
        selected = "Person"
        empty_ui()
        from Scripts.UI.MapUI import MapUI
        add_ui(MapUI())
        play()
