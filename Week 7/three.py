# Write a program which uses (file read using "open ()" & "with open ()") both.

# Using open()

file = open("info.txt", "r")
data = file.read()
print("Using open(): ")
print(data)
file.close()

#Using with open()
print("Using with open(): ")
with open("info.txt", "r") as file:
    data = file.read()
    print(data)