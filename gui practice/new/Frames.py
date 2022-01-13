from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Framse per second")
root.iconbitmap('icon.ico')

def destroytheframe():
    global frame
    frame.destroy
    #frame = LabelFrame(root,text = 'You cannot kill me!!', padx = 6, pady = 6)
    #button2= Button(frame, text = "I am not scaired of you", command = root.destroy)
    
def openanendingframe():
    frame = LabelFrame(root,text = 'You cannot kill me!!', padx = 6, pady = 6)
    button2= Button(frame, text = "I am not scaired of you", command = root.destroy)
    frame.pack(padx=10, pady=10)
    button2.pack()

def bothfunctions():
    destroytheframe()
    #openanendingframe()

#widgets
frame = LabelFrame(root, text = 'This is the frame', padx=5, pady=5)
buttons = Button(frame, text ='Click Me!', command = lambda: [frame.destroy, openanendingframe()])


#packing
frame.pack(padx=10, pady=10)
buttons.pack()


root.mainloop()