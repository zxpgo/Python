import tkinter as tk

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side = tk.BOTTOM, padx = 100, pady = 10)

        self.hi_there = tk.Button(frame, text = '打招呼', bg = "black", fg = "blue" , command = self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('heilo')
        
    
root = tk.Tk()
app = APP(root)

root.mainloop()
