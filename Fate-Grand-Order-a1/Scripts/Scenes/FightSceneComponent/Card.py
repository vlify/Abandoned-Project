from Core.DataType.Delay import Delay
from Core.Game.function import create_surface, singleText, get_mTime, get_system
from Core.UI.UIBase import Button
from Scripts.Type import CardType
from conf import WHITE

UP = 1
DOWN = 2


class Card(Button):
    def __init__(self, id, name, event, cardData, pos):
        super(Card, self).__init__(id, name, event)
        size = 140, 200
        self.surface = create_surface(size, WHITE)
        self.rect = self.surface.get_rect()
        self.servant = cardData['servant']
        self.card = cardData['card']
        if self.card.type is CardType.BUSTER:
            surface = singleText(self.servant.name + "Buster", size=20)
        elif self.card.type is CardType.ARTS:
            surface = singleText(self.servant.name + "Arts", size=20)
            pass
        elif self.card.type is CardType.QUICK:
            surface = singleText(self.servant.name + "Quick", size=20)
            pass
        self.surface.blit(surface, [0, 0])
        self.image = self.surface
        self.rect.topleft = pos
        self.move_type = DOWN
        self.max_y = self.rect.y + 30
        self.min_y = self.rect.y - 30
        self.delay = Delay(80)
        self.event.append(self.set_system_action_card_list)

    def set_system_action_card_list(self):
        data = {"card": self, "over": False}
        if not data in get_system().action_cards_list:
            index = get_system().action_cards_list.index(None)
            get_system().action_cards_list[index] = data
        else:
            index = get_system().action_cards_list.index(data)
            get_system().action_cards_list[index] = None
        if not None in get_system().action_cards_list:
            get_system().action_servant_round()

    def update(self, *args):
        super(Card, self).update()
        self.delay.update(get_mTime())
        if self.delay.loopRound(1):
            if self.move_type is UP:
                self.rect.y += 1
            if self.move_type is DOWN:
                self.rect.y -= 1
        if self.rect.y >= self.max_y:
            self.move_type = DOWN
        if self.rect.y <= self.min_y:
            self.move_type = UP
