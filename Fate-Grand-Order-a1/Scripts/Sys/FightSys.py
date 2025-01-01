# coding=utf-8
import random

from transitions import Machine

from Core.Game.function import get_scene, centerY, singleText, get_system
from Scripts.Scenes.FightSceneComponent.Card import Card
from Scripts.Scenes.FightSceneComponent.MaskSprite import MaskSprite
from Scripts.Scenes.FightSceneComponent.SelectCardsButton import SelectCardsButton
from Scripts.Scenes.FightSceneComponent.SkillButton import SkillButton
from conf import WHITE


class FightSys(object):
    def __init__(self, servant_team, enemy_team):
        super(FightSys, self).__init__()
        self.servant_team = servant_team
        self.enemy_team = enemy_team

        self.action_order = []
        self.servant_target = self.enemy_team[0]
        self.card_list = self.create_servant_cards()
        self.current_cards = []
        self.draw_cards = []
        self.current_card_index = 0
        self.card_index = 0
        self.action_cards_list = [None, None, None]
        self.animate_time = 0

        self.enemy_skill = []

        states = ['start', 'shuffle', "skill", "servant_draw", "servant_round", "enemy_ai", "enemy_round", "success",
                  "fail"]
        initial = "start"
        transitions = [
            {"trigger": "action_shuffle", "source": "start", "dest": "shuffle"},
            {"trigger": "action_skill", "source": "shuffle", "dest": "skill"},
            {"trigger": "action_servant_draw", "source": "skill", "dest": "servant_draw"},
            {"trigger": "action_servant_round", "source": "servant_draw", "dest": "servant_round"},
            {"trigger": "action_enemy_ai", "source": "servant_round", "dest": "enemy_round"},
            {"trigger": "action_success", "source": "servant_round", "dest": "success"},
            {"trigger": "action_success", "source": "enemy_round", "dest": "success"},
            {"trigger": "action_fail", "source": "servant_round", "dest": "fail"},
            {"trigger": "action_fail", "source": "enemy_round", "dest": "fail"},
            {"trigger": "loop", "source": "enemy_round", "dest": "shuffle"}
        ]
        Machine(self, states, initial, transitions, after_state_change="enter_state")
        self.mask = MaskSprite()

    def enter_state(self):
        if self.state is "skill":
            _btns = ['ARTS', 'BUSTER', 'QUICK']
            btns = []
            for i, btn in enumerate(_btns):
                surface = singleText(btn, WHITE)
                pos = 100 + (surface.get_rect().w + 40) * i, 650
                btns.append(SkillButton(surface, pos, 1.1, []))
            get_scene().add(btns, layer="skills")
            btns[0].event.append(self.servant_team[0].animate_arts)
            btns[1].event.append(self.servant_team[0].animate_quick)
            btns[2].event.append(self.servant_team[0].animate_buster)
        else:
            get_scene().remove_sprites_of_layer("skills")
        if self.state is "shuffle":
            self.select_cards()
            ssb = SelectCardsButton()
            get_scene().add(ssb)
            self.action_skill()
        if self.state is "servant_draw":
            get_scene().add(self.mask)
            for i, data in enumerate(self.current_cards):
                event = []
                pos = 300 + (140 + 20) * i, centerY(200) + 50
                card_sp = Card(i, "card_" + str(i), event, data, pos)
                get_scene().add(card_sp, layer="cards")
        else:
            get_scene().remove(self.mask)
            get_scene().remove_sprites_of_layer("cards")
        if get_system().state is "enemy_round":
            self.enemy_skill = []
            self.card_index = 0
            for enemy in get_system().enemy_team:
                data = {"enemy": enemy, "skill": random.sample(enemy.skills, 1)[0]}
                self.enemy_skill.append(data)

    def select_cards(self):
        if len(self.card_list) < 5:
            self.card_list = self.create_servant_cards()
        self.current_cards = random.sample(self.card_list, 5)
        for card in self.current_cards:
            self.card_list.remove(card)


    def create_servant_cards(self):
        cards = []
        for servant in self.servant_team:
            for card in servant.cards:
                data = {"servant": servant, "card": card}
                cards.append(data)
        return cards
