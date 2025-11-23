# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to seperate a program into parts

# import messages
#
# messages.hello()
# messages.bye()

# import messages as msg
#
# msg.hello()
# msg.bye()

# from messages import hello,bye
#
# hello()
# bye()

from messages import * # (this one is dangerous)
hello()
bye()

#help("modules")