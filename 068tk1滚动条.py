from tkinter import *

master = Tk()

theLB = Listbox(master, height=18)
theLB.pack()
for item in ['鸡蛋','鸭蛋','鹅蛋','李狗蛋']:
    theLB.insert(END, item)

theButton = Button(master, text="删除它", \
                    command=lambda x=theLB:x.delete(ACTIVE))
theButton.pack()
#theLB.insert(0, "zxp")


mainloop()
