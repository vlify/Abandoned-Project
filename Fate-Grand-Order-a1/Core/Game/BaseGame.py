import pygame

import Core.Game.globalvar as gl
from Core.Game.function import getImage
from Core.conf import windowIcon
from conf import FPS, windowTitle, BLACK, windowSize


class BaseGame(object):
    def __init__(self):
        super(BaseGame, self).__init__()
        gl.start()
        pygame.init()
        self.display = pygame.display
        self.isRunning = True
        self.scene = None

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(windowSize, 0, 32)
        icon = getImage(windowIcon, type=1)
        self.display.set_icon(icon)
        self.mTime = 0
        self.scenePlay = True

    def run(self):
        while self.isRunning:
            self.clock.tick(FPS)
            self.display.set_caption(windowTitle + " FPS:" + str(round(self.clock.get_fps(), 1)))
            self.mTime = self.clock.get_time()
            self.screen.fill(BLACK)
            for e in pygame.event.get():
                if e.type is pygame.QUIT:
                    self.isRunning = False
            if self.scene:
                self.scene.draw(self.screen)
                if self.scenePlay:
                    self.scene.update()
            self.group_run()
            pygame.display.update()

    def play(self):
        self.scenePlay = True

    def pause(self):
        self.scenePlay = False

    def enterScene(self, scene):
        self.scene = scene

    def group_run(self):
        pass
