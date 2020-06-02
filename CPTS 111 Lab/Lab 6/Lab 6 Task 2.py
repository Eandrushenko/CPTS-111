user_input = 0
stopper = True
big = 0

while user_input >= 0 and stopper == True:
    user_input = int(input("Enter a Number: "))
    if user_input > big:
        big = user_input
    if user_input < 0:
        stopper = False
        print("The largest number is: ", big)
