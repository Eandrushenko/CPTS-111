my_list = [1, 2, 8, 0, 7]
small = 99999999999999999999999999999999999
counter = -1
index = 0

for items in my_list:
    counter += 1
    if items < small:
        small = items
        index = counter
        
        
print("Your list is:", my_list)
print("The smallest number in the list is", small, "Found at index", index + 1)
