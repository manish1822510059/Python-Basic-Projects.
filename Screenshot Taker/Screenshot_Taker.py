import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Screenshort Taker')
root.resizable(False,False)

canvas1 = tk.Canvas(root,width = 300,height = 300)
canvas1.pack()

def myscreenshort():
    sc = pyautogui.screenshot()
    sc.save(r'C:\CodeWithManish\tkinter\Python sft\Screenshot Taker\screenshot1.png')

myButton = tk.Button(text="Take Screenshort",command = myscreenshort,bg = 'red',fg = 'white', font = 15)
canvas1.create_window(150,150,window=myButton)

root.mainloop()