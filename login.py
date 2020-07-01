from tkinter import *

root = Tk()
root.title("Login")
root.geometry('300x200')


user_lbl = Label(root, text="Username")
pass_lbl = Label(root, text="Password")
user_entry = Entry(root)
pass_entry = Entry(root)

user_lbl.grid(row=0, column=0)
user_entry.grid(row=0, column=1)
pass_lbl.grid(row=1, column=0)
pass_entry.grid(row=1, column=1)

root.mainloop()