import pygame
import sys
from pygame.locals import *

#初始化Pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255, 255, 255)

fullscreen = False
#创建指定大小窗口
screen = pygame.display.set_mode(size, RESIZABLE)
#设置窗口标题
pygame.display.set_caption("小乌龟")

#设置放大缩小比率
ratio = 1.0
#加载图片
oturtle = pygame.image.load("turtle.jpg")
turtle = oturtle

#获取图片的位置矩形
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

l_hand = turtle
r_hand = pygame.transform.flip(turtle, True, False)

LH = pygame.display.list_modes()[0]#获取当前电脑屏幕最高分辨率
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
                turtle = l_hand
            if event.key == K_RIGHT:
                speed = [1, 0]
                turtle = r_hand
            if event.key == K_DOWN:
                speed = [0, 1]
            if event.key == K_UP:
                speed = [0, -1]

            #全屏（F11）
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(LH, \
                                                     FULLSCREEN | HWSURFACE)
                    width, height = LH
                else:
                    screen = pygame.display.set_mode(size)

            #放大缩小小乌龟(=,-)
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                #最大只能放大一倍，缩小50%
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS  and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                turtle = pygame.transform.scale(oturtle, (int(oturtle_rect.width * ratio),\
                                             int(oturtle_rect.height * ratio)))
                l_hand = turtle
                r_hand = pygame.transform.flip(turtle, True, False)
                    
        #用户调整窗口尺寸
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            print(size)
            screen = pygame.display.set_mode(size, RESIZABLE)
            
                
    #移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        #反方向移动
        speed[0] = -speed[0]

    if position.bottom > height or position.top < 0:
        speed[1] = -speed[1]

    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(turtle, position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(10)
    
        
