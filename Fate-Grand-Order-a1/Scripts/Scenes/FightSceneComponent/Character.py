from transitions import Machine

from Core.Game.AnimateSprite import AnimateSpirte
from Core.Game.function import get_game


class Character(AnimateSpirte):
    def __init__(self, name, data, skills, pos, clip=False):
        super(Character, self).__init__(data, clip)
        self.name = name
        self.skills = skills
        states = []
        for item in data:
            states.append(item['name'])
        initial = states[0]
        transitions = [
            {"trigger": "arts_act", "source": "stand", "dest": "arts"},
            {"trigger": "buster_act", "source": "stand", "dest": "buster"},
            {"trigger": "quick_act", "source": "stand", "dest": "quick"},
            {"trigger": "ex_act", "source": "stand", "dest": "ex"},
            {"trigger": "stand_act", "source": "arts", "dest": "stand"},
            {"trigger": "stand_act", "source": "buster", "dest": "stand"},
            {"trigger": "stand_act", "source": "quick", "dest": "stand"},
            {"trigger": "stand_act", "source": "ex", "dest": "stand"},
        ]
        Machine(self, states, initial, transitions)
        self.pos = pos
        self.set_animate("stand", 0, pos)


class Servant(Character):
    def __init__(self, name, data, cards, skills, pos):
        super(Servant, self).__init__(name, data, skills, pos)
        self.cards = cards

    def hit(self):
        scene = get_game().scene
        scene.servant_hit(3)

    def animate_arts(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "arts":
            self.arts_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_quick(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "quick":
            self.quick_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_buster(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "buster":
            self.buster_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_ex(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "ex":
            self.ex_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_stand(self):
        self.stand_act()
        self.set_animate(self.state, 0, self.pos)
        self.clear_round_event()
        self.clear_time_event()
        self.reset_animate_state()


class Enemy(Character):
    def __init__(self, name, data, skills, pos):
        super(Enemy, self).__init__(name, data, skills, pos, True)

    def hit(self):
        scene = get_game().scene
        scene.enemy_hit(3)

    def animate_arts(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "arts":
            self.arts_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_quick(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "quick":
            self.quick_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_buster(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "buster":
            self.buster_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_ex(self):
        if not self.state is "stand":
            self.stand_act()
        if not self.state is "ex":
            self.ex_act()
            self.set_animate(self.state, 0, self.pos)
            self.add_time_event([{"time": 680, "event": [self.hit]}])
            self.add_round_event([{"round": 1, "event": [self.animate_stand]}])

    def animate_stand(self):
        self.stand_act()
        self.set_animate(self.state, 0, self.pos)
        self.clear_round_event()
        self.clear_time_event()
        self.reset_animate_state()
