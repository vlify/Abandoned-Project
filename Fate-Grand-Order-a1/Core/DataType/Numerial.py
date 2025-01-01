# coding=utf-8
class Numerial(object):
    def __init__(self, val, max_val, min_val=0):
        super(Numerial, self).__init__()
        self.val = val
        self.max_val = max_val
        self.min_val = min_val

    def set_val(self, val):
        self.val = self.max_val = val

    def get_val(self):
        return self.val

    def is_zero(self):
        if self.val == 0:
            return True
        else:
            return False

    def is_min_val(self):
        if self.val <= self.min_val:
            return True
        else:
            return False

    def is_max_val(self):
        if self.val >= self.max_val:
            return True
        else:
            return False

    def verity_overstep(self, val):
        __val = self.val
        __val -= val
        if __val < self.min_val:
            return True
        else:
            return False

    # 减少 超出
    def reduce_overstep(self, val):
        __val = self.val
        __val -= val
        return -__val

    # 增加 超出
    def increase_overstep(self, val):
        self.val += val
        if self.is_max_val():
            return self.val - self.max_val

    # 减少
    def reduce(self, val):
        self.val -= val
        if self.is_min_val():
            self.val = self.min_val

    # 增加
    def increase(self, val):
        self.val += val
        if self.is_max_val():
            self.val = self.max_val
