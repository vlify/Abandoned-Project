# coding=utf-8
from Core.Game.function import singleText, floatRight, bottom, get_system
from Core.UI.UIBase import Button
from conf import WHITE


class SelectCardsButton(Button):
    def __init__(self):
        super(SelectCardsButton, self).__init__(0, "select_cards_button", [])
        self.cards = get_system().current_cards
        self.surface = singleText(u"选择行动卡", WHITE)
        self.image = self.surface.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = floatRight(self.rect.w) - 10, bottom(self.rect.h) - 10

        self.event.append(get_system().select_cards)
        self.event.append(get_system().action_servant_draw)
        self.event.append(self.kill)
