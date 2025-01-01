import pygame

from Core.Game.function import get_game


class CharacterAnimate(object):
    class Clip(object):
        def __init__(self, surface, speed):
            super(CharacterAnimate.Clip, self).__init__()
            self.surface = surface
            self.speed = speed

    def __init__(self, data_list, flip):
        super(CharacterAnimate, self).__init__()
        self.duration = 0
        self.time = 0
        self.Time = 0
        self._Time = 0
        self.round = 0
        self.round_event = []
        self.time_event = []
        self.play = True
        for data in data_list:
            setattr(self, data["name"], self.create_clip(data['surface'], data['jsonData'], flip))

    '''
        event = [{"round":1,"event":[]}]
    '''

    def set_round_event(self, event):
        self.round_event = event

    '''
        event = [{"time":140,"event":[]}]
    '''

    def set_time_event(self, event):
        self.time_event = event

    def set_animate(self, animateName, start_clip):
        self.duration = 0
        animate = getattr(self, animateName)
        self.current, self.num = animate, len(animate)
        self.index = start_clip
        for sp in self.current:
            self.duration += sp.speed

    def create_clip(self, image, data, flip):
        arr = []
        for _data in data:
            rect = _data["x"], _data["y"], _data["w"], _data["h"]
            speed = _data['speed']
            if not flip:
                clip = CharacterAnimate.Clip(image.subsurface(rect), speed)
            else:
                surface = pygame.transform.flip(image.subsurface(rect), True, False)
                clip = CharacterAnimate.Clip(surface, speed)
            arr.append(clip)
        return arr

    def get_surface(self, index):
        return self.current[index].surface

    def update(self):
        if self.play:
            mt = get_game().mTime
            if not self.round_event:
                self.time += mt
                if self.time > self.current[self.index].speed:
                    self.time = 0
                    self.index += 1
                if self.index >= self.num:
                    self.index = 0
            else:
                self.Time += mt
                if self.Time < self.duration:
                    self.time += mt
                    if self.time > self.current[self.index].speed:
                        self.time = 0
                        self.index += 1
                    if self.index >= self.num:
                        self.index = 0
                else:
                    self.round += 1
                    self.Time = 0
                    self._Time = 0

                for item in self.round_event:
                    round, event = item['round'], item['event']
                    if self.round == round:
                        for e in event:
                            e()

            if self.time_event:
                self._Time += mt
                for item in self.time_event:
                    time, event, do = item['time'], item['event'], item['do']
                    if time >= self._Time - mt and time <= self._Time + mt and not item['do']:
                        for e in event:
                            e()
                            item['do'] = True
                        self.time_event.remove(item)


class AnimateSpirte(pygame.sprite.Sprite):
    '''
    data= [
            {"name":"stand","surface":surface,"jsonData":data},
            {"name":"stand","surface":surface,"jsonData":data},
            {"name":"stand","surface":surface,"jsonData":data}
         ]
    '''

    def __init__(self, data, clip):
        super(AnimateSpirte, self).__init__()
        self.data = data
        self.animate = CharacterAnimate(data, clip)

    def get_animate_duration(self, animateName):
        data = []
        for _data in self.data:
            if _data['name'] is animateName:
                data = _data
        dur = 0
        for _data in data['jsonData']:
            dur += int(_data['speed'])
        return dur

    def update(self):
        super(AnimateSpirte, self).update()
        self.animate.update()
        self.image = self.animate.get_surface(self.animate.index)
        self.rect.topleft = self.position

    # first run fun
    def set_animate(self, animateName, start_clip, pos):
        self.animate.set_animate(animateName, start_clip)
        self.image = self.animate.get_surface(start_clip)
        self.rect = self.image.get_rect()
        self.position = pos
        self.rect.topleft = self.position

    def add_round_event(self, event):
        self.animate.set_round_event(event)

    def clear_round_event(self):
        self.animate.round_event = []

    def reset_animate_state(self):
        self.animate.Time = 0
        self.animate.time = 0
        self.animate.round = 0

    def add_time_event(self, event):
        for e in event:
            e['do'] = False
        self.animate.set_time_event(event)

    def clear_time_event(self):
        self.animate.time_event = []
