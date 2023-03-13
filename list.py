#Write a programe that removes a dublicate in our list


list = [20, 2, 2, 5, 3, 3, 3, 5 , 3, 7, 19]
new_list =[]

#now we add numbers not in the new list.
for numbers in list:
    if numbers not in new_list:
        new_list.append(numbers)
print(new_list)
