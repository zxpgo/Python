import time as t

class MyTimer():
    #开始计时
    def start(self):
        self.start=t.localtime()
        print("计时开始。。。。")
        
    #停止计时
    def stop(self):
        self.stop=t.localtime()
        self._calc()
        print("计时结束。。。")

    #内部方法，计算运行时间
    def _calc(self):
        self.lasted=[]
        self.prompt("总共运行了")
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.promtp+=str(self.lasted[index])

        print(self.prompt)
        
