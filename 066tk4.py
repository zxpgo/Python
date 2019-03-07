from tkinter import *

root = Tk()

LANGS =[
    ('python', 1),
    ('Per1', 2),
    ('Ruby', 3),
    ('Lua', 4)
    ]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    b =  Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
    b.pack(fill=X)


mainloop()
