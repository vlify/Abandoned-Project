class Effect(object):
    def __init__(self, name, value, EffectType, UseArea):
        super(Effect, self).__init__()
        self.name = name
        self.value = value
        self.EffectType = EffectType
        self.UseArea = UseArea


class EffectRound(object):
    def __init__(self, name, value, round, EffectType, UseArea):
        super(EffectRound, self).__init__()
        self.name = name
        self.value = value
        self.EffectType = EffectType
        self.UseArea = UseArea
        self.round = round
        self.max_round = round

    def round_val(self, val=1):
        self.round -= val