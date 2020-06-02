#Assignment (Guess My Number!)
#
#Description: (A program that has you guess what number it has using higher and lower)
#
#Author: (Elijah Andrew Andrushenko)
#WSU ID: (011476324)
#Completion Time: (Half an hour on part)
#
#
#In completing this program, I obtain help or worked with the following:
#Nobody

#Import random number to generate a new random number everytime
from random import *
computer_number = randint(0, 100)

#Insert a Boolean variable so when you guess the correct number
#It wont loop forever
stopper = True

#Explain the game to the user
print("Guess the computer's number")
print("The computer will tell you if your entered number is higher or lower than the computer's number.")
print("Hint: It is only between 0 and 100")
print("......")

#Explain the game to the user
guess = int(input("Guess a number: "))

#Have a while loop so it will constantly correct you when you guess
#incorrectly and have you reguess
#It will also stop working if you dont enter an integer between 0 and 100
while guess <= 100 and guess >= 0 and stopper == True:
    if guess == computer_number:
        print("You did it you correctly guessed the right number!")
        print("The computer's number was", computer_number)
        stopper = False
    elif guess < computer_number:
        print("HIGHER")
        guess = int(input("Guess another number: "))
    elif guess > computer_number:
        print("LOWER")
        guess = int(input("Guess another number: "))
        

        

        
