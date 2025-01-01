from Core.Game.Item import ItemBase
from Core.Game.function import create_surface, get_system, get_scene
from Core.UI.UIBase import ScaleButton
from conf import WHITE


class ItemButton(ScaleButton):
    def __init__(self, pos, item_id=0, number=0, size=[25, 25], scale=1.1, event=[]):
        if item_id is 0:
            surface = create_surface(size, WHITE, alpha=50)
        else:
            surface = ItemBase.get_item_icon(item_id, size)
        super(ItemButton, self).__init__(surface, pos, scale, event=[self.refrush])
        self.item_id = item_id
        self.num = number
        self.size = size

    def refrush(self):
        if self.item_id:
            get_system().platform_items.append(self.item_id)
            get_system().package_items.remove(self.item_id)
        self._refrush()

    def _refrush(self):
        package_items = get_system().package_items
        platform_items = get_system().platform_items
        for index, item in enumerate(get_scene().package.items):
            if index < len(package_items):
                item.item_id = package_items[index]
            else:
                item.item_id = 0
        for index, item in enumerate(get_scene().platform.items):
            if index < len(platform_items):
                item.item_id = platform_items[index]
            else:
                item.item_id = 0
        craft = get_system().getCraft()
        print craft
        if craft:
            get_scene().platform.createdItem.item_id = craft.itemID
        else:
            get_scene().platform.createdItem.item_id = 0

    def update(self, *args):
        super(ItemButton, self).update()
        if self.item_id is 0:
            surface = create_surface(self.size, WHITE, alpha=50)
        else:
            surface = ItemBase.get_item_icon(self.item_id, self.size)
        self.image = surface


class CreaftButton(ItemButton):
    def __init__(self, pos, item_id=0, number=0, size=[25, 25], scale=1.1):
        super(CreaftButton, self).__init__(pos, item_id, number, size, scale, event=[self.refrush])

    def refrush(self):
        if self.item_id:
            get_system().package_items.append(self.item_id)
            get_system().platform_items.remove(self.item_id)
        self._refrush()


class CreatedButton(ItemButton):
    def __init__(self, pos, item_id=0, number=1, size=[25, 25], scale=1.1, event=[]):
        super(CreatedButton, self).__init__(pos, item_id, number, size, scale, event=[self.refrush])

    def refrush(self):
        get_system().platform_items = []
        get_system().package_items.append(self.item_id)
        self._refrush()
