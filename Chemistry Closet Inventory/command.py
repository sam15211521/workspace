from cProfile import label
from tkinter import *
def forget_widgets():
    pass

def clear_text(widget):
    widget.delete(0,END)

root = Tk()

text1 = Label(root, text = 'Hello')
entry1 = Entry(root)
button1 = Button(root, text = 'load new screen', command = lambda:[text1.grid_forget(), 
                                                                   entry1.grid_forget(), 
                                                                   button1.grid_forget(),
                                                                   clear_text(entry1),
                                                                   text2.grid(column=1,row=1),
                                                                   entry2.grid(column=1,row=2),
                                                                   button2.grid(column=1,row=3)])
text2 = Label(root, text = 'you did it')
entry2 = Entry(root)
button2 = Button(root, text = 'go back', command= lambda:[text2.grid_forget(), 
                                                          entry2.grid_forget(), 
                                                          button2.grid_forget(),
                                                          clear_text(entry2),
                                                          text1.grid(column=1,row=1),
                                                          entry1.grid(column=1,row=2),
                                                          button1.grid(column=1,row=3),
                                                          exit_button.grid(column=2,row=3)
    ])
exit_button = Button(root,text = 'Exit', command = root.destroy)

text1.grid(column=1,row=1)
entry1.grid(column=1,row=2)
button1.grid(column=1,row=3)

root.mainloop()