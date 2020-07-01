''' This program demonstrates how to set up a basic GUI using Tkinter. '''

from tkinter import *

root = Tk()
root.title("My first GUI")
root.geometry('400x300')

header_frame = Frame(root, width=400, height=30, bg='#ff0000')
header_frame.grid_propagate(0)
header_frame.grid(sticky=N, columnspan=2)
greeting_lbl = Label(header_frame, text="Welcome!", bg='#ff0000', fg='#ffffff', font=('Calibri', 20))
greeting_lbl.place(relx=.5, rely=.5, anchor="center")


left_frame = Frame(root, width=200, height=20, padx=10)
left_frame.grid_propagate(0)
left_frame.grid(row=1, column=0)
right_frame = Frame(root, width=200)
right_frame.grid(row=1, column=1)

lbl = Label(left_frame, text="asdasd")
lbl.grid()

lbl2 = Label(right_frame, text="mnbvcx")
lbl2.grid()


root.mainloop()