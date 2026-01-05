# Write a python program to save a simple inquiry form data to a file name called formdata.txt.

# Form details (name, age, qualification, description, hobby, and interest, etc.)

print("Inquiry Form")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
qualification = input("Enter your qualification: ")
hobby = input("Enter your hobby: ")
interest = input("Enter your interest: ")

with open("formdata.txt", "w") as file:
    file.write(f"Name: {name}\nAge: {age} \nQualification: {qualification} \nHobby: {hobby} \nInterest: {interest}")


