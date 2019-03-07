from tkinter import *

root = Tk()

def callback():
    print('你好')
    
menubar = Menu(root)

openvar = IntVar()
savevar = IntVar()
quitvar = IntVar()

filemenu = Menu(menubar, tearoff=False)
filemenu.add_checkbutton(label="开打", command=callback, variable=openvar)
filemenu.add_checkbutton(label="保存", command=callback, variable=savevar)
filemenu.add_separator()
filemenu.add_checkbutton(label="退出", command=root.quit, variable=quitvar)
menubar.add_cascade(label="文件", menu=filemenu)

editvar = IntVar()

editmenu = Menu(menubar, tearoff=False)
editmenu.add_radiobutton(label="剪切", command=callback, variable=editvar,value=1)
editmenu.add_radiobutton(label="拷贝", command=callback, variable=editvar,value=2)
editmenu.add_radiobutton(label="黏贴", command=callback, variable=editvar,value=3)
menubar.add_cascade(label="编辑", menu=editmenu)

root.config(menu=menubar)


mainloop()
