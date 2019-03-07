from tkinter import *

root = Tk()

v = IntVar()

Radiobutton(root, text="one", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="two", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="three", variable=v, value=3).pack(anchor=W)

mainloop()
