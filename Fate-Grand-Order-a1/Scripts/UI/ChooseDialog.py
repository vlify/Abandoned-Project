# coding=utf-8
import pygame

from Core.Game.function import singleText, centerX, create_surface, getImage, MultiText, resolve_image, centerXY, click, \
    closeDialog, play, jumpScene
from Scripts.function import empty_enemy_team
from conf import WHITE, windowSize, BLACK, resourcePath, fontYouyuanPath


class DialogButton(pygame.sprite.Sprite):
    def __init__(self, dialog, info, width):
        super(DialogButton, self).__init__()
        self.dialog = dialog
        self.text = info['text']
        self.def_image = singleText(self.text, WHITE)
        self.hover_image = singleText(self.text, [184, 163, 48])
        self.image = self.def_image
        self.rect = self.image.get_rect()
        self.rect.w = width
        self.rect.x = centerX(self.rect.w)
        self.effects = info['effect'].split("|")

    def update(self):
        mouse = pygame.mouse
        if self.rect.collidepoint(mouse.get_pos()):
            self.image = self.hover_image
        else:
            self.image = self.def_image
        if click(self.rect):
            for effect in self.effects:
                ef = effect.split(":")
                if ef[0] == "story":
                    self.story(ef[1])
                if ef[0] == "exit":
                    play()
                if ef[0] == "fight":
                    from Scripts.Scenes.FightScene import FightScene
                    jumpScene(FightScene())
                    play()
            closeDialog(self.dialog)
            empty_enemy_team()
            pygame.event.wait()

    def story(self, story_id):
        print story_id

    def instrace(self):
        pass


class ChooseDialog(pygame.sprite.OrderedUpdates):
    def __init__(self, info, thumb=0, mask=230):
        super(ChooseDialog, self).__init__()
        w = 770
        h = 0
        wl = 820
        lh = 23

        msg = info['msg']
        btns = info['btns']

        if mask:
            sp_mask = pygame.sprite.Sprite()
            sp_mask.image = create_surface(windowSize, BLACK, mask)
            sp_mask.rect = sp_mask.image.get_rect()
            self.add(sp_mask)

        self.bg = pygame.sprite.Sprite()
        self.bg.image = create_surface([wl, h], alpha=0)
        self.bg.rect = self.bg.image.get_rect()
        self.add(self.bg)

        self.thumb = pygame.sprite.Sprite()
        self.thumb.image = getImage(resourcePath + "image/dialog/" + str(thumb) + ".png", [w, 150], type=1)
        self.thumb.rect = self.thumb.image.get_rect()
        self.add(self.thumb)
        h += self.thumb.rect.h

        self.msg = pygame.sprite.Sprite()
        self.msg.image = MultiText(msg, 60, WHITE, w, font=fontYouyuanPath)
        self.msg.rect = self.msg.image.get_rect()
        self.add(self.msg)
        h += self.msg.rect.h

        h += len(btns) * lh + 70
        self.bg.image = resolve_image(resourcePath + "image/map_dialog_background.png", [wl, h], 40)
        self.bg.rect.h = h
        self.bg.rect.topleft = centerXY(self.bg.rect.size)
        self.thumb.rect.topleft = centerX(self.thumb.rect.w), self.bg.rect.y + 30
        self.msg.rect.topleft = centerX(self.msg.rect.w), self.bg.rect.y + 190

        self.height = 0
        for key, btn in enumerate(btns):
            button = DialogButton(self, btn, w)
            button.rect.y += 10 + self.msg.rect.y + self.msg.rect.h + lh * key
            self.add(button)

    def destory(self):
        pass
