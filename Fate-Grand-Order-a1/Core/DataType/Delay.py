class Delay(object):
    def __init__(self, second=1000):
        super(Delay, self).__init__()
        self.time = 0
        self.second = 0
        self.maxSecond = second
        self.round = 0
        self.delayOpen = True

    def delayClear(self):
        self.round = 0
        self.time = 0
        self.second = 0
        self.delayOpen = True

    def delayClose(self):
        self.round = 0
        self.time = 0
        self.second = 0
        self.delayOpen = False

    def update(self, mTime):
        if self.delayOpen:
            self.second += mTime
            if self.second >= self.maxSecond:
                self.second = 0
                # print "1 second"
            self.time += mTime
            if self.time >= self.maxSecond:
                self.time = 0
                self.round += 1
                # print "{0} times after ,round: {1}".format(str(delty), str(self.round))

    def atRound(self, round):
        if self.round >= round:
            self.delayClose()
            return True
        else:
            return False

    def loopRound(self, round):
        if self.round >= round:
            self.delayClear()
            return True
        else:
            return False
