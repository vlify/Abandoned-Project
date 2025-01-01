# coding=utf-8
import pygame

from Scripts.Type import ProfessionType
from Scripts.Type import RaceType


class Base:
    def __init__(self, data):
        self.stamina = data['stamina']
        self.strength = data['strength']
        self.agile = data['agile']
        self.intelligence = data['intelligence']
        self.spirit = data['spirit']
        self.memory = data['memory']
        self.rule = data['rule']


class UpBase:
    def __init__(self, data):
        self.stamina = data['stamina']
        self.strength = data['strength']
        self.agile = data['agile']
        self.intelligence = data['intelligence']
        self.spirit = data['spirit']
        self.memory = data['memory']
        self.rule = data['rule']


class Element:
    def __init__(self, data):
        self.fire = data['fire']
        self.water = data['water']
        self.thunder = data['thunder']
        self.wind = data['wind']
        self.earth = data['earth']
        self.light = data['light']
        self.dark = data['dark']


class Fight:
    def __init__(self, data):
        self.speed = data['speed']
        self.parry = data['parry']
        self.dodge = data['dodge']
        self.crit = data['crit']
        self.combo = data['combo']
        self.speed_resist = data['speed_resist']
        self.chanting = data['chanting']
        self.strong_chanting = data['strong_chanting']
        self.heal = data['heal']
        self.notisdead = data['notisdead']


class Equip:
    def __init__(self, data):
        self.head = data['head']
        self.body = data['body']
        self.foot = data['foot']
        self.weapon = data['weapon']
        self.offhand = data['offhand']


class FeatureEffect:
    def __init__(self, effect):
        pass


class Feature:
    def __init__(self, data):
        self.name = data['name']
        self.des = data['des']
        self.effects = []
        for effect in data['effect']:
            self.effects.append(FeatureEffect(effect))


# item 为赠送属性，舔选 物品id:物品num 即可往背包中添加num数量的物品
# features 为特性列表，填写 特性id 即可增加人物的特性效果
class Character(object):
    def __init__(self, data, level):
        super(Character, self).__init__()
        self.level = level
        self.data = data

        self.id = id
        self.name = self.data['name']
        self._sex = self.data['sex']
        if self.data['sex'] == 0:
            sex = u'不明'
        elif self.data['sex'] == 1:
            sex = u'女'
        else:
            sex = u'男'
        self.sex = sex
        self.profession = self.data['profession'].upper()
        self.profession_id = getattr(ProfessionType, self.data['profession'].upper())

        self.race = getattr(RaceType, self.data['race'])
        self.ract_str = getattr(RaceType, "str_" + self.data['race'])

        self.p_atk = self.get_p_atk_num()
        self.m_atk = self.get_m_atk_num()
        self.defance = self.get_defance_num()
        self.hp = self.get_hp_num()
        self.base = Base(self.data['base'])
        self.upbase = Base(self.data['up'])


    def get_defance_num(self):
        pass

    def get_hp_num(self):
        pass

    def get_p_atk_num(self):
        return 1000

    def get_m_atk_num(self):
        return 2000
