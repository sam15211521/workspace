from tkinter import *
from PIL import ImageTk, Image

img = 0 #tells what picture you are on
   

def back():         #makes the pictures go in reverse.
    global img
    global my_label
    global button_next
    global button_back
    if img <= -len(image_lst):
        img = 0
    my_label.grid_forget()
    img -=1
    my_label =Label(image = image_lst[img])
    my_label.grid(row=1, column=1, columnspan=3)

def forward():  #makes the pictures go forward
    global img
    global my_label
    global button_next
    global button_back
    if img >= len(image_lst)-1:
        img = -1
    my_label.grid_forget()
    img +=1
    my_label =Label(image = image_lst[img])
    my_label.grid(row=1, column=1, columnspan=3)


root = Tk()
root.title("Image Viewer")

#the location of all the images and making them variables

my_image1 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/attraction charge.png'))
my_image2 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/attraction distance.png'))
my_image3 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/peridic table.png'))

#image list
image_lst = [my_image1, my_image2, my_image3]


#defining buttons

button_back = Button(root, text = "<<", command =back)
button_next = Button(root, text = ">>", command= forward)
button_exit = Button(root, text = "Exit Program", command = root.quit)

#defining where the image goes
my_label = Label(image = image_lst[img])

#placing widgets on the window
my_label.grid(row=1, column=1, columnspan=3)

button_back.grid(row=2, column = 1)
button_exit.grid(row=2, column=2)
button_next.grid(row=2, column=3)



root.mainloop()