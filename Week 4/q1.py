#Python program to calculate the sum of all the odd and even numbers within the given range. (Suppose given range is 10)

# Using for Loop
sumOfEven = 0
sumOfOdd = 0

for i in range(2, 10, 2):
    sumOfEven += i
print(sumOfEven)

for i in range(1, 10, 2):
    sumOfOdd += i
print(sumOfOdd)

#Using While Loop
# sumOfEven = 0
# n = 0
# while (n < 10):
#     sumOfEven += n;
#     n += 2;
# print(sumOfEven)

# sumOfOdd = 0
# n = 1
# while (n < 10):
#     sumOfOdd += n;
#     n += 2;
# print(sumOfOdd)