# sort() method   = used with lists
# sort() function = used with iterables

# level 1
# students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]
students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

# students.sort()
# students.sort(reverse=True)

# sorted_students = sorted(students)
# sorted_students = sorted(students,reverse=True)
#
# for i in students:
#     print(i)

# for i in sorted_students:
#     print(i)

# level 2

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs", "C", 78)]

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

#students.sort()

#grade = lambda grades:grades[1]
# students.sort(key=grade)
#students.sort(key=grade,reverse=True)

#age = lambda ages:ages[2]
# students.sort(key=age)
#students.sort(key=age,reverse=True)

age = lambda ages:ages[2]
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)