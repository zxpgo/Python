import pygame
import sys
from pygame.locals import *

#初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [5, 0]
bg = (255, 255, 255)

fullscreen = False
#创建指定大小窗口
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption("小乌龟")

#加载图片
turtle = pygame.image.load("turtle.jpg")

turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle
turtle = turtle_top

#获取图片的位置矩形
position = turtle.get_rect()

l_hand = turtle
r_hand = pygame.transform.flip(turtle, True, False)

LH = pygame.display.list_modes()[0]#获取当前电脑屏幕最高分辨率
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:

            #全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(LH, \
                                                     FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)  
            
                
    #移动图像
    position = position.move(speed)

    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.left = width - turtle_rect.width
        speed = [0, 5]

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.left = width -turtle_rect.width
        position.top = height -turtle_rect.height
        speed = [-5, 0]
        
    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.top = height -turtle_rect.height
        speed = [0, -5]

    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        speed = [5, 0]
        
  
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(turtle, position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(10)
    
        
