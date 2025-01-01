import math


class Progress(object):
    def __init__(self, current, max):
        super(Progress, self).__init__()
        self.current = current
        self.max = max
        self.point = float(self.current) / float(self.max) * 100.0

    def getPoint(self, type=2):
        if 0 == type:
            return int(math.ceil(float(self.current) / float(self.max) * 100.0))
        else:
            return round(float(self.current) / float(self.max) * 100.0, type)
