import pygame
import sys
import math
from random import *
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size
        
    def move(self):
        self.rect = self.rect.move(self.speed)

        if self.rect.right < 0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.bottom < 0:
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0

         
def collide_check(item, target):
    col_balls = []
    for each in target:
        distance = math.sqrt(math.pow((item.rect.center[0]-each.rect.center[0]),2)+\
                             math.pow((item.rect.center[1]-each.rect.center[1]),2))
        if distance <= (item.rect.width + each.rect.width) / 2:
            col_balls.append(each)

    return col_balls

        
def main():
    pygame.init()

    ball_image = "gray_ball.png"
    bg_image = "background.png"

    running = True

    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")

    background = pygame.image.load(bg_image).convert_alpha()
    #用来存放小球对象的列表
    balls = []
    #创建五个小球
    BALL_NUM = 5
    
    for i in range(BALL_NUM):
        #小球位置随机，速度随机
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        while collide_check(ball, balls):
             ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
            
        balls.append(ball)

    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0,0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
            
        for i in range(BALL_NUM):
            item = balls.pop(i)

            if collide_check(item, balls):
                item.speed[0] = - item.speed[0]
                item.speed[1] = - item.speed[1]

            balls.insert(i, item)
                
        pygame.display.flip()
        clock.tick(30)

    
if __name__ == "__main__":
    main()
