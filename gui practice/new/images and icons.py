from tkinter import *

from PIL import ImageTk, Image   #PIL is Pillow for inserting images into Tk

root = Tk()
root.title("Icons")
#placing images in the icon
root.iconbitmap('C:/Users/sam15/Documents/workspace/gui practice/new/icon.ico')



# placing the image

my_img = ImageTk.PhotoImage(Image.open("C:/Users/sam15/Documents/workspace/gui practice/new/BAROMET.jpg"))


#buttons

button_quit = Button(root, text ="Exit Program", comman = root.quit)
image_box = Label(image=my_img)         #puts the image into an object that is usable widget

#placing in winwo
button_quit.pack()
image_box.pack()                #packs the image widget into the window





root.mainloop()
