import random
secret=random.randint(1,10) 
print("---------------我爱小平-------------")
temp=input("不妨猜一下小平现在心里想的是哪个数字：\n")
guess=int(temp)
i=1
while guess !=secret and i<=3:
    temp=input("哎呀，猜错了，请重新输入吧：\n")
    guess=int(temp)
    if guess == secret:
        print("我操，你是小平心里的蛔虫吗?!")
        print("哼，猜中了也没有奖励！  ")
    else:
        if guess>secret:
            print("大了，大了")
        else:
            print("嘿，小了，小了")
    i=i+1
print("游戏结束，不玩了")
