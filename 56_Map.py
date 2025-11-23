# map() = applies a function to each item in an iterable (list, tuple, etc)
#
# map (function,iterable) # 2 arguments function,iterable

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

# to_euros = lambda data: (data[0],data[1]*0.82)
to_dollors = lambda data: (data[0],data[1]/0.82)

# store_euros = list(map(to_euros, store))
store_dollors = list(map(to_dollors, store))

for i in store_dollors:
    print(i)