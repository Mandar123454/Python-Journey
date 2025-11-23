# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Mandar" # global scope (available inside and outside functions)

def display_name():
    name = "Kajbaje" # local scope (available only inside this function)
    #name = "Kajbaje" # for checking
    print(name)

display_name()
print(name)

# Rules
# L = Local
# E = Enclosing
# G = Global
# B = Built-in