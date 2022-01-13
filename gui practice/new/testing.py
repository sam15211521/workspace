from tkinter import *
 
def delete():
    mylabel.destroy()
 
root = Tk()
root.geometry('150x100')
 
mylabel = Label(root, text = "This is some random text")
mylabel.pack(pady = 5)
 
mybutton = Button(root, text = "Delete", command = delete)
mybutton.pack(pady = 5)
 
root.mainloop()