color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("four.txt", "w") as file:
    for colors in color:
        file.write(f" {colors}")