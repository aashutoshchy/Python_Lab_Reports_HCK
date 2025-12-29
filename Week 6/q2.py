# Add multi-line Docstrings to the function, create a simple function to take user input for “name”, “age” and Qualification.

def my_func():
    '''
    This Function takes name, age and qualification from the user.
    It also prints the details to the console.
    '''
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    qual = input("Enter your Qualification: ")

    print(f"Your Name is {name} and age is {age}. Your Qualification is {qual}")

my_func()
