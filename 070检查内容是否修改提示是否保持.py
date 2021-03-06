from tkinter import *
import hashlib

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'I love Fishc.com')
contents = text.get('1.0', END)

def getSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = text.get('1.0', END)
    if sig != getSig(contents):
        print('警报！')
    else:
        print('...')

Button(root, text="检查", command=check).pack()

mainloop()
