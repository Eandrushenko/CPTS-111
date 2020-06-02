running_total = 0
user_input = 0
stopper = True
index = 0

while user_input >= 0 and stopper == True:
    user_input = int(input("Enter a Number: "))
    running_total += user_input
    index += 1
    if user_input < 0:
        running_total -= user_input
        index -= 1
        stopper = False
        print("Average =", running_total / index)
        




