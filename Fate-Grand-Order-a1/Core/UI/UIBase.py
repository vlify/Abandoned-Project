import pygame

from Core.Game.function import singleText, click
from conf import WHITE


class ScaleButton(pygame.sprite.Sprite):
    def __init__(self, surface, pos, scale=1.1, event=[]):
        super(ScaleButton, self).__init__()
        self.image = surface
        self._image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.center = self.rect.center
        self.event = event
        self.scale = scale
        self.able = True

    def addEvent(self, fun, type=False):
        if not type:
            self.event.append(fun)
        else:
            self.event.insert(type, fun)

    def update(self, *args):
        super(ScaleButton, self).update()
        if click(self.rect) and self.event and self.able:
            for e in self.event:
                e()
            pygame.event.wait()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = pygame.transform.rotozoom(self._image, 0, self.scale)
        else:
            self.image = self._image
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class View(pygame.sprite.Sprite):
    def __init__(self, id, name=None):
        super(View, self).__init__()
        self.id = id
        if not name:
            self.name = "view_" + str(self.id)
        else:
            self.name = name

    def set_position(self, x, y):
        self.rect.topleft = x, y

    @classmethod
    def create_by_pos(cls, id, name, pos):
        sp = cls.__init__(id, name)
        sp.rect.topleft = pos
        return sp


class AbleView(View):
    def __init__(self, id, name=None):
        super(AbleView, self).__init__(id, name)
        self.id = id
        if not name:
            self.name = "AbleView_" + str(self.id)
        else:
            self.name = name
        self.able = True

    def update(self, *args):
        if self.able:
            super(AbleView, self).update(*args)


class Label(View):
    def __init__(self, id, surface, name=None):
        super(Label, self).__init__(id, name)
        if not name:
            self.name = "layer_" + str(self.id)
        else:
            self.name = name
        self.image = surface
        self.rect = self.image.get_rect()

    @classmethod
    def create_by_pos(cls, id, name, surface, pos):
        sp = cls(id, surface, name)
        sp.rect.topleft = pos
        return sp


class Container(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super(Container, self).__init__()


class TextView(View):
    def __init__(self, id, text, name=None):
        super(TextView, self).__init__(id, name)
        if not name:
            self.name = "text_" + str(self.id)
        else:
            self.name = name
        self.text = text
        self.image = singleText(self.text, WHITE, 24)
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.image = singleText(self.text, WHITE, 24)
        self.rect = self.image.get_rect()


class Button(AbleView):
    def __init__(self, id, name=None, event=[]):
        super(Button, self).__init__(id, name)
        if not name:
            self.name = "container_" + str(self.id)
        else:
            self.name = name
        self.event = event

    @classmethod
    def position(cls, x, y):
        cls.rect.topleft = x, y

    def update(self, *args):
        super(Button, self).update()
        if self.able and self.event and click(self.rect):
            for e in self.event:
                e()
            pygame.event.wait()


class UiSys(object):
    def __init__(self):
        super(UiSys, self).__init__()

    def get_sprite_by_name(self, name):
        arr = []
        for sp in self.sprites():
            if sp.name == name:
                arr.append(sp)
        if len(arr) == 1:
            return arr[0]
        return arr

    def get_sprite_by_id(self, id):
        arr = []
        for sp in self.sprites():
            if sp.id == id:
                arr.append(sp)
        if len(arr) == 1:
            return arr[0]
        return arr

    def all(self):
        all = []
        for sp in self.sprites():
            _sp = {"id": sp.id, "name": sp.name}
            all.append(_sp)
        return all


class UIBase(pygame.sprite.LayeredUpdates, UiSys):
    def __init__(self):
        super(UIBase, self).__init__()
        UiSys.__init__(self)

    def update(self, *args):
        super(UIBase, self).update(*args)
