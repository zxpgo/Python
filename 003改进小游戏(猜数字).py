import random
secret = random.randint(1,10)
print('---------------------zxp-------------------------')
temp=input("不妨猜一下zxp现在心里想的是哪个数字：")
if isinstance(temp,int):    
    guess=int(temp)
    while guess != secret:
        if guess == secret:
            print("卧槽，你是zxp心里的蛔虫吗？！")
            print("哼，猜中也没有奖励")
        else:
            if guess > secret:
                print('大了大了')
            else:
                print("小了小了！sb")
        temp=input("猜错啦，请重新输入：")
        guess=int(temp)
else:
    print('输入类型有误')
print("Game over")
