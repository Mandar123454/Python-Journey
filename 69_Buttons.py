from tkinter import *

# buttons = you click it, then it does stuff

count = 0

def click():
    #print("You clicked the button!")
    global count
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file='70.5_Design.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE, # we can set also disabled
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()