#text = "Yooooooo\nThis is some text\nHave a good one!\n"
#text = "Uh oh! This texy has been overwritten"
text = "Have a nice day! See ya"

with open('34.5_test.txt', 'a') as file:
    file.write(text)