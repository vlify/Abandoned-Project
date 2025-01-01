import sys
import pygame
from Setting import *

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新游戏状态
    # TODO: 在此处添加游戏逻辑和状态更新代码

    # 渲染画面
    screen.fill((0, 0, 0))
    # TODO: 在此处添加绘制图形和文本的代码

    # 更新屏幕显示
    pygame.display.flip()