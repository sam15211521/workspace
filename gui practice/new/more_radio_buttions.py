from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("more buttons")

r =IntVar()
r.set("2")
button = False

modes = [
        ("Pepperoni","Pepperoni"),
        ("Mushroom","Mushroom"),
        ("Cheese","Cheese"),
        ("Onion","Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")


def radio_button(value):
    global screen
    global message_frame
    message_frame.destroy()
    message_frame = LabelFrame(root, padx = 10, pady= 10)
    message_frame.grid(column=1,row=1, columnspan=2)
    if button == True:
        push_the_button("Is the dough ready?")
    screen = Label(message_frame, text =value).grid(row =1)


def push_the_button(value):                     #use to push the button 
    global button
    button = True
    time_screen = Label(message_frame, text = value).grid(row =2)


# sets up diffrent frames for items

radio_frame = LabelFrame(root, padx=10, pady=10)
button_frame = LabelFrame(root, padx = 10, pady = 10)
message_frame = LabelFrame(root, padx = 10, pady= 10)

#places frames on window
radio_frame.grid(column=1, row=2)
button_frame.grid(column=2, row=2)
message_frame.grid(column=1,row=1, columnspan=2)


#sets up radio buttons manuely
###
#Radiobutton(radio_frame, text ="Option 1", variable=r, value=1, command = lambda:radio_button(r.get())).grid(row=1)
#Radiobutton(radio_frame, text ="Option 2", variable=r, value=2, command = lambda:radio_button(r.get())).grid(row=2)
#Radiobutton(radio_frame, text ="Option 3", variable=r, value=3, command = lambda:radio_button(r.get())).grid(row=3)

###

#sets up radio buttons automaticaly
def making_radio_buttons(modes = modes):
    global pizza
    i=1
    for text, mode in modes:
        Radiobutton(radio_frame, text=text, variable = pizza, value = mode,command = lambda:radio_button(pizza.get())).grid(row = i)
        i+=1

making_radio_buttons()

#places buttons
enter_button = Button(button_frame, text = "Enter", padx=5, pady=2, command =lambda:push_the_button("Is the dough ready?")).grid(column = 1, row=1)
quit_button = Button(button_frame, text = "Exit", padx=5, pady=2, command=root.destroy).grid(pady =5, column = 1, row=2)

#places screen frame
screen= Label(message_frame, text =0).grid(column=1)







root.mainloop()