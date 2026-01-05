# Write a Python program to read an entire text file.

with open("info.txt", "r") as file:
    data = file.read()
    print(data)
