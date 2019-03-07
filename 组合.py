class Turtle:
    def __init__(self,x):
        self.num=x

class Fish:
    def __init__(self,y):
        self.num=y

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)

    def print_num(self):
        print("水池里共有乌龟%d只，小鱼%d只"%(self.turtle.num,self.fish.num))
