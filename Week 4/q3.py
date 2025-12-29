# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# Using for loop
# for i in range (0, 7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)

# Using While loop
i = 0
while i <= 6:
    if i == 3 or i == 6:
        i += 1
        continue
    else:
        print(i)
    i += 1
