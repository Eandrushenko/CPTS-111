file = open('first_names.txt', 'r')
lines = file.readlines()
name = -1
starting_value = 0
value = 1000

while value < 0 or value > 50:
    value = int(input("Enter a value between 0 and 50: "))

while name < (value - 1 ):
    name += 1
    print('Name at', starting_value, ':', lines[starting_value])
    starting_value += 1
    
