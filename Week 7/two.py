# Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.

count = 0

with open("PYTHON.TXT", "r") as file:
    data = file.read()
    for ch in data:
        if ch.isupper():
            count += 1

print("The numbe of Uppercase is: ", count)