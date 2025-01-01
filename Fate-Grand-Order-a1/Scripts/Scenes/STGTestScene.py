import threading
from random import randint

import pygame
from pygame.math import Vector2
from transitions import Machine
from Core.AI.AiMove import AiMove
from Core.DataType.Delay import Delay
from Core.Game.AI import AI
from Core.Game.Scene import Scene
from Core.Game.function import create_surface, singleText, get_scene, anglePos, get_mTime, radian
from Scripts.SocketClient import client
from conf import WHITE


class AiEnemy(AI):
    def __init__(self):
        super(AiEnemy, self).__init__()

    @staticmethod
    def move(sprite):
        if sprite.state is "enter":
            print 11
        elif sprite.state is "fight":
            pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Enemy, self).__init__()
        size = 30, 30
        self.surface = create_surface(size, WHITE)
        self.image = self.surface
        self.rect = self.image.get_rect()
        states = ['enter', "fight", "leave"]
        initial = states[0]
        transitions = [
            {"trigger": "act_fight", "source": "enter", "dest": "fight"},
            {"trigger": "act_leave", "source": "fight", "dest": "leave"}
        ]
        Machine(self, states, initial, transitions)
        self.rect.topleft = Vector2(pos)

        self.atk_area = 3
        self.find_area = 6
        self.delay = Delay(500)

    def fire(self):
        list = []
        for x in range(0, 360, 30):
            data = {"angle": x, "pos": self.rect.center}
            list.append(data)
        client.emit("enemy bullet", list)

    def update(self, *args):
        super(Enemy, self).update()
        self.delay.update(get_mTime())
        if self.delay.loopRound(2):
            self.fire()

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, angle, pos, speed=3):
            super(Enemy.Bullet, self).__init__()
            size = 5, 5
            self.surface = create_surface(size, WHITE)
            # self.image = pygame.transform.rotozoom(self.surface, angle, 1)
            self.image = self.surface
            self.rect = self.image.get_rect()
            self.speed = speed
            self.rect.center = pos
            self.target_pos = anglePos(self.rect.center, angle, 360)
            self.vectorSpeed = pygame.math.Vector2(self.target_pos) - pygame.math.Vector2(self.rect.topleft)
            self.vectorSpeed.scale_to_length(self.speed)

        def update(self, *args):
            super(Enemy.Bullet, self).update()
            AiMove.posMove(self)
            AiMove.outWindowDestory(self)


class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        super(Character, self).__init__()
        self.name = name
        self.image = singleText(str(self.name), WHITE, 9)
        self.rect = self.image.get_rect()
        self.rect.topleft = randint(0, 100), randint(100, 300)
        self.speed_x = 2
        self.speed_y = 2


class OnlinePlayer(Character):
    def __init__(self, sid, name):
        super(OnlinePlayer, self).__init__(name)
        self.sid = sid

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, angle, pos, speed=3):
            super(OnlinePlayer.Bullet, self).__init__()
            size = 10, 2
            self.surface = create_surface(size, WHITE)
            # self.image = self.surface.copy()
            self.image = pygame.transform.rotozoom(self.surface, angle, 1)
            self.rect = self.image.get_rect()
            self.speed = speed
            self.rect.center = pos
            self.target_pos = anglePos(self.rect.center, angle, 360)
            self.vectorSpeed = pygame.math.Vector2(self.target_pos) - pygame.math.Vector2(self.rect.topleft)
            self.vectorSpeed.scale_to_length(self.speed)

        def update(self, *args):
            super(OnlinePlayer.Bullet, self).update()
            AiMove.posMove(self)
            AiMove.outWindowDestory(self)


class Player(Character):
    def __init__(self, name):
        super(Player, self).__init__(name)

    def update(self, *args):
        super(Player, self).update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -self.speed_y)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed_y)
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed_x, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed_x, 0)
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            data = {"sid": self.name, "pos": self.rect.topleft}
            client.emit("player move", data)
        mouse = pygame.mouse
        if mouse.get_pressed()[0]:
            angle = -round(radian(self.rect.center, mouse.get_pos()), 2)
            get_scene().add(Player.Bullet(angle, self.rect.center))
            data = {"sid": self.name, "angle": angle}
            client.emit("player fire", data)

    def move(self, *args):
        print self.name, args[0]['sid']
        if self.name == args[0]['sid']:
            pos = args[0]['pos']
            self.rect.topleft = pos

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, angle, pos, speed=3):
            super(Player.Bullet, self).__init__()
            size = 10, 2
            self.surface = create_surface(size, WHITE)
            self.image = pygame.transform.rotozoom(self.surface, angle, 1)
            # self.image = self.surface.copy()
            self.rect = self.image.get_rect()
            self.speed = speed
            self.rect.center = pos
            self.target_pos = anglePos(self.rect.center, angle, 360)
            self.vectorSpeed = pygame.math.Vector2(self.target_pos) - pygame.math.Vector2(self.rect.topleft)
            self.vectorSpeed.scale_to_length(self.speed)

        def update(self, *args):
            super(Player.Bullet, self).update()
            AiMove.posMove(self)
            AiMove.outWindowDestory(self)


class STGTestScene(Scene):
    def __init__(self):
        super(STGTestScene, self).__init__()
        self.playerList = []
        self.enemyList = []
        t = threading.Thread(target=self.socket)
        t.start()

    def socket(self):
        client.emit("user login", {"username": "admin"})
        client.on("player list", self.login)
        client.on("player pos", self.playerPos)
        client.on("bullet", self.bullet)

        client.on("create enemy", self.createEnemy)
        client.on("create enemy bullet", self.createEnemyBullet)
        client.wait()

    def login(self, *args):
        data = args[0]
        index = data['index']
        list = data['list']
        _list = []
        for sp in self.sprites():
            if isinstance(sp, Player) or isinstance(sp, OnlinePlayer):
                _list.append(sp.name)
        for player in list:
            if not player['sid'] in _list:
                _player = OnlinePlayer(player['sid'], player['sid'])
                _player.rect.topleft = player['pos']
                self.add(_player)
        hasPlayer = False
        for sprite in self.sprites():
            if isinstance(sprite, Player):
                hasPlayer = True
                break
        if not hasPlayer:
            _player = self.sprites()[index]
            self.remove(_player)
            _data = list[index]
            player = Player(_data['sid'])
            player.rect.topleft = _data['pos']
            self.add(player)

    def playerPos(self, data):
        for sprite in self.sprites():
            if isinstance(sprite, OnlinePlayer):
                if sprite.name == data['sid']:
                    sprite.rect.topleft = data['pos']

    def bullet(self, data):
        for sprite in self.sprites():
            if isinstance(sprite, OnlinePlayer):
                if sprite.name == data['sid']:
                    self.add(OnlinePlayer.Bullet(data['angle'], sprite.rect.center))

    def createEnemy(self, data):
        print data
        for enemy_pos in data:
            self.add(Enemy(enemy_pos['pos']))

    def createEnemyBullet(self, data):
        list = []
        for bullet in data:
            list.append(Enemy.Bullet(bullet['angle'], bullet['pos']))
        self.add(list, layer="enemy_bullet")
