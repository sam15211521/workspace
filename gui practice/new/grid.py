from tkinter import *
from typing import Collection

root = Tk()

myLabel = Label(root, text = "Hello this should be in 1")
myLabel1 = Label(root, text = "this should be under it")


myLabel.grid(row=1, column=1)
myLabel1.grid(row=2, column = 1)

root.mainloop()