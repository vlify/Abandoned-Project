import random

import pygame


class MovePoint(object):
    def __init__(self, start_position, end_position):
        super(MovePoint, self).__init__()
        self.x = self.y = 0
        self.start = pygame.math.Vector2(start_position)
        self.end = pygame.math.Vector2(end_position)

    def distance(self, current_position, distance=0.1):
        if pygame.math.Vector2(current_position).distance_to(self.end) > distance:
            return True
        return False

    def normalize(self):
        return (self.end - self.start).normalize()

    def set_focus(self, focus_position):
        self.end = pygame.math.Vector2(focus_position)

    def get_move_ip(self):
        normalize = self.normalize()
        x = y = 0
        self.x += normalize[0]
        self.y += normalize[1]
        if abs(self.x) > 1:
            x = int(self.x)
            self.x = self.x - x
        if abs(self.y) > 1:
            y = int(self.y)
            self.y = self.y - y
        return x, y

    @staticmethod
    def random_position(start_list, end_list):
        pos = random.randint(start_list[0], start_list[1]), random.randint(end_list[0], end_list[1])
        return pos