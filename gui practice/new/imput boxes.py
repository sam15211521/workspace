from tkinter import *

def turn_off():
    root.destroy()

def entry_click():
    hello ="Hello " + entry_label.get()
    myLabel = Label(root, text = hello)
    myLabel.grid(row=4, column=2)
    


root = Tk()

myLabel= Label(root, text = "Please enter your name.")

entry_label = Entry(root, width =50 )
entry_button = Button(root, text= "Enter", command=entry_click)

turn_off_button = Button(root, text = "Close Window", bg = 'silver',command = turn_off)

myLabel.grid(column=2, row = 1)
entry_label.grid(column= 2, row =2)
turn_off_button.grid(column =3, row = 3, padx =3)
entry_button.grid(column = 1, row = 3, padx = 3)

root.mainloop()