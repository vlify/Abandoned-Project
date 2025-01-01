# coding=utf-8
'''测试用'''

class Delay(object):
    def __init__(self, time, i):
        super(Delay, self).__init__()
        self.id = i
        self.i = 0
        self.round = 0
        self.run = False
        self.time = time

    @classmethod
    def create(cls, index):
        return cls(1000, index)

    def update(self, dt):
        if self.run:
            self.i += dt
            if self.i > self.time:
                self.round += 1
        print self.i

    def atRound(self, round):
        if self.round >= round:
            return True
        else:
            return False

    def reset(self):
        self.i = 0
        self.round = 0

    def replay(self):
        self.reset()
        self.play()

    def over(self):
        self.reset()
        self.run = False

    def play(self):
        self.run = True


class _Animate(object):
    def __init__(self, delay_list):
        super(_Animate, self).__init__()
        self.delay_list = delay_list
        self.index = 0
        self.time = 0
        self.delay = self.delay_list[self.index]
        self.delay.play()
        self.play = True
        self.round = 0
        self.loop = 1
        self.finish = False

    def atRound(self, round):
        if self.round >= round:
            return False
        else:
            return True

    def reset(self):
        self.round = 0
        self.index = 0
        self.finish = False

    def over(self):
        self.reset()
        self.stop()

    def stop(self):
        self.play = False
        self.finish = True

    def update(self):
        if self.play:
            self.delay.update(17)
            if self.delay.atRound(1):
                self.delay.over()
                self.index += 1
                if self.index > len(self.delay_list) - 1:
                    self.index = 0
                    self.round += 1
                self.delay = self.delay_list[self.index]
                self.delay.replay()
            if self.round >= self.loop:
                self.stop()
