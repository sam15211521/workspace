from tkinter import *
window = Tk()

label = Label(text = "Name")
entry = Entry()

label.pack()
entry.pack()
window.mainloop()

name = entry.get()
name 
