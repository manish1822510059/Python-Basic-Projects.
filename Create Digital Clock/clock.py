from tkinter import *
from tkinter.ttk import *

from time import strftime


def clock():
    tick = strftime('%H:%M:%S %p')
    label.config(text=tick)
    label.after(1000, clock)


root = Tk()
root.title('Digital Clock')

label = Label(root, font=('sans', 80),
              background='black', foreground='light blue')
label.pack(anchor="center")
clock()


root.mainloop()
