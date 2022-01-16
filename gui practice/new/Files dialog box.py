from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root =Tk()
root.title('file dialog box')

def file_box_open():
    global my_immage
    root.filename = filedialog.askopenfilename(initialdir = 'c:/Users/sam15/OneDrive/Desktop/programing/workspace/gui practice/new/Sketchbook', title = "Select a File", filetypes=(('.png', '*.png'), ('all files', '*.*')))
    mylabel = Label(root, text = root.filename).pack()
    my_immage = ImageTk.PhotoImage(Image.open(root.filename))
    immage_label=Label(root, image =my_immage).pack()



Label(root, padx = 50, pady =50).pack()
file_open_button = Button(root, text = 'Open Files', command= file_box_open).pack()
exit_button = Button(root, text = 'Exit', command= root.destroy ).pack()





root.mainloop()