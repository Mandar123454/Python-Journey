from tkinter import *

# label = an area widget that holds text and/or and image within a window

window = Tk()

photo = PhotoImage(file='69.5_Image.png')

# label = Label(window,text="Hello World",font=('Arial',40,'bold'),fg='green') # fg means foreground or font color
# label = Label(window,
#               text="Hello",
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='bottom')
label = Label(window,
              text="bro, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=0,y=0)
#label.place(x=100,y=100)

window.mainloop()