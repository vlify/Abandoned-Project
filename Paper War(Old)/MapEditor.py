# coding:utf-8
import pygame as pg
import json
from pygame.locals import *

from Setting import *
from Map import Land
from UI.Button import Button
from UI.Menu import Menu
from UI.Menu import DropMenu
from UI.MessageBox import MessageBox
from UI.Input import Input

pg.font.init()
font = pg.font.Font("Font/微软雅黑Bbold.ttf", 17)


class MapCompiler(object):
	def __init__(self):
		pg.init()
		'''创建屏幕'''
		self.screen = pg.display.set_mode((SCREEN_WHIGT, SCREEN_HIGHT))
		pg.display.set_caption("地图编译器V0.1")
		pg.key.set_repeat(400, 50)
		self.b_init()
		self.m_init()
		self.map_name = None
		self.map_data = []
		self.Clist = []
		self.land_state = ""


def get_event(self):
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        rel = pg.mouse.get_rel()
        click = pg.mouse.get_pressed()
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN:
            for c in self.Clist:
                self.map_name = c.input_get_event(event)
            if event.key == K_w and pg.key.get_mods() & KMOD_CTRL:
                self.write_map()
            if event.key == K_r and pg.key.get_mods() & KMOD_CTRL:
                self.read_map()
            if event.key == K_1:
                self.land_state = "草地"
            if event.key == K_2:
                self.land_state = "山地"
            if event.key == K_3:
                self.land_state = "海洋"

        if event.type == MOUSEMOTION:
            for c in self.Clist:
                if c.is_clicked:
                    c.move(event, pos, rel)
            if not any(c.is_clicked for c in self.Clist):
                self.Menu.button_chage_color(pos)
                for b in self.blist:
                    b.chage_color(pos)
        if event.type == MOUSEBUTTONDOWN:
            self.Menu.get_event(pos)
            for c in self.Clist:
                c.button_get_event(pos)
                if c.rect.collidepoint(pos):
                    c.is_clicked = True
                else:
                    c.is_clicked = False
            for b in self.blist:
                b.update(pos)
            if click[0]:
                if pos[1] > self.Menu.hight and pos[0] < SCREEN_WHIGT - 200 and self.land_state != "":
                    pg.event.wait()
                    if self.land_state == "delete":
                        for land in self.map_data:
                            if land[0] == pos[0] // RECT_WHIGT + 1 and land[1] == pos[1] // RECT_HIGHT + 1:
                                self.map_data.remove(land)
                    land = self.land_factory(pos)
                    if land and self.not_in_map_data(land):
                        self.map_data.append(land)
            elif event.type == MOUSEBUTTONUP:
                for c in self.Clist:
                    c.is_clicked = False


def read_map(self):
		print("读取地图数据ing")
		self.map_data = []
		mb = MessageBox(self.screen, (SCREEN_WHIGT - 170) // 2, SCREEN_HIGHT // 2, "InputBox", "输入地图文件名",
						wide=300, high=200, input_w=250)
		self.Clist.append(mb)
		if self.map_name != None:
			self.map_name = self.map_name[1:]
			try:
				with open(MapPath + self.map_name + ".json", "r") as f:
					self.map_data = json.loads(f.read())
				mb.Blist[0].event()
				self.Clist.remove(mb)
				del mb
			except FileNotFoundError:
				mb = MessageBox(self.screen, (SCREEN_WHIGT - 170) // 2, SCREEN_HIGHT // 2, "TextBox",
								"好像没有这个文件", wide=200, high=150)
				self.Clist.append(mb)

	def write_map(self):
		print("写入地图数据ing")
		mb = MessageBox(self.screen, (SCREEN_WHIGT - 170) // 2, SCREEN_HIGHT // 2, "TextBox", "保存成功", wide=200,
						high=150)
		self.Clist.append(mb)
		'''
        with open(MapPath+"map3.json","w") as f:
            f.write(json.dumps(self.map_data))
        print("写入成功")
        '''

	def new_map(self):
		mb = MessageBox(self.screen, (SCREEN_WHIGT - 170) // 2, SCREEN_HIGHT // 2, "InputBox", "输入地图文件名",
						wide=300, high=200, input_w=250)
		self.Clist.append(mb)

	def not_in_map_data(self, l):
		for land_data in self.map_data:
			if land_data[0] == l[0] and land_data[1] == l[1]:
				return False
		return True

	def land_factory(self, pos):
		land_data = list()

		land_data.append(pos[0] // RECT_WHIGT + 1)
		land_data.append(pos[1] // RECT_HIGHT + 1)

		if self.land_state == "山地":
			land_data.append(self.land_state)
			land_data.append(MOUNTAIN_COLOR)
		elif self.land_state == "草地":
			land_data.append(self.land_state)
			land_data.append(LAWN_COLOR)
		elif self.land_state == "海洋":
			land_data.append(self.land_state)
			land_data.append(OCEAN_COLOR)
		else:
			return None

		return tuple(land_data)

	def map_draw(self):
		"""地图可视化"""
		for land_data in self.map_data:
			l = Land(self.screen, land_data[2], land_data[0], land_data[1], land_data[3])

	def draw_black_line(self):
		"""真丶满屏黑线"""
		for w in range(0, SCREEN_HIGHT, 60):
			pg.draw.line(self.screen, BLACK, (0, w), (SCREEN_WHIGT - 170, w))
		for h in range(0, SCREEN_WHIGT - 170, 60):
			pg.draw.line(self.screen, BLACK, (h, 0), (h, 800))

	def update(self):
		while True:
			self.screen.fill((230, 230, 230))
			self.send_message(self.screen, "当前地形:" + self.land_state, (SCREEN_WHIGT - 170, 300))
			self.get_event()
			self.map_draw()
			self.draw_black_line()
			for c in self.Clist:
				c.update()
			self.Menu.updata()
			for b in self.blist:
				b.draw_button()
			pg.display.update()

	def b_init(self):
		b1 = Button(self.screen, "草地(1)", SCREEN_WHIGT - 170, 50)
		b2 = Button(self.screen, "山地(2)", SCREEN_WHIGT - 170, 150)
		b3 = Button(self.screen, "海洋(3)", SCREEN_WHIGT - 170, 250)
		b4 = Button(self.screen, "删除所有", SCREEN_WHIGT - 170, 400)
		b5 = Button(self.screen, "删除", SCREEN_WHIGT - 170, 500)
		self.blist = [b1, b2, b3, b4, b5]
		b1.set_elist(self.set_lawn)
		b2.set_elist(self.set_mountain)
		b3.set_elist(self.set_oeacn)
		b4.set_elist(self.delete_all)
		b5.set_elist(self.delete)

	def set_lawn(self):
		self.land_state = "草地"

	def set_mountain(self):
		self.land_state = "山地"

	def set_oeacn(self):
		self.land_state = "海洋"

	def delete_all(self):
		self.map_data = []

	def delete(self):
		self.land_state = "delete"

	def m_init(self):
		self.Menu = Menu(self.screen)
		Fmenu = DropMenu(self.screen)
		for t, f in {"打开": self.read_map, "保存": self.write_map, "新建": self.new_map}.items():
			Fmenu.add_command(t, f)
		self.Menu.add_cascade("文件", Fmenu)
		Qmenu = DropMenu(self.screen)
		for t in ["帮助", "关于"]:
			Qmenu.add_command(t, self.callback)
		self.Menu.add_cascade("其他", Qmenu)

	def send_message(self, sur, text, pos, color=BLACK):
		font_image = font.render(text, True, color)
		sur.blit(font_image, pos)

	def callback(self):
		print("texing")


if __name__ == "__main__":
	mc = MapCompiler()
	mc.update()
