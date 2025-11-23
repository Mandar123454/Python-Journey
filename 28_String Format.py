
# str.format() = optional method that gives users more
#                control when displaying output

# Placeholder

animal = "cow"
item = "moon"

#print("the "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format("cow","moon"))
#print("The {} jumped over the {}".format(animal,item))  # {} known as placeholder
#print("The {} jumped over the {}".format(item,animal)) # inserting values to placeholder is known as positional argument
#print("The {0} jumped over the {1}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item))
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument
#print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))
#print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))
#print("The {1} jumped over the {1}".format(animal,item))

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

# Padding

# name = "Mandar"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}".format(name)) # makes more spaces in o/p
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

# formatting numbers

# number = 3.14159
#
# #print("The number pi is {:.2f}".format(number)) # f is floating point number
# print("The number pi is {:.3f}".format(number))

number = 1000

#print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) # binary
print("The number is {:o}".format(number)) # octal
print("The number is {:X}".format(number)) # hexadecimal
print("The number is {:E}".format(number)) # scientific notation
