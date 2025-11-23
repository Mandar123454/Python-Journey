# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# indexing

# start
name = "Mandar Kajbaje"
#first_name = name[0]
#print(first_name)
#first_name = name[1]
#print(first_name)
#first_name = name[2]
#print(first_name)
#first_name = name[6] # because of empty space nothing is in output
#print(first_name)

# stop
#first_name = name[0:6]
#print(first_name)

#first_name = name[:6]
#print(first_name)

#first_name = name[:6]
#last_name = name[7:14]
#print(last_name)

#last_name = name[7:]
#print(last_name)

# step
first_name = name[:6]
last_name = name[7:]
#funky_name = name[0:14:3]
#funky_name = name[::3]
#reversed_name = name[::-1]

#print(funky_name)
#print(reversed_name)

# slice

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #7 is g and -4 is e from reverse

print(website1[slice])
print(website2[slice])