import os, operator

from Core.Game.function import getJsonFile


class CraftItem(object):
    def __init__(self, platform, createItemID, materials):
        super(CraftItem, self).__init__()
        self.platform = int(platform)
        self.itemID = int(createItemID)
        self.materials = []
        for material in materials:
            mate = CraftItem.Material(material)
            self.materials.append(mate)

    def contains(self, item_id):
        for material in self.materials:
            if material.contains(item_id):
                return material.itemNumber
        return False

    class Material(object):
        def __init__(self, item):
            super(CraftItem.Material, self).__init__()
            self.itemID = int(item['item_id'])

        def contains(self, item_id):
            if self.itemID is item_id:
                return True
            return False


class CraftSys(object):
    def __init__(self):
        super(CraftSys, self).__init__()
        path = "Data/Craft"
        self.craftData = []
        for file in os.listdir(path):
            data = getJsonFile(path + "/" + file)
            for _data in data:
                craft = CraftItem(_data['platform'], _data['item_id'], _data['material'])
                self.craftData.append(craft)
        self.platform_items = []
        self.package_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def add_creaft_items(self, item_id):
        self.platform_items.append(item_id)

    def platformContains(self, platform):
        list = []
        for craft in self.craftData:
            if (craft.platform is platform):
                list.append(craft)
        return list

    def craftContains(self, item_id):
        list = []
        for craft in self.craftData:
            if (craft.itemID is item_id):
                list.append(craft)
        return list

    def materialContains(self, item_id):
        list = []
        for craft in self.craftData:
            for material in craft.materials:
                if material.contains(item_id):
                    list.append(craft)
        return list

    def getCraft(self):
        platform_data = []
        for item in self.platform_items:
            _data = {"item_id": item}
            platform_data.append(_data)
        platform_data = sorted(platform_data, key=operator.itemgetter('item_id'))
        craft_data = []
        for craft in self.craftData:
            data = []
            for material in craft.materials:
                _data = {"item_id": material.itemID}
                data.append(_data)
            _data = {"craft": craft, "material": data}
            craft_data.append(_data)
        for craft in craft_data:
            if sorted(craft['material'], key=operator.itemgetter('item_id')) == platform_data:
                return craft['craft']
        return None
