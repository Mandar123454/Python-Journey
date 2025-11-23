# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Mandar",18,"male")

print(student.count("Mandar"))
print(student.index("male"))

for x in student:
    print(x)

if "Mandar" in student:
    print("Mandar is here!")
