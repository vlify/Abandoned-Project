# coding=utf-8

from Core.Game.Scene import Scene
from Core.Game.function import set_system
from Scripts.Scenes.TestScene4Component.Package import Package
from Scripts.Scenes.TestScene4Component.Platform import Platform
from Scripts.Sys.CraftSys import CraftSys


class TestScene2(Scene):
    def __init__(self):
        super(TestScene2, self).__init__()
        set_system(CraftSys())
        x = 450
        self.platform = Platform(pos=[x, 120], blockSize=[40, 40])
        self.package = Package(pos=[x, 320], blockSize=[40, 40])
        self.add(self.platform, self.package)

