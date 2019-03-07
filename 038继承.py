import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(1,10)
        self.y = r.randint(1,10)

    def move(self):
        self.x -=1;
        print('我的位置是：', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self)#1.未绑定的父类方法
        super().__init__()  #2.super方法调用父类的方法
        self.hungry = True

    def eat(self):
        if self.hungry :
            print('天天有得吃')
            self.hungry = False
        else:
            print('不饿！')

