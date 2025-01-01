# coding:utf-8
import pygame as pg
from Button import Button

pg.font.init()
font = pg.font.Font(None, 10)


class Menu:
	# 定义一个菜单按钮的默认宽度和高度
	BUTTON_WIDTH = 85
	BUTTON_HEIGHT = 40

	def __init__(self, screen):
		# 初始化菜单类，并传入屏幕对象
		self.screen = screen
		# 创建一个用于放置菜单按钮的表面对象，并且表面高度与BUTTON_HEIGHT相同
		self.surface = pg.Surface((self.screen.get_width(), self.BUTTON_HEIGHT))
		# 填充白色背景
		self.surface.fill((255, 255, 255))
		# 定义一个空列表用于存放菜单中的按钮
		self.buttons = []

	def add_button(self, label, command=None, dropdown=None):
		# 添加一个按钮，其中label表示按钮上的文字，command表示点击该按钮时所触发的事件
		# dropdown表示是否有下拉菜单与该按钮相关联

		# 计算新按钮的x轴位置，使其按照BUTTON_WIDTH在表面上水平排列
		x = self.BUTTON_WIDTH * len(self.buttons)

		# 创建一个新的按钮对象
		button = Button(self.surface, label, x, 0, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

		# 如果该按钮有下拉菜单，则设置事件调用下拉菜单对象的call方法
		if dropdown is not None:
			button.set_event(dropdown.call)
			dropdown.init(button)

		# 如果该按钮有自定义事件，则设置事件调用command方法
		if command is not None:
			button.set_event(command)

		# 将新的按钮添加到按钮列表中
		self.buttons.append(button)

	def get_event(self, pos):
		# 获取鼠标事件的位置pos，然后更新每个按钮的状态
		for button in self.buttons:
			button.update(pos)

	def button_change_color(self, pos):
		# 根据鼠标事件的位置pos，改变每个按钮的背景颜色
		for button in self.buttons:
			button.change_color(pos)

	def update(self):
		# 更新菜单表面的显示
		self.screen.blit(self.surface, (0, 0))
		# 循环遍历每个按钮并画出
		for button in self.buttons:
			button.draw_button()


class DropdownMenu:
	# 定义一个下拉菜单按钮的默认宽度和高度
	BUTTON_WIDTH = 85
	BUTTON_HEIGHT = 40

	def __init__(self, screen, items: list, x, y):
		# 初始化下拉菜单类，并传入屏幕对象，菜单项和x、y轴位置
		self.screen = screen
		self.x = x
		self.y = y
		self.is_open = False
		self.width = self.BUTTON_WIDTH
		self.height = self.BUTTON_HEIGHT * len(items)

		# 创建一个用于放置下拉菜单项的表面对象
		self.surface = pg.Surface((self.width, self.height))
		self.surface.fill((255, 255, 255))
		self.buttons = []

		# 添加下拉菜单项按钮
		for i, item in enumerate(items):
			button = Button(self.surface, item, 0, i * self.BUTTON_HEIGHT, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
			button.set_event(lambda: print(f"Clicked {item}"))
			self.buttons.append(button)

	def init(self, button):
		# 初始化下拉菜单与按钮之间的关系，即将下拉菜单的x、y轴位置设置为按钮的底部中心位置
		self.x = button.x + self.BUTTON_WIDTH // 2 - self.width // 2
		self.y = button.y + self.BUTTON_HEIGHT

	def call(self):
		# 切换下拉菜单的状态
		self.is_open = not self.is_open

	def draw(self):
		# 如果下拉菜单是打开状态，则将其显示在屏幕上
		if self.is_open:
			# 在屏幕上显示下拉菜单
			self.screen.blit(self.surface, (self.x, self.y))
			# 循环遍历每个下拉菜单项的按钮并画出
			for button in self.buttons:
				button.draw_button()
