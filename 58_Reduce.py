# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y:x + y,letters)
# print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y:x * y,factorial)
print(result)

# reduce means
# ["H","E","L","L","O"] x is H y is E perform x+y
# ["HE","L","L","O"] x is HE y is L perform x+y
# ["HEL","L","O"]
# ["HELL","O"]
# ["HELO"]
