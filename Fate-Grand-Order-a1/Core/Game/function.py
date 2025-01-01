# coding=utf-8
import json, os, math, pygame
import random

import globalvar as gl
from Core.UI.Toast import Toast
from conf import windowSize, BLACK, fontYaHeiPath, msgFontSize, btnFontSize, SoundPath, multiLineHeight, fontPath, \
    MusicPath, SavePath, toastPos, fontYouyuanPath

'''
cardType = Buster | Arts | Quick | EX
position = 1 | 2 | 3 | 4
cardBuff = 影响此项的因素有从者保有技能"魔力放出"、怪物技能"蹂躏准备"、从者职阶技能"骑乘"、相关概念礼装、相关宝具特效等等。
firstBuff = 0 | 0.5 -- 0.5为红卡加成
moonType = Saber[1.00]、Archer[0.95]、Lancer[1.05]，四骑Rider[1.0]、Caster[0.9]、Assassin[0.9]、Berserker[1.1]，其他职阶Ruler[1.1]、Shielder[1.0]、Avenger[1.1]、Beast[1.0]
kezhi = 0.5 | 1.0 | 1.5 | 2.0  -- 0.5为被克制  1为无克制  1.5为Berserker克制  2为克制
xiangxing = 0.9 | 1.0 | 1.1  --  0.9为被克制  1为无克制  1.1为被克制
attkBuff = 影响此项的因素有从者保有技能"怪力"、从者保有技能"破坏工作"、Master技能"瞬间强化"、相关概念礼装、相关宝具特效等等。
targetDefBuff = 影响此项的因素有从者保有技能"变化"、从者保有技能"拷问技术"、怪物技能"硬化"、相关宝具特效等等。
tegongBuff = 敌人在Buff特攻范围内时计算此项，是针对特定对象的威力UP状态。例如从者保有技能"处刑人"、"银河流星剑"、相关概念礼装等等。某些活动期内，活动礼装的幅度极高的“攻击力UP”效果实质上也按特攻威力BUFF参与计算。
另外，多个特攻叠加的情况，增幅为直接加算，这种情况只会发生在存在多个特攻Buff同时被触发时。同一个Buff，即使是有多个范围的特攻Buff，被触发一个以上特攻条件时仍然只计算一次增幅。
我方在敌方Buff特防范围内时计算此项，是针对特定对象的防御力UP状态。如从者保有技能"屠龙者"。
baojiWeiliBuff = 暴击时计算此项。这里是“暴击威力BUFF－暴击威力DEBUFF”的简写。影响此项的因素有从者保有技能"心眼(伪)"、从者保有技能"鉴识眼"、怪物技能"畏怖"、从者职阶技能"单独行动"、相关概念礼装等等。
baoji = True | False -- 暴击 | 非暴击
chain = 3.5 | 2.0 三卡同色 | 非三卡同色
gudingBuff = 增加固定伤害的BUFF。如从者保有技能"军师的指挥"、从者职阶技能"神性"、相关概念礼装等等。
targetGudingBuff = 敌方减免固定伤害的BUFF。如从者保有技能"军师的忠言"等。
busterChain = 0 | 0.2 前三张指令卡都为红卡[0.2]和不都为红卡[0]两种情况。

'''


def attackNumber(atk, cardType="Buster", position=1, cardBuff=None, firstBuff=0.0, moonType="Saber", kezhi=1.0,
                 xiangxing=1.0, attkBuff=None, targetDefBuff=None, tegongBuff=None, tefangBuff=None,
                 baojiWeiliBuff=None,
                 baoji=False, chain=3.5, gudingBuff=None, targetGudingBuff=None, busterChain=0.0):
    if cardType == "Buster":
        x = 1.5
    elif cardType == "Arts":
        x = 1.0
    elif cardType == "Quick":
        x = 0.8
    else:
        x = 1.0
    if position == 1:
        y = 1.0
    elif position == 2:
        y = 1.2
    elif position == 3:
        y = 1.4
    else:
        y = 1.0

    if None == cardBuff:
        z = 0.0

    if moonType == "Saber":
        a = 1.00
    elif moonType == "Archer":
        a = 0.95
    elif moonType == "Lancer":
        a = 1.05
    elif moonType == "Rider":
        a = 1.0
    elif moonType == "Caster":
        a = 0.9
    elif moonType == "Assassin":
        a = 0.9
    elif moonType == "Berserker":
        a = 1.1
    elif moonType == "Ruler":
        a = 1.1
    elif moonType == "Shielder":
        a = 1.0
    elif moonType == "Avenger":
        a = 1.1
    else:
        a = 1.0

    if None == attkBuff:
        b = 0.0
    if None == targetDefBuff:
        c = 0.0
    if None == tegongBuff:
        d = 0.0
    if None == tefangBuff:
        e = 0.0
    if baoji:
        f = 2.0
    else:
        f = 1.0

    if None == baojiWeiliBuff:
        g = 0.0
    if None == gudingBuff:
        h = 0.0
    if None == targetGudingBuff:
        j = 0.0

    import random
    randFloat = float(random.randint(90, 110)) / 100.00
    return int(float(atk) * 0.23 * (x * y * (1 + z) + firstBuff) * a * kezhi * xiangxing * randFloat * (
            1 + b - c) * (1 + d - e + g) * f * chain + (h - j) + float(atk) * busterChain)


def jumpScene(scene):
    set_scene(scene)


def centerX(width=0):
    return (windowSize[0] - width) / 2


def centerY(height=0):
    return (windowSize[1] - height) / 2


def centerXY(size=None):
    if size is None:
        size = [0, 0]
    return centerX(size[0]), centerY(size[1])


def floatRight(w=0):
    return windowSize[0] - w


def bottom(height):
    return windowSize[1] - height


def playMusic(file, volume=.4, loop=-1):
    import pygame
    file = MusicPath + file
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loop, 0)
    pygame.mixer.music.set_volume(volume)


def MultiText(text, maxFontLength=100, color=BLACK, width=100, height=None, lineHeight=multiLineHeight,
              backgroundColor=None,
              font=fontYaHeiPath, fontSize=msgFontSize):
    _arrText = text.split("\n")
    _arrSur = []
    h = 0
    for text in _arrText:
        sur = MultiTextLen(text, maxFontLength, color, width, height, lineHeight, backgroundColor, font, fontSize)
        _arrSur.append(sur)
        h += sur.get_rect().h
    if height is None:
        _h = h
    else:
        _h = height
    surface = create_surface([width, _h], alpha=0)
    if backgroundColor:
        surface.fill(backgroundColor)
    i = 0
    for x in _arrSur:
        if i is 0:
            pos = 0, 0
        else:
            pos = 0, pos[1] + _arrSur[i - 1].get_rect().h
        i += 1
        surface.blit(x, pos)
    return surface


def MultiTextLen(text, maxFontLength=100, color=BLACK, width=100, height=None, lineHeight=multiLineHeight,
                 backgroundColor=None,
                 font=fontYaHeiPath, fontSize=msgFontSize):
    pygame.font.init()
    font = pygame.font.Font(font, fontSize)
    maxNum = len(text) / maxFontLength + 1
    if height is None:
        h = lineHeight * maxNum
    else:
        h = height
    surface = create_surface([width, h], alpha=0)
    if backgroundColor:
        surface.fill(backgroundColor)
    for x in range(0, maxNum):
        _text = text[:maxFontLength]
        text = text[maxFontLength:]
        pos = 0, x * lineHeight
        surface.blit(font.render(_text, True, color), pos)
    return surface


def singleText(text, color=BLACK, size=msgFontSize, path=fontYaHeiPath):
    pygame.font.init()
    font = pygame.font.Font(path, size)
    return font.render(text, True, color)


def getJsonFile(filePath):
    import os
    import json
    if os.path.exists(filePath):
        __file = open(filePath, "rb")
        data = json.load(__file)
        __file.close()
        return data
    else:
        print("file Not Exist : " + filePath)
        return False


def alphaText(text, size=btnFontSize, color=BLACK, path=fontYaHeiPath, bold=False, border=False):
    import pygame
    antialias = 400
    font = pygame.font.Font(path, size)
    font.set_bold(bold)
    if border is not True:
        return font.render(text, antialias, color)
    else:
        surface = font.render(text, antialias, color)
        # shadow
        surface1 = font.render(text, antialias, [21, 21, 21])
        surface2 = font.render(text, antialias, [21, 21, 21])
        surface1.blit(surface2, [2, 2])
        surface1.blit(surface, [1, 1])
        return surface1


def createSceneClass(module_name, scnenName, *args):
    module = __import__(module_name + "." + scnenName, fromlist=True)
    c = getattr(module, scnenName)
    return c(*args)


def playSound(file, loop=0, volume=1):
    pygame.mixer.init()
    filePath = SoundPath + file + ".wav"
    sound = pygame.mixer.Sound(filePath)
    sound.set_volume(volume)
    sound.play(loop)
    return "path:" + filePath + " volume:" + str(sound.get_volume())


def getImage(file, size=None, type=0):
    if type == 0:
        image = pygame.image.load(file).convert()
    else:
        image = pygame.image.load(file).convert_alpha()
    if size != None:
        image = pygame.transform.scale(image, size)
    return image


def subImage(surface, rect, size=None):
    return surface.subsurface(rect)


def saveFile(jsonData, fileName):
    jsObj = json.dumps(jsonData)
    file = SavePath + fileName + '.json'
    arr = file.split("/")
    last = arr[len(arr) - 1]
    _file = file[:-len(last)]
    if not os.path.exists(_file):
        os.makedirs(_file)
    fileObject = open(file, 'w')
    fileObject.write(jsObj)
    fileObject.close()


def removeFile(file):
    os.remove(file)


def toast(msg, pos=toastPos, size=[200, 50], time=2000):
    if not gl.get_value('MsgList'):
        gl.set_value('MsgList', [])
    msglist = gl.get_value('MsgList')
    game = gl.get_value('Game')
    toast = Toast(msg, pos, size, time)
    msglist.append(toast)
    game.msgGroup.add(toast)


def play():
    game = gl.get_value('Game')
    game.scenePlay = True


def playGameGroup(groupName):
    game = gl.get_value('Game')
    if hasattr(game, groupName):
        setattr(game, groupName, True)


def pause():
    game = gl.get_value('Game')
    game.scenePlay = False


def pauseGameGroup(groupName):
    game = gl.get_value('Game')
    if hasattr(game, groupName):
        setattr(game, groupName, False)


def showDialog(dialog):
    game = gl.get_value('Game')
    if hasattr(dialog, "name"):
        print dialog.name + ' Show!'
    if game.dialogGroup.sprites():
        for _dialog in game.dialogGroup.sprites():
            if _dialog.name != dialog.name:
                game.dialogGroup.add(dialog)
    else:
        game.dialogGroup.add(dialog)


def closeDialog(dialog):
    game = gl.get_value('Game')
    game.dialogGroup.remove(dialog)
    dialog.destory()


def showConfirm(confirm):
    pause()
    game = gl.get_value("Game")
    if not game.dialogGroup.has(confirm):
        game.dialogGroup.add(confirm)


def closeConfirm(confirm):
    play()
    game = gl.get_value("Game")
    game.dialogGroup.remove(confirm)
    if game.dialogGroup.has(confirm):
        game.dialogGroup.remove(confirm)


def click(rect, mouse_button_num=0):
    mouse = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if mouse[mouse_button_num] and rect.collidepoint(pos):
        return True
    return False


def format_number(num, _str='  '):
    if num < 10:
        return str(num) + _str
    return num


def resolve_image(imagePath, size, cut_size=35):
    image = getImage(imagePath, type=1)
    iw = image.get_rect().w
    ih = image.get_rect().h
    lt, rt, lb, rb, t, b, l, r, c = \
        [0, 0, cut_size, cut_size], [iw - cut_size, 0, cut_size, cut_size], \
        [0, ih - cut_size, cut_size, cut_size], [iw - cut_size, ih - cut_size, cut_size, cut_size], \
        [cut_size, 0, iw - cut_size * 2, cut_size], [cut_size, ih - cut_size, iw - cut_size * 2, cut_size], \
        [0, cut_size, cut_size, ih - cut_size * 2], [iw - cut_size, cut_size, cut_size, ih - cut_size * 2], \
        [cut_size, cut_size, iw - cut_size * 2, ih - cut_size * 2]

    self_image = create_surface(size, alpha=0)
    self_image.blit(image.subsurface(lt), [0, 0])
    t = pygame.transform.scale(image.subsurface(t), [size[0] - cut_size * 2, cut_size])
    self_image.blit(t, [cut_size, 0])
    self_image.blit(image.subsurface(rt), [size[0] - cut_size, 0])
    l = pygame.transform.scale(image.subsurface(l), [cut_size, size[1] - cut_size * 2])
    self_image.blit(l, [0, cut_size])
    r = pygame.transform.scale(image.subsurface(r), [cut_size, size[1] - cut_size * 2])
    self_image.blit(r, [size[0] - cut_size, cut_size])
    self_image.blit(image.subsurface(lb), [0, size[1] - cut_size])
    self_image.blit(image.subsurface(rb), [size[0] - cut_size, size[1] - cut_size])
    b = pygame.transform.scale(image.subsurface(b), [size[0] - cut_size * 2, cut_size])
    self_image.blit(b, [cut_size, size[1] - cut_size])
    c = pygame.transform.scale(image.subsurface(c), [size[0] - cut_size * 2, size[1] - cut_size * 2])
    self_image.blit(c, [cut_size, cut_size])

    return self_image


def create_surface(size, color=BLACK, alpha=False):
    if False is alpha:
        surface = pygame.Surface(size).convert()
        surface.fill(color)
    else:
        surface = pygame.Surface(size).convert_alpha()
        color = list(color) + [alpha]
        surface.fill(color)
    return surface


def near(matrix, pos, distance, type=1):
    foucus_pos = pos
    if distance <= 0:
        msg = '距离不能小于0'
        raise AttributeError(msg)
    if distance == 1:
        dd = near_one(matrix, pos, type)
        return {'1': dd}, dd
    else:
        __pos = {}
        __pos[1] = near_one(matrix, pos, type)
        all = __pos[1]
        for _num in range(1, distance):
            num = _num + 1
            _arr = []
            for _pos in __pos[_num]:
                _arr += near_one(matrix, _pos, type)
            arr = [list(t) for t in _arr]
            __pos[num] = []
            for ___pos in arr:
                if ___pos not in all and ___pos != foucus_pos:
                    __pos[num].append(___pos)
                    all.append(___pos)
        return __pos, all


def near_one(matrix, pos, type=1):
    if type == 1:
        xs = (-1, 0, 1, -1, 1, -1, 0, 1)
        ys = (-1, -1, -1, 0, 0, 1, 1, 1)
    else:
        xs = (0, -1, 1, 0)
        ys = (-1, 0, 0, 1)
    _pos = []
    for x, y in zip(xs, ys):
        _x, _y = pos[0] - x, pos[1] - y
        if _x >= 0 and _x <= len(matrix[0]) - 1 and _y >= 0 and _y <= len(matrix) - 1:
            _pos.append([_x, _y])
    return _pos


def cutImage(surface, w, h, size, offer_x=0, offer_y=0):
    t_w = size[0]
    t_h = size[1]
    arr = []
    if not isinstance(surface, pygame.Surface):
        raise AttributeError('surface 必须是 pygame.Surface 类型！')
    for y in range(h):
        _arr = []
        for x in range(w):
            rect = pygame.Rect(offer_x + x * t_w, offer_y + y * t_h, t_w, t_h)
            sur = surface.subsurface(rect)
            _arr.append(sur)
        arr.append(_arr)
    return arr


def toOneArray(multiArr):
    return [i for item in multiArr for i in item]


def set_attr_matrix(matrix, coords, attrName, attrSetValue):
    if isinstance(coords[0], list):
        for coord in coords:
            setattr(matrix[coord[0]][coord[1]], attrName, attrSetValue)
    else:
        setattr(matrix[coords[0]][coords[1]], attrName, attrSetValue)


def set_attr_matrix_all(matrix, attrName, attrValue):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            element = matrix[x][y]
            setattr(element, attrName, attrValue)


def set_attr_matrix_coords(matrix, coords, attrName, attrSetValue, attrDefValue):
    set_attr_matrix_all(matrix, attrName, attrDefValue)
    set_attr_matrix(matrix, coords, attrName, attrSetValue)


def get_coords_in_matrix_for_val(matrix, attrName, attrVal):
    coords = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            element = matrix[x][y]
            if hasattr(element, attrName):
                val = getattr(element, attrName)
                if val == attrVal:
                    coords.append([x, y])
            else:
                print "{0} not have {1}".format(type(element), attrName)
    if len(coords) > 1:
        return coords
    else:
        return coords[0]


def get_game():
    return gl.get_value('Game')


def angle(p1, p2):
    return math.atan2((p2[1] - p1[1]), (p2[0] - p1[0]))


def radian(p1, p2):
    return angle(p1, p2) * (180 / math.pi)


def random_name(length=3):
    xing = getJsonFile("Core/resource/data/xing.json")
    ming = getJsonFile("Core/resource/data/ming.json")
    if length == 3:
        name = xing[random.randint(0, len(xing))] + ming[random.randint(0, len(ming))] + ming[
            random.randint(0, len(ming))]
    elif length == 2:
        name = xing[random.randint(0, len(xing))] + ming[random.randint(0, len(ming))]
    else:
        name = random_name(random.randint(2, 3))
    return name


def set_scene(scene):
    get_game().scene = scene


def get_scene():
    return get_game().scene


def set_system(system):
    get_game().system = system


def get_system():
    return get_game().system


def get_mTime():
    return get_game().mTime


def get_items():
    return gl.get_value("items")


def get_item_data(item_id):
    for item in get_items():
        if item.id is item_id:
            return item
    return None


def shadowFont(font, text, color, shadowColor=[3, 9, 23, 3], shadowPos=[1, 1]):
    _font = font.render(text, 1, color)
    _shadow_font = font.render(text, 1, shadowColor)
    size = _font.get_rect().w + shadowPos[0], _font.get_rect().h + shadowPos[1]
    surface = pygame.Surface(size, pygame.SRCALPHA, 32)
    surface.blit(_shadow_font, shadowPos)
    surface.blit(_font, [0, 0])
    return surface


def getFont(path=fontYouyuanPath, size=16):
    return pygame.font.Font(path, size)


def numberSurface(value, path="resource/image/number.png"):
    surface = getImage(path, type=1)
    numbers = []
    width = surface.get_rect().w / 10
    size = width, surface.get_rect().h
    for x in range(10):
        pos = x * size[0], 0
        rect = pos, size
        numbers.append(surface.subsurface(rect))
    length = len(str(value))
    surface = pygame.Surface([length * size[0], size[1]], pygame.SRCALPHA, 32)
    for i, x in enumerate(str(value)):
        surface.blit(numbers[int(x)], [i * size[0], 0])

    return surface


def anglePos(pos, angle, r):
    return pos[0] + r * math.cos(angle * 3.14 / 180), pos[1] - r * math.sin(angle * 3.14 / 180)
