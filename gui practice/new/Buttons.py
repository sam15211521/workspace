from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!!")
    myLabel.pack()

introduction = Label(root, text = "click the button", padx =50, pady= 4)

myButton = Button(root, text = "Click Me!", bg = "red", padx=2, pady=4, command = myClick)



introduction.pack()
myButton.pack()

root.mainloop()