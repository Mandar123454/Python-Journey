# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True) # it is ued to change daemon to non daemon or non daemon to daemon and it should not work when running the program, actually use before the start function
# print(x.isDaemon()) # used to check if a thread is a daemon or not it will return true or false

answer = input("Do you wish to exit?")