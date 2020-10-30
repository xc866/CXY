import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode([500, 500])


pygame.display.set_caption("窗口标题")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 若检测到事件类型为退出，则退出系统
            pygame.quit()
            sys.exit()
    pygame.display.update()


