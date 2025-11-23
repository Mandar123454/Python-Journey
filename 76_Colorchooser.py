from tkinter import *
from tkinter import colorchooser # submodule

def click():
    # color = colorchooser.askcolor()
    # colorHex = color[1]
    # window.config(bg=colorHex) # change background color
    #window.config(bg=color[1])
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()