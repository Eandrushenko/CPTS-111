my_list = [12, 15, 9, 7, 4, 3, 4, 8, 19, 1, 986435, 9908, -9, 0]
sort_list = []
small = 9999999
index = 0
print("Original List: ", my_list)

while len(my_list) > 0:
    small = my_list[0]
    index = 0
    counter = 0
    for items in my_list:
        if items < small:
            small = items
            index = counter
        counter += 1
    sort_list.append(small)
    del my_list[index]

print("Sorted List: ", sort_list)


            



