import pygame

from Scripts.Scenes.TestScene4Component.ItemButton import CreaftButton, CreatedButton


class Platform(pygame.sprite.LayeredUpdates):
    def __init__(self, pos, blockSize=[25, 25]):
        super(Platform, self).__init__()
        self.pos = pos
        self.items = []
        size = blockSize
        offer_x = 5
        offer_y = 5
        row = 7
        col = 2
        for y in range(col):
            for x in range(row):
                pos = self.pos[0] + x * (size[0] + offer_x), self.pos[1] + size[1] + (size[1] + offer_y) * y + 15
                item_btn = CreaftButton(pos, 0, 0, size)
                self.items.append(item_btn)
        self.add(self.items)
        pos = (size[0] * row + offer_x * (row - 1)) / 2 - size[0] / 2 + self.pos[0], self.pos[1]
        self.createdItem = CreatedButton(pos, 0, 0, size)
        self.add(self.createdItem)
