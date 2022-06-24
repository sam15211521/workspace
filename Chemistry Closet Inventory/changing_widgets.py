from tkinter import *

def start_button(widgets):
    for widget in widgets:
        widget.grid_forget()


def main():
    root = Tk()
    start = Button(root, text = 'start', command = lambda: start_button(widgets = [start, stop]))
    stop = Button(root, text ='stop', command = root.destroy)
    remember = Button(root,text = 'remember', command = lambda: (start.grid(column= 1, row= 1), stop.grid(column= 1, row = 2)))
    start.grid(column= 1, row= 1)
    stop.grid(column= 1, row= 2)
    remember.grid(column= 1, row= 3)
    root.mainloop()



main()

