# coding=utf-8

# 真实伤害
TRUE_DAMAGE = 1
# 物理伤害
PHYSICAL_DAMAGE = 2
# 魔法伤害
MAGIC_DAMAGE = 3
# 治疗
HEAL = 4
# 回复物理护甲
HEAL_PHYSICAL_ARMOR = 5
# 回复魔法护甲
HEAL_MAGIC_ARMOR = 6

# 每回合增加真实伤害
BUFF_TRUE_DAMAGE = 7
# 每回合增加物理伤害
BUFF_PHYSICAL_DAMAGE = 8
# 每回合增加魔法伤害
BUFF_MAGIC_DAMAGE = 9

# 每回合治疗
BUFF_HEAL = 10
# 治疗增量
BUFF_OFFSET_HEAL = 11
# 每回合回复物理护甲
BUFF_HEAL_PHYSICAL_ARMOR = 12
# 每回合回复魔法护甲
BUFF_HEAL_MAGIC_ARMOR = 13

# 抵消 真实伤害
BUFF_OFFSET_TRUE_DAMAGE = 14
# 抵消 物理伤害
BUFF_OFFSET_PHYSICAL_DAMAGE = 15
# 抵消 魔法伤害
BUFF_OFFSET_MAGIC_DAMAGE = 16

# 免疫眩晕
BUFF_VERTIGO = 17
# 免疫移动
BUFF_MOVE = 18
# 增强属性
BUFF_BASE = 19

# 每回合 真实伤害
DOT_DAMAGE = 20
# 每回合 物理伤害
DOT_DAMAGE_PHYSICAL = 21
# 每回合 魔法伤害
DOT_DAMAGE_MAGIC = 22

# 抑制 治疗
DOT_OFFSET_HEAL = 23
# 附加 真实伤害
DOT_TRUE_DAMAGE = 26
# 附加 物理伤害
DOT_PHYSICAL_DAMAGE = 27
# 附加 魔法伤害
DOT_MAGIC_DAMAGE = 28

# 眩晕
DOT_VERTIGO = 29
# 移动限制
DOT_MOVE = 30
# 减少属性
DOT_BASE = 31


def is_buff(type):
    if type == BUFF_TRUE_DAMAGE or type == BUFF_PHYSICAL_DAMAGE or type == BUFF_MAGIC_DAMAGE or type == BUFF_HEAL \
            or type == BUFF_OFFSET_HEAL or type == BUFF_HEAL_PHYSICAL_ARMOR or type == BUFF_HEAL_MAGIC_ARMOR or \
            type == BUFF_OFFSET_TRUE_DAMAGE or type == BUFF_OFFSET_PHYSICAL_DAMAGE or type == BUFF_OFFSET_MAGIC_DAMAGE \
            or type == BUFF_VERTIGO or type == BUFF_MOVE or type == BUFF_BASE:
        return True
    return False


def is_dot(type):
    if type == DOT_DAMAGE or type == DOT_DAMAGE_PHYSICAL or type == DOT_DAMAGE_MAGIC or type == DOT_OFFSET_HEAL or \
            type == DOT_TRUE_DAMAGE or type == DOT_PHYSICAL_DAMAGE or type == DOT_MAGIC_DAMAGE or type == DOT_VERTIGO or \
            type == DOT_MOVE or type == DOT_BASE:
        return True
    return False


def not_buff_dot(type):
    if not is_buff(type) or not is_dot(type):
        return True
    return False
