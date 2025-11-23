# nested loops = The "inner loop" will finish all of it's iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
coloumns = int(input("How many coloumns ?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(coloumns):
        print(symbol, end="")
    print()