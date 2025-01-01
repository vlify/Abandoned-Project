# coding=utf-8
import Core.Game.globalvar as gl
from Core.Game.function import get_game


# 生成敌人数据
# order 为 敌人品阶 分为5级
def create_enemy_data(level, order):
    pass


def empty_ui():
    ui = gl.get_value("Game").uiGroup
    print(ui)
    game = gl.get_value('Game')
    game.uiGroup.empty()


def add_ui(ui):
    game = gl.get_value('Game')
    game.uiGroup.add(ui)


def say(text):
    from Scripts.UI.MapUI import Say
    uiGroup = get_game().uiGroup
    say = Say(text)
    destory_say()
    uiGroup.add(say)


def destory_say():
    from Scripts.UI.MapUI import Say
    uiGroup = get_game().uiGroup
    for sprite in uiGroup.sprites():
        if isinstance(sprite, Say):
            uiGroup.remove(sprite)


def set_enemy_team(enemy_list):
    gl.set_value("enemys", enemy_list)


def get_enemy_team():
    return gl.get_value("enemys")


def empty_enemy_team():
    set_enemy_team([])


def get_resource(resource_name):
    return str(gl.get_value("USER_DATA")['resources'][resource_name])


def get_material(material_name):
    return str(gl.get_value("USER_DATA")['material'][material_name])


def set_resource(resource_name, value):
    gl.get_value("USER_DATA")['resources'][resource_name] = value
    return get_resource(resource_name)


def set_material(material_name, value):
    gl.get_value("USER_DATA")['material'][material_name] = value
    return get_resource(material_name)

