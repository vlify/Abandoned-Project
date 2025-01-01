import pygame


class Page(object):
    def __init__(self, pageSize, maxNumber, current=1):
        super(Page, self).__init__()
        self.current = current
        self.pageSize = pageSize
        self.maxNum = maxNumber
        if self.maxNum % self.pageSize:
            self.lastPage = self.maxNum / self.pageSize
            self.lastPage += 1
        else:
            self.lastPage = self.maxNum / self.pageSize

    def prevPage(self):
        self.current -= 1
        if self.current < 1:
            self.current = 1

    def nextPage(self):
        self.current += 1
        if self.current > self.lastPage:
            self.current = self.lastPage

    def pages(self, font, color, c='/', surface=True):
        _current = ''
        if len(str(self.current)) < len(str(self.lastPage)):
            for x in range(len(str(self.lastPage)) - len(str(self.current))):
                _current += '0'
        _current += str(self.current)
        current = font.render(_current, 1, color)
        c = font.render(c, 1, color)
        max = font.render(str(self.lastPage), 1, color)
        if surface:
            size = current.get_rect().w + c.get_rect().w + max.get_rect().w, current.get_rect().h
            surface = pygame.Surface(size, pygame.SRCALPHA, 32)
            surface.blit(current, [0, 0])
            surface.blit(c, [current.get_rect().w, 0])
            surface.blit(max, [current.get_rect().w + c.get_rect().w, 0])
            return surface
        else:
            return current, c, max

    def start_end(self):
        return ((self.current - 1) * self.pageSize), ((self.current - 1) * self.pageSize) + self.pageSize - 1
