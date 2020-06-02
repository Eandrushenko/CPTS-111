#Assignment (Guess My Number!)
#
#Description: A program that guesses your number in a very time consuming manor
#
#Author: (Elijah Andrew Andrushenko)
#WSU ID: (011476324)
#Completion Time: (2 hours)
#In completing this prgram, I obtained help or worked with the following:
#Nobody

#Prompt the user for a number
guess = int(input("Enter a number between 0-100: "))
#Explain the user how to enter appropriate values
print("If my guess is incorrect say H or L")
print("Say YES if it is your number")
print('\n')
#variable that affects what number is being guessed
num_var = int(50)
#Boolean variable that stops when 'YES' is answer so there is no infinate loop
stopper = True
#asks the user higher lower or yes
print(num_var)
answer = input("Is this your number? ")

#loop so I dont have to enter 100 if statements
while answer == 'H' and stopper == True:
    num_var += 1
    print(num_var)
    answer = input("Is this your number? ")
    #Ends the loop
    if answer == 'YES':
        print("END OF GAME")
        stopper = False
#the same as the loop above only decreasing instead of increasing
while answer == 'L' and stopper == True:
    num_var -= 1
    print(num_var)
    answer = input("Is this your number? ")
    if answer == 'YES':
        print("END OF GAME")
        stopper = False
    
