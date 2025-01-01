from Scripts.Model.Base.Card import Card


class EnemySkill(Card):
    def __init__(self, cardType, power):
        super(EnemySkill, self).__init__(cardType, power)
