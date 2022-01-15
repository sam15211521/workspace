from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
#from tkinter import messagebox


root = Tk()
root.title("Message Boxes")

def popup():                #title of the box       message of the box
    responce = messagebox.askquestion("This is my Popup box", "Hello World", )
    Label(root, text = responce).pack()
    if responce == "yes":
        Label(root,text="you clicked yes").pack()
    else:
        Label(root,text="you clicked no").pack()
# message boxes: showinfo, showwarning, showerror, askquestion, askokcancle, askyesno


Button(root, text ='Popup', command = popup).pack()





root.mainloop()