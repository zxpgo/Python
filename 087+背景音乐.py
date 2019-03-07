import pygame
import sys
import traceback
from random import *
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        pygame.sprite.Sprite.__init__(self)

        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        self.rect.left, self.rect.top = position
        self.side = [choice([-1, 1]), choice([-1, 1])]
        self.speed = speed
        self.collide = False#检查小球是否发生碰撞
        self.target = target
        self.control = False
        self.width, self.height = bg_size
        
    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move(self.side[0] * self.speed[0],\
                                   self.side[1] * self.speed[1])
        
        #如果小球的左侧出了边界，那么将小球左侧的位置改为右侧的边界
        #这样便实现了从左边进入，右边出来的效果
        if self.rect.right <= 0:
            self.rect.left = self.width

        elif self.rect.left >= self.width:
            self.rect.right = 0

        elif self.rect.bottom <= 0:
            self.rect.top = self.height

        elif self.rect.top >= self.height:
            self.rect.bottom = 0
            
    def check(self, motion):
        if self.target < motion < self.target + 5:
            return True
        else:
            return False
          
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = \
                              (bg_size[0] - self.glass_rect.width) // 2,\
                              bg_size[1] - self.glass_rect.height
        #导入想要鼠标图案， 并获取图案大小，以及设置鼠标默认位置
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top =\
                              self.glass_rect.left, self.glass_rect.top
        #让电脑鼠标图案消失
        pygame.mouse.set_visible(True)
        
        

def main():
    pygame.init()

    grayball_image = "gray_ball.png"
    greenball_image = "green_ball.png"
    bg_image = "background.png"
    glass_image = "bg.gif"
    mouse_image = "mouse_image.png"
    running = True

    #添加背景音乐
    #pygame.mixer.music.load("bg_music.ogg")
    #pygame.mixer.play()

    #添加音效
    #loser_sound = pygame.mixer.Sound("loser.wav")
    #laugh_sound = pygame.mixer.Sound("laugh.wav")
    #winner_sound = pygame.mixer.Sound("winner.wav")
    #hole_sound = pygame.mixer.Sound("hole.wav")

    #音乐播放完时游戏结束
    #GAMEOVER = USEREVENT
    #pygame.mixer.music.set_endevent(GAMEOVER)
    
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Play the ball")

    background = pygame.image.load(bg_image).convert_alpha()

    hole = [(117, 119+10, 199, 201+10), (225, 227+10, 390, 392+10), (503, 505+10, 320, 322+10),\
            (698, 700+10, 192, 194+10), (906, 908+10, 419, 411+10)]
    balls = []
    msgs = []
    group = pygame.sprite.Group()
    
    for i in range(5):
        position = randint(0, width-100), randint(0, height-100)
        speed = [randint(1, 10), randint(1, 10)]
        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5*(i+1))
        while pygame.sprite.spritecollide(ball, group ,False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width-100), randint(0, height-100)
            
        balls.append(ball)
        group.add(ball)
        
    #在背景底部添加画板
    glass = Glass(glass_image, mouse_image, bg_size)

    #记录鼠标触发事件个数
    motion = 0
    MYTIME = USEREVENT + 1
    pygame.time.set_timer(MYTIME, 1000)

    pygame.key.set_repeat(100, 100)
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #elif event.type == GAMEOVER:
             #   loser_sound.play()
              #  pygame.time.delay(2000)
               # laugh_sound.play()
                #running = False

            elif event.type == MYTIME:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0
            elif event.type == MOUSEMOTION:
                motion += 1
            #使用w a s d控制小球移动的方向
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                            
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1

                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
          
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0]-10 <= each.rect.left <= i[1] and\
                                   i[2]-10 <= each.rect.top <= i[3]:
                                    each.speed = [0, 0]
                                    group.remove(each)
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0, temp)
                                    hole.remove(i)
                                if not hole:
                                    #pygame.mixer.mousic.stop()
                                    #winner_sound.play()
                                    #pygame.time.delay(3000)
                                    msg = pygame.image.load("win.jpg").convert_alpha()
                                    msg_pos = (width - msg.get_width()) // 2,\
                                                    (height - msg.get_height()) //2
                                    msgs.append((msg, msg_pos))
                                    #laugh_sound.play()
                                    
        screen.blit(background, (0,0))
        screen.blit(glass.glass_image, glass.glass_rect)

        
        #得到现有鼠标的位置
        glass.mouse_rect.left, glass.mouse_rect.top = pygame.mouse.get_pos()
        #判断鼠标是否在面板内，如果超出拉回来
        if glass.mouse_rect.left < glass.glass_rect.left:
            glass.mouse_rect.left = glass.glass_rect.left
        if glass.mouse_rect.left > glass.glass_rect.right - glass.mouse_rect.width:
            glass.mouse_rect.left = glass.glass_rect.right - glass.mouse_rect.width
        if glass.mouse_rect.top < glass.glass_rect.top:
            glass.mouse_rect.top = glass.glass_rect.top
        if glass.mouse_rect.top > glass.glass_rect.bottom - glass.mouse_rect.height:
            glass.mouse_rect.top = glass.glass_rect.bottom - glass.mouse_rect.height
        #将所要的鼠标指针画到鼠标位置
        screen.blit(glass.mouse_image, glass.mouse_rect)
          
        for each in balls:
            each.move()
            #当发生碰撞速度变成随机
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False
            if each.control:
                #画绿色小球
                screen.blit(each.greenball_image, each.rect)
            else:
                #画灰色小球
                screen.blit(each.grayball_image, each.rect)

        for each in group :
            group.remove(each)
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                #当发生膨胀，小球速度方向取反
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False#发生碰撞变为不受控制的球
                
            group.add(each)

        for msg in msgs:
            screen.blit(msg[0], msg[1])
            
        pygame.display.flip()
        clock.tick(30)



    
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
