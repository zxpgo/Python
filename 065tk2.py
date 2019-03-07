from tkinter import *

root = Tk()

photo = PhotoImage(file = "bg.gif")
textLabel = Label(root,
                  text = "学Python",
                  justify = LEFT,
                  image = photo,
                  compound = CENTER,
                  font = ("华康少女字体",28),
                  fg = "yellow")
textLabel.pack(side = LEFT)


mainloop()
