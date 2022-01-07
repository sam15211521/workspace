from tkinter import *
window = Tk()
greeting = Label(window, foreground= "DarkRed", background="#34A2FE", text = "Hello, Tkinter", width = 10, height = 5)
greeting.pack()
entry = Entry(fg ="white", bg ="black", width = 10)
entry.pack()
button = Button(text = "Click me!", width = 10, height=5, bg="blue", fg="ForestGreen")
button.pack()
window.mainloop()