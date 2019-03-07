from tkinter import *

root = Tk()

GIRLS = ['西施', '貂蝉', '王昭君', '杨玉环']

v = []

for girl in GIRLS:
    v.append(IntVar())
    c = Checkbutton(root, text= girl, variable= v[-1])
    c.pack(anchor = W)


mainloop()
    
