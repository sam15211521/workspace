# Import the required library
from tkinter import *

# Create an instance of tkinter frame
win = Tk()

# Define geometry of the window
win.geometry("700x250")

lst = [1,2,3,4,5,6,7,8,9,10]

entry1 = Label(win, text=lst).pack()

win.mainloop()