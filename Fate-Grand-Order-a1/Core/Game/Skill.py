# coding=utf-8
'''
cd 为0 可被连击触发
'''
from Core.Game.Effect import Effect
from Core.Type import EffectType, UseArea


class Skill(object):
    def __init__(self, name, cd, effects=None, target_num=1):
        super(Skill, self).__init__()
        self.name = name
        self.cd = cd + 1
        self.max_cd = cd + 1
        self.is_cd = False
        self.target_num = target_num
        if effects is None:
            effects = [Effect('普通攻击', 1, EffectType.PHYSICAL_DAMAGE, UseArea.TARGET_ONE)]
        self.effects = effects

    def reduce_cd(self, val=1):
        if self.is_cd:
            self.cd -= val
            if self.cd <= 0:
                self.is_cd = False
                self.cd = self.max_cd
