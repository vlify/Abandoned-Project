import pygame

from Core.Game.function import get_system
from Scripts.Scenes.TestScene4Component.ItemButton import ItemButton
from Scripts.UI.PageUI import PageSprite


class Package(pygame.sprite.LayeredUpdates):
    def __init__(self, pos, col=7, row=5 , blockSize=[25,25]):
        super(Package, self).__init__()
        size = blockSize
        offer_x = 5
        offer_y = 5
        self.pos = pos
        package = get_system().package_items
        package_index = -1
        self.items = []
        for y in range(row):
            for x in range(col):
                pos = self.pos[0] + x * (size[0] + offer_x), self.pos[1] + (size[1] + offer_y) * y
                package_index += 1
                if package_index >= len(package):
                    item_id = 0
                else:
                    item_id = package[package_index]
                number = 1
                self.items.append(ItemButton(pos, item_id, number, size))
        self.add(self.items, layer="package")
        pageSp = PageSprite(col * row, len(package),
                            [self.pos[0] + (100 / 2), self.pos[1] + row * size[1] + offer_y * row + 10])
        self.add(pageSp)
