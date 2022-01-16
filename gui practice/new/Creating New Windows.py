from tkinter import *


root = Tk()
root.title('making new windows')


def start_top():
    top = Toplevel()
    lbl = Label(top, text = 'Hello World').pack()
    end_button=Button(top,text ="kill program", command = top.destroy).pack()
    stop_button = Button(root, text = "destroy", command = root.destroy).pack()

Button(root, text = "start second window", command=start_top).pack()



root.mainloop()