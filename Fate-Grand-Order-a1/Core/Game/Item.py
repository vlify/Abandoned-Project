import os

from Core.Game.function import getImage, get_item_data
from Core.Type import ItemType, UseArea
from conf import resourcePath


class ItemBase(object):
    def __init__(self, itemData):
        super(ItemBase, self).__init__()
        self.id = itemData['id']
        self.name = itemData['name']
        self.description = itemData['description']
        self.price = itemData['price']
        self.useArea = getattr(UseArea, itemData['useArea'].upper())
        self.able = bool(itemData['able'])
        self.category = itemData['category']
        self.type = []
        self.effect = []
        for type in itemData['type']:
            self.type.append(getattr(ItemType, type.upper()))
        for effect in itemData['effect']:
            self.effect.append(effect)
        self.iconPath = resourcePath + "image/icon/" + itemData['icon'] + ".png"
        if not os.path.exists(self.iconPath):
            self.iconPath = resourcePath + "image/icon/" + itemData['icon'] + ".jpg"
        self.icon = getImage(self.iconPath, type=1)

    @staticmethod
    def get_item_icon(item_id, size):
        return getImage(get_item_data(item_id).iconPath, size, type=1)


class Weapon(ItemBase):
    def __init__(self, data):
        super(Weapon, self).__init__(data)


class Armor(ItemBase):
    def __init__(self, data):
        super(Armor, self).__init__(data)
