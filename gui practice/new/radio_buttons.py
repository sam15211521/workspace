from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio buttons')

r = IntVar() # makes radobuttons variable work
r.set("0")  #sets radiobutton to a specific variable

def clicked(value): #funciton to destroy myLable and replace it with value of the radiobuttion.
    global myLabel

    myLabel.destroy()
    myLabel = Label(label_frame, text = value)
    myLabel.grid()

# making frames for the buttons
radio_frame = LabelFrame(root, text = 'number values', padx = 5, pady =5)
button_frame = LabelFrame(root, text = 'All the buttons', padx = 5, pady =5)
label_frame = LabelFrame(root, padx = 20, pady =5)


# looping radiobuttions in 


#manuely adding a radiobuttion
Radiobutton(radio_frame,text = "Option1", variable = r, value = 1, command = lambda: clicked(r.get())).grid(column=1, row=1)
Radiobutton(radio_frame,text = "Option2", variable = r, value = 2, command = lambda: clicked(r.get())).grid(column=1, row=2)



my_button = Button(button_frame, text = "click me", command=lambda: clicked(3))

myLabel = Label(label_frame, text = r.get())


radio_frame.grid(column=2,row=1)
button_frame.grid(column=2,row=2)
label_frame.grid(column=1, row=1, rowspan=2)
myLabel.grid(column =1, row = 1)
my_button.grid(column =1, row = 1)


root.mainloop()