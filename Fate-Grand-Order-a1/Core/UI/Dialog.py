import pygame

from Core.conf import resourcePath


class CloseButton(pygame.sprite.Sprite):
    def __init__(self, dialog):
        super(CloseButton, self).__init__()
        from Core.Game.function import getImage
        self.image = getImage(resourcePath + 'image/dialog_close_button.png', [15, 15], 1)
        self.rect = self.image.get_rect()

        self.dialog = dialog

    def update(self):
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if mouse[0] and self.rect.collidepoint(pos):
            from Core.Game.function import closeDialog
            closeDialog(self.dialog)
            pygame.event.wait()


class Dialog(pygame.sprite.LayeredUpdates):
    def __init__(self, name, surface, pos, size, backgound):
        super(Dialog, self).__init__()
        self.name = name
        bg = pygame.sprite.Sprite()
        if backgound:
            bg.image = backgound
        else:
            bg.image = pygame.Surface(size)
        bg.rect = bg.image.get_rect()
        bg.rect.topleft = pos

        closeBtn = CloseButton(self)
        closeBtn.rect.topleft = size[0] - 3, pos[1] - 15

        bg.image.blit(surface, [0, 0])
        self.add(bg)
        self.add(closeBtn)

    def destory(self):
        pass
