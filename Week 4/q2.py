posCount = 0
negCount = 0
sum = 0

while True:
    num = int(input("Enter any number: "))

    if num == 0:
        break         

    if num > 0:
        posCount += 1
        sum += num
    elif num < 0:
        negCount += 1
    else:
        continue     

print("Total no. of Positive numbers are ", posCount)
print("Total no. of Negative numbers are ", negCount)
print("Sum of Positive numbers is ", sum)

