# coding=utf-8
from random import randint, sample

import pygame

from Core.DataType.Delay import Delay
from Core.Game.Scene import Scene
from Core.Game.function import getImage, getJsonFile, get_game, get_system, set_system, get_mTime
from Scripts.Model.Base.Card import BusterCard, QuickCard, ArtsCard
from Scripts.Model.Base.EnemySkill import EnemySkill
from Scripts.Scenes.FightSceneComponent.Bar import Bar
from Scripts.Scenes.FightSceneComponent.Character import Servant, Enemy
from Scripts.Scenes.FightSceneComponent.HitSprite import HitSprite
from Scripts.Sys.FightSys import FightSys
from Scripts.Type import CardType
from Scripts.function import empty_ui
from conf import servantPath, resourcePath


class FightScene(Scene):
    def __init__(self):
        super(FightScene, self).__init__()
        empty_ui()
        bg = pygame.sprite.Sprite()
        bg.image = getImage(resourcePath + "image/demo_fight.png")
        bg.rect = bg.image.get_rect()
        self.add(bg)
        surface = getImage(servantPath + "00/image/animate.png", type=1)
        data_s1 = [
            {"name": "stand", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/stand.json")},
            {"name": "arts", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/arts.json")},
            {"name": "buster", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/buster.json")},
            {"name": "quick", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/quick.json")},
            {"name": "ex", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/ex.json")}
        ]
        data_e1 = [
            {"name": "stand", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/stand.json")},
            {"name": "arts", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/arts.json")},
            {"name": "buster", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/buster.json")},
            {"name": "quick", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/quick.json")},
            {"name": "ex", "surface": surface, "jsonData": getJsonFile(servantPath + "00/animate/ex.json")}
        ]
        servant_cards = [BusterCard(), BusterCard(), BusterCard(), QuickCard(), ArtsCard()]
        servant_skills = ['ARTS', 'BUSTER', 'QUICK']
        self.servant_team = [
            Servant("s1", data_s1, servant_cards, servant_skills, [200, 450]),
            Servant("s2", data_s1, servant_cards, servant_skills, [320, 450]),
            Servant("s3", data_s1, servant_cards, servant_skills, [440, 450])
        ]
        self.add(self.servant_team)
        enemy_skills = [
            EnemySkill(CardType.BUSTER, 100),
            EnemySkill(CardType.ARTS, 100),
            EnemySkill(CardType.QUICK, 100),
            EnemySkill(CardType.EX, 100)
        ]
        self.enemy_team = [
            Enemy("e1", data_e1, enemy_skills, [800, 450]),
            Enemy("e2", data_e1, enemy_skills, [920, 450]),
            Enemy("e3", data_e1, enemy_skills, [1040, 450])
        ]
        self.add(self.servant_team, self.enemy_team)

        set_system(FightSys(self.servant_team, self.enemy_team))

        self.hp = 656846
        self.servant_bar = Bar(self.hp, self.hp, [320, 600])
        self.enemy_bar = Bar(self.hp, self.hp, [800, 600])
        self.add(self.servant_bar, self.enemy_bar)

        self.delay = Delay(100)
        self.hit_list = []

        get_system().action_shuffle()

    def update(self, *args):
        super(FightScene, self).update()
        self.delay.update(get_game().mTime)
        if self.hit_list and self.delay.loopRound(1):
            hit = self.hit_list[0]
            self.add(hit, layer="hit")
            self.hit_list.remove(hit)
            self.reduce_hp(hit.value)
        if get_system().state is "servant_round" or get_system().state is "enemy_round":
            if get_system().state is "servant_round":
                action = get_system().action_cards_list[get_system().card_index]
                char = action['card'].servant
                action_act = action['card'].card
            else:
                action = get_system().enemy_skill[get_system().card_index]
                char = action['enemy']
                action_act = action['skill']
            if action_act.type is CardType.BUSTER:
                actionName = "buster"
            elif action_act.type is CardType.ARTS:
                actionName = "arts"
            elif action_act.type is CardType.QUICK:
                actionName = "quick"
            else:
                actionName = "ex"
            time = char.get_animate_duration(actionName)
            get_system().animate_time += get_mTime()
            if not char.state is "buster" and action_act.type is CardType.BUSTER:
                char.animate_buster()
            if not char.state is "arts" and action_act.type is CardType.ARTS:
                char.animate_arts()
            if not char.state is "quick" and action_act.type is CardType.QUICK:
                char.animate_quick()
            if not char.state is "ex" and action_act.type is CardType.EX:
                char.animate_ex()
            if get_system().animate_time >= time:
                get_system().animate_time = 0
                get_system().card_index += 1
                if get_system().card_index >= len(get_system().action_cards_list):
                    get_system().action_cards_list = [None, None, None]
                    get_system().card_index = 0
                    if get_system().state is "servant_round":
                        get_system().action_enemy_ai()
                    else:
                        get_system().loop()

    def servant_hit(self, hit_number):
        self.hit_list = []
        for x in range(hit_number):
            hit_number = randint(1, 10000)
            hs = HitSprite(hit_number, centerPos=[get_system().servant_target.rect.centerx,
                                                  get_system().servant_target.rect.centery - 50])
            self.hit_list.append(hs)

    def enemy_hit(self, hit_number):
        self.hit_list = []
        enemy = sample(self.servant_team, 1)[0]
        for x in range(hit_number):
            hit_number = randint(1, 10000)
            hs = HitSprite(hit_number, centerPos=[enemy.rect.centerx,
                                                  enemy.rect.centery - 50])
            self.hit_list.append(hs)

    def reduce_hp(self, offer_hp):
        hp = self.enemy_bar.hp - offer_hp
        self.set_hp(hp)

    def set_hp(self, hp):
        self.enemy_bar.set_hp(hp)
