from tkinter import *

root = Tk()
frame1=Frame(root)
frame1.pack()

photo = PhotoImage(file="18.gif")
Label(frame1, image=photo).grid(row=0, column=2, rowspan=2, padx=10)

Label(frame1, text="用户名：").grid(row=0, sticky=W)
Label(frame1, text="密码：").grid(row=1, sticky=W)

Entry(frame1).grid(row=0, column=1)
Entry(frame1, show="*").grid(row=1, column=1)

frame2= Frame(root)
frame2.pack()
Button(frame2, text="登陆", command=root.quit).grid(row=2,padx=20, pady=10)
Button(frame2, text="注册", command=root.quit).grid(row=2, column=1,pady=10)

mainloop()
