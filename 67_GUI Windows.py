# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Mandar Kajbaje first GUI program")

icon = PhotoImage(file='68.5_Design.png')
window.iconphoto(True,icon)
# window.config(background="black") # we can give color name or hex color picker
window.config(background="#42d4f5")

window.mainloop() # place window on computer screen, listen for events
