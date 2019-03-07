from tkinter import *

root = Tk()

menubar = Menu(root)

def callback():
    print('你好')

menubar.add_command(label="Hello", command=callback)
menubar.add_command(label="quit", command=root.quit)

root.config(menu=menubar)


mainloop()
