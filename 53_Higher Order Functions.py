# Higher Order Function = a function either:
#                         1. accepts a function as an argument
#                             or
#                         2. returns a function
#                          (In python, functions are also treated as objects)

# 1st part

# def loud(text):
#     return text.upper()
#
# def quite(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quite)

# 2nd part

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))