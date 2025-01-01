# coding=utf-8
from Core.Game.Scene import Scene
from Core.Game.function import centerXY, getImage, set_attr_matrix_all, set_system, get_system
from Core.Game.MapBase import Map, Player, Camera, MapEnemy
from Scripts.Model.Enemy import Enemy
from Scripts.Sys.MapSys import MapSys
from Scripts.UI.MapUI import MapUI
from Scripts.function import empty_ui, add_ui
from conf import resourcePath, windowSize


class RandomMapScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        empty_ui()

        size = 10, 10
        self.tileSize = 32, 32

        base, up, element = Enemy.rank_data()
        data = {
            'name': '121212',
            'sex': 1,
            'profession': 'rider',
            'race': 'human',
            'base': base,
            'up': up,
            'element': element
        }
        level = 5
        coord = 0, 0
        enemy_blocks = [
            MapEnemy([Enemy(data, level)], coord)
        ]
        self.map = Map(self, size, self.tileSize, enemy_blocks)

        surface = getImage(resourcePath + "image/player.png", type=1)
        pos = centerXY(self.tileSize)
        self.player = Player(pos, self.tileSize, surface)
        sp_player = self.player.get_sprite()
        set_system(MapSys(self.player.servant))

        self.coords = 1, 0
        self.camera = Camera(windowSize, self.tileSize, [0, 0])
        self.move_player_coords(self.coords)

        self.add(self.map)
        self.add(sp_player)
        add_ui(MapUI())

    def move_player(self, position, coord):
        self.camera.set_map_coods(position)
        self.map.set_pos(self.camera.center())  # 移动： map跟着镜头pos变，人物不变 ， 先设置镜头在地图上的坐标，然后让地图坐标 = 镜头center 坐标
        self.map.set_player(coord)
        self.map.set_player_move_area(get_system().player_can_move_speed, self.player.move_type)
        set_attr_matrix_all(self.map.matrix_block, "move", 0)
        self.map.set_fog_area(coord, get_system().player_see)

    def move_player_coords(self, coords):
        position = [coords[0] * self.tileSize[0], coords[1] * self.tileSize[0]]
        self.move_player(position, coords)
