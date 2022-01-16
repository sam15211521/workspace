from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slider Bars")
root.geometry("400x400")

def slide():

    my_label= Label(root, text= slider.get()).pack()
    root.geometry(str(hor_slider.get()) +'x'+str(slider.get()))

#def self_slide():

slider = Scale(root, from_ = 400, to=200)
hor_slider = Scale(root, from_ = 100, to=400, orient=HORIZONTAL)

my_label = Label(root, text = slider.get()).pack()


my_btn = Button(root,  text="change", command = slide).pack()



slider.pack()
hor_slider.pack()



root.mainloop()