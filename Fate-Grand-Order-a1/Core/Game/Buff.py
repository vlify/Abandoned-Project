from Core.Game.Effect import EffectRound
from Core.Type import EffectType


class Buff(EffectRound):
    def __init__(self, name, value, round, buff_type, UseArea):
        super(Buff, self).__init__(name, value, round, buff_type, UseArea)
        self.vertigo = False
        self.move = False
        if self.EffectType is EffectType.BUFF_VERTIGO:
            self.vertigo = True
        if self.EffectType is EffectType.BUFF_MOVE:
            self.move = True
