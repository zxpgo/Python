from tkinter import *

root = Tk()

text = Text(root, width=30, height=5, undo=True, autoseparators=False)
text.pack()

text.insert(INSERT,'I love fishc.com!')

def callback(event):
    text.edit_separator()

text.bind('<Key>', callback)

def show():
    text.edit_undo()

Button(root, text="撤销", command=show).pack()

mainloop()

