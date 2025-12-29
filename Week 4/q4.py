name = input("Enter your name: ");
age = int(input("Enter your age: "));
qualification = input("Enter your qualification: ");
cNum = input("Enter your Contact number: ");
address = input("Enter your address: ");
email = input("Enter your email: ");
iArea = input("What is your interested area? ");
desc = input("Give your description: ");

salExp = int(input("Enter your salary expectation: "));
if salExp > 20000:
    print("Your work experience must be atleast 2 years.")
    experience = int(input("How much is your experience? "));
    if experience >= 2:
        print("you are shortlisted your enquiry has been recorded, we will notify you, thank you!!")
    else:
        print("Your enquiry has been recorded, we will notify you, thank you!!")
else:
    print("Your enquiry has been recorded, we will notify you, thank you!!")
