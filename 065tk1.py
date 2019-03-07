from tkinter import *

def callback():
    var.set("吹吧，我才不信你")

root = Tk()

frame1= Frame(root)
frame2= Frame(root)

var = StringVar()
var.set("您所下载的影片含有未成年人限制的内容,\n未满18的青少年禁止访问")

textLabel = Label(frame1,
                  textvariable = var,
                  justify = LEFT)
textLabel.pack(side = LEFT)


photo = PhotoImage(file = "18.gif")
imageLabel = Label(frame1, image = photo)
imageLabel.pack(side =  RIGHT)

theButton = Button(frame2, text = "我已满18周岁", command = callback)
theButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)

mainloop()
