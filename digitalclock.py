from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("My Clock")
label = Label(root,font=('ds_digital',80),background='black',foreground='cyan')
label.pack(anchor="center")

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

time()


root.mainloop()
