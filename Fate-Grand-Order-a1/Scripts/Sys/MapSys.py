# coding=utf-8
from transitions import Machine

from Core.Game.function import toast


class MapSys(object):
    def __init__(self, servant):
        super(MapSys, self).__init__()
        self.servant = servant

        self.player_can_move_speed = self.default_move_speed = 1
        self.player_see = self.servant.see
        self.player_move_type = self.servant.movetype
        self.round = 0
        self.turn = self.servant.move
        self.move_num = self.player_move_num = 60

        states = ["player", "enemy"]
        transitions = [
            {"trigger": "over", "source": "player", "dest": "enemy"},
            {"trigger": "over", "source": "enemy", "dest": "player"}
        ]
        Machine(model=self, states=states, transitions=transitions, initial='player')

    def pass_turn(self):
        self.turn -= 1

    def next_turn(self, move_speed=None):
        if move_speed:
            self.player_can_move_speed = move_speed
        else:
            self.player_can_move_speed = self.default_move_speed

    def reduce_move(self, num):
        self.move_num -= num

    def can_move(self):
        if self.move_num <= 0 or not self.state is "player":
            return False
        return True

    def enemy_ai(self):
        print '1212'

    def over_turn(self):
        self.over()
        if self.state is "player":
            self.move_num = self.player_move_num
            toast(u'玩家回合')
        else:
            self.enemy_ai()
            toast(u'敌人回合')
