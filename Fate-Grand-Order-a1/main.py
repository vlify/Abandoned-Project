import Core.Game.globalvar as gl

from Scripts.Game import Game
from Core.Game.function import jumpScene, get_game
from Scripts.Scenes.FightScene import FightScene

from Scripts.Scenes.MainScene import MainScene
from Scripts.Scenes.STGTestScene import STGTestScene
from Scripts.Scenes.SaveDoneScene import SaveDoneScene
from Scripts.Scenes.CreateNewGameScene import CreateNewGameScene
from Scripts.Scenes.MapScene import MapScene
from Scripts.Scenes.RandomMapScene import RandomMapScene
# from Scripts.Scenes.STGTestScene import STGTestScene
from Scripts.Scenes.TestScene import TestScene
from Scripts.Scenes.TestScene2 import TestScene2

if __name__ == "__main__":
    gl.set_value("Game", Game())
    scene = MainScene()
    #scene = SaveDoneScene()
    #scene = CreateNewGameScene()
    #scene = MapScene()
    #scene = RandomMapScene()
    #scene = FightScene()
    #scene = STGTestScene()
    #scene = TestScene()
    #scene = TestScene2()
    jumpScene(scene)
    get_game().run()
