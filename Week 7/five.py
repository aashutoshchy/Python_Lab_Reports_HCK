with open("data.txt", "r") as file:
    data = file.read()
    text = "This is a sample file for question No. five"
    words = text.split()
    print("The longest word is: ", max(words, key=len))
    print("The shortest word is: ", max(words, key=len))
    print("The shortest word is: ", max(words, key=len))


    