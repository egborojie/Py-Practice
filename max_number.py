#!/user/bin/python3
#how to find the max number on a list
numbers = [12, 3, 50, 5, 600]
#creat a variable to store the max number. assume it's index 0
max = numbers[0]
#Use for loop to intirate through the list of numbers
for number in numbers:
    if number > max:
#assingn the maximum number from the list to max.
        max = number
print(max)
