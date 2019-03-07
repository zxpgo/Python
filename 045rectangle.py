class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            #self.name = value #陷入死循环
            #super().__setattr__(name, value)#方法一
            self.__dict__[name] = value#方法二
    def getArea(self):
        return self.width * self.height

            
