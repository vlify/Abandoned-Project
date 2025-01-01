from Scripts.Type import CardType


class Card(object):
    def __init__(self, type, power):
        super(Card, self).__init__()
        self.type = type
        self.power = float(power)
        if self.type is CardType.ARTS:
            pass
        elif self.type is CardType.BUSTER:
            pass
        elif self.type is CardType.QUICK:
            pass
        elif self.type is CardType.EX:
            pass
        else:
            print('none cardtype')


class BusterCard(Card):
    def __init__(self):
        super(BusterCard, self).__init__(CardType.BUSTER, 1.2)


class ArtsCard(Card):
    def __init__(self):
        super(ArtsCard, self).__init__(CardType.ARTS, 1)


class QuickCard(Card):
    def __init__(self):
        super(QuickCard, self).__init__(CardType.QUICK, 0.8)


class ExCard(Card):
    def __init__(self):
        super(ExCard, self).__init__(ExCard, 1)
