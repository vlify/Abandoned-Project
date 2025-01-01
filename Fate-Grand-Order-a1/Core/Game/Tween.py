import math


class Tween(object):
    def __init__(self):
        super(Tween, self).__init__()

    def Linear(self, currentTime, begin, end, duration):
        return float(end) * float(currentTime) / float(duration) + float(begin)

    @property
    def Quad(self):
        return Quad()

    @property
    def Cubic(self):
        return Cubic()

    @property
    def Quart(self):
        return Quart()

    @property
    def Quint(self):
        return Quint()

    @property
    def Sine(self):
        return Sine()

    @property
    def Expo(self):
        return Expo()

    @property
    def Circ(self):
        return Circ()

    @property
    def Elastic(self):
        return Elastic()

    @property
    def Back(self):
        return Back()

    @property
    def Bounce(self):
        return Bounce()


class Quad(object):
    def __init__(self):
        super(Quad, self).__init__()

    def easeIn(self, t, b, c, d):
        t = float(t) / float(d)
        return float(c) * t * t + float(b)

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d)
        return -float(c) * t * (t - 2) + float(b)

    def easeInOut(self, t, b, c, d):
        t = float(t) / (float(d) / 2)
        if t < 1:
            return float(c) / float(2) * t * t + float(b)
        else:
            t -= 1
            return float(-c) / 2 * (t * (t - 2) - 1) + float(b)


class Cubic(object):
    def __init__(self):
        pass

    def easeIn(self, t, b, c, d):
        t = float(t) / float(d)
        return float(c) * t * t * t + float(b)

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d) - 1
        return float(c) * (t * t * t + 1) + float(b)

    def easeInOut(self, t, b, c, d):
        t = float(t) / (float(d) / 2)
        if (t < 1):
            return float(c) / 2 * t * t * t + float(b)
        else:
            t -= 2
            return float(c) / 2 * (t * t * t + 2) + float(b)


class Quart(object):
    def __init__(self):
        super(Quart, self).__init__()

    def easeIn(self, t, b, c, d):
        t = float(t) / float(d)
        return float(c) * t * t * t * t + float(b)

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d) - 1
        return float(-c) * (t * t * t * t - 1) + float(b)

    def easeInOut(self, t, b, c, d):
        t = float(t) / (float(d) / 2)
        if (t < 1):
            return float(c) / 2 * t * t * t * t + float(b)
        else:
            t -= 2
            return float(-c) / 2 * (t * t * t * t - 2) + float(b)


class Quint(object):
    def __init__(self):
        super(Quint, self).__init__()

    def easeIn(self, t, b, c, d):
        t = float(t) / float(d)
        return float(c) * t * t * t * t * t + float(b)

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d) - 1
        return float(c) * (t * t * t * t * t + 1) + float(b)

    def easeInOut(self, t, b, c, d):
        t = float(t) / (float(d) / 2)
        if (t < 1):
            return float(c) / 2 * t * t * t * t * t + float(b)
        else:
            t -= 2
            return float(c) / 2 * (t * t * t * t * t + 2) + float(b)


class Sine(object):
    def __init__(self):
        super(Sine, self).__init__()

    def easeIn(self, t, b, c, d):
        return float(-c) * math.cos(float(t) / float(d) * (math.pi / 2)) + float(c) + float(b)

    def easeOut(self, t, b, c, d):
        return float(c) * math.sin(float(t) / float(d) * (math.pi / 2)) + float(b)

    def easeInOut(self, t, b, c, d):
        return float(-c) / 2 * (math.cos(math.pi * float(t) / float(d)) - 1) + float(b)


class Expo(object):
    def __init__(self):
        pass

    def easeIn(self, t, b, c, d):
        if t == 0:
            return b
        else:
            return float(c) * math.pow(2, 10 * (float(t) / float(d) - 1)) + float(b)

    def easeOut(self, t, b, c, d):
        if t == d:
            return float(b) + float(c)
        else:
            return float(c) * (-math.pow(2, -10 * float(t) / float(d)) + 1) + float(b)

    def easeInOut(self, t, b, c, d):
        if t == 0: return b
        if t == d: return b + c
        t = float(t) / (float(d) / 2)
        if (t < 1):
            return float(c) / 2 * math.pow(2, 10 * (float(t) - 1)) + float(b)
        else:
            return float(c) / 2 * (-math.pow(2, -10 * --t) + 2) + float(b)


class Circ(object):
    def __init__(self):
        super(Circ, self).__init__()

    # error
    def easeIn(self, t, b, c, d):
        t = float(t) / float(d)
        return float(-c) * (math.sqrt(1 - t * t) - 1) + float(b)

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d) - 1
        return float(c) * math.sqrt(1 - t * t) + float(b)

    def easeInOut(self, t, b, c, d):
        t = float(t) / (float(d) / 2)
        if t < 1:
            return float(-c) / 2 * (math.sqrt(1 - t * t) - 1) + float(b)
        else:
            t -= 2
            return float(c) / 2 * (math.sqrt(1 - t * t) + 1) + float(b)


class Elastic(object):
    def __init__(self):
        super(Elastic, self).__init__()

    def easeIn(self, t, b, c, d, a, p):
        if t == 0:
            return b
        t = float(t) / float(d)
        if t == 1:
            return float(b) + float(c)
        if not p:
            p = float(d) * .3
        if not a or a < abs(c):
            a = float(c)
            s = float(p) / 4
        else:
            s = float(p) / (2 * math.pi) * math.asin(float(c) / float(a))
        t -= 1
        return -(float(a) * math.pow(2, 10 * t) * math.sin(
            (t * float(d) - float(s)) * (2 * math.pi) / float(p))) + float(b)

    def easeOut(self, t, b, c, d, a, p):
        if t == 0: return b
        t = float(t) / float(d)
        if t == 1:
            return b + c
        if not p:
            p = float(d) * .3
        if not a or a < abs(c):
            a = c
            s = p / 4
        else:
            s = p / (2 * math.pi) * math.asin(c / a)
        return a * math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) + c + b

    def easeInOut(self, t, b, c, d, a, p):
        if t == 0:
            return b
        t = float(t) / (float(d) / 2)
        if t == 2:
            return b + c
        if not p:
            p = d * (.3 * 1.5)
        if not a or a < abs(c):
            a = c
            s = p / 4
        else:
            s = p / (2 * math.pi) * math.asin(c / a)
        if t < 1:
            t -= 1
            return -.5 * (a * math.pow(2, 10 * t) * math.sin((t * d - s) * (2 * math.pi) / p)) + b
        t -= 1
        return a * math.pow(2, -10 * t) * math.sin((t * d - s) * (2 * math.pi) / p) * .5 + c + b


class Back(object):
    def __init__(self):
        super(Back, self).__init__()

    def easeIn(self, t, b, c, d, s):
        if not s:
            s = 1.70158
        t = float(t) / float(d)
        return c * t * t * ((s + 1) * t - s) + b

    def easeOut(self, t, b, c, d, s):
        if not s:
            s = 1.70158
        t = float(t) / float(d) - 1
        return c * (t * t * ((s + 1) * t + s) + 1) + b

    def easeInOut(self, t, b, c, d, s):
        if not s:
            s = 1.70158
        t = float(t) / (float(d) / 2)
        if t < 1:
            s *= (1.525)
            return c / 2 * (t * t * (((s) + 1) * t - s)) + b
        t -= 2
        s *= (1.525)
        return c / 2 * (t * t * (((s) + 1) * t + s) + 2) + b


class Bounce(object):
    def __init__(self):
        super(Bounce, self).__init__()

    def easeIn(self, t, b, c, d):
        return c - self.easeOut(d - t, 0, c, d) + b

    def easeOut(self, t, b, c, d):
        t = float(t) / float(d)
        if t < (1 / 2.75):
            return c * (7.5625 * t * t) + b
        elif t < (2 / 2.75):
            t -= (1.5 / 2.75)
            return c * (7.5625 * t * t + .75) + b
        elif t < (2.5 / 2.75):
            t -= (2.25 / 2.75)
            return c * (7.5625 * t * t + .9375) + b
        else:
            t -= (2.625 / 2.75)
            return c * (7.5625 * t * t + .984375) + b

    def easeInOut(self, t, b, c, d):
        if t < d / 2:
            return self.easeIn(t * 2, 0, c, d) * .5 + b
        else:
            return self.easeOut(t * 2 - d, 0, c, d) * .5 + c * .5 + b

