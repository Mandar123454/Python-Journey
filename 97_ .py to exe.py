# windows defender may prevent you from running
# make sure pip and pyinstaller are installed/updated

# cd to directory that contains your .py file
# pyinstaller ...
#                 -F            (all in 1 file)
#                 -w            (removes terminal window)
#                 -i icon.ico   (adds custom icon to .exe)
#                 clock.py      (name of your main python file)

# .exe is located in the dist folder


# take clock program and make a new folder on desktop and paste the code
# take a picture of clock
# convert picture of clock to ico converter to ico (icon.ico)
# go to cmd and cd & paste file path of new folder
# type pyinstaller -F -w -i icon.ico
# then code will execute successfully
# icon.ico image will appear in desktop
# move new folder to recycle bin
# open icon.ico image
# it will show output of code
