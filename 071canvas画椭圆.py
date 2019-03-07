from tkinter import *


root = Tk()

w = Canvas(root, width=200, height=100, background='white')
w.pack()

w.create_rectangle(40, 20, 160,80, fill='green', dash=(4,4))#画矩形
#w.create_oval(70, 20, 130, 80, fill='pink')#画圆形
#w.create_oval(40, 20, 160, 80, fill='pink')#画椭圆


w.create_text(100, 50, text="FishC")

mainloop()
