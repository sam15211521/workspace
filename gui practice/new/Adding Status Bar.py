from tkinter import *
from PIL import ImageTk, Image

img = 0 #tells what picture you are on
   

def back():         #makes the pictures go in reverse. and status grid as well
    global img
    global my_label
    global button_next
    global button_back
    global status
    global status_string

    if img <= -len(image_lst):
        img = 0

    my_label.grid_forget()
    
    img -=1
    
    my_label =Label(image = image_lst[img])
    my_label.grid(row=1, column=1, columnspan=3)
    
    status_string ='image {current} of {total}'.format(current = img+4 if img <0 else img+1, total = len(image_lst))
    status =Label(root, text = status_string, bd = 5, relief= SUNKEN, pady =10, ancor = E)
    status.grid(row=3,column=1, columnspan=3, sticky=W+E)

def forward():  #makes the pictures go forward.  and status grid as well
    global img
    global my_label
    global button_next
    global button_back
    global status
    global status_string

    if img >= len(image_lst)-1:
        img = -1
    
    my_label.grid_forget()
   

    img +=1
    
    my_label =Label(image = image_lst[img])
    my_label.grid(row=1, column=1, columnspan=3)
    
    status_string ='image {current} of {total}'.format(current = img+1, total = len(image_lst))
    status =Label(root, text = status_string, bd = 5, relief= SUNKEN, pady =10, anchor = E)
    status.grid(row=3,column=1, columnspan=3, sticky=W+E)
    




root = Tk()
root.title("Image Viewer")

#the location of all the images and making them variables

my_image1 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/attraction charge.png'))
my_image2 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/attraction distance.png'))
my_image3 = ImageTk.PhotoImage(Image.open('C:/Users/sam15/Documents/workspace/gui practice/new/Sketchbook/peridic table.png'))

#image list
image_lst = [my_image1, my_image2, my_image3]


# status bar
status_string ='image {current} of {total}'.format(current = img+1, total = len(image_lst))
status = Label(root, text = status_string, bd = 5, relief= SUNKEN, pady =10, anchor= E) 


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

status.grid(row=3,column=1, columnspan=3, sticky=W+E)

root.mainloop()