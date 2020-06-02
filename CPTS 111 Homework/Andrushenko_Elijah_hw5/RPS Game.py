#Assignment: Rock Paper Scissors
#
#Description: A Rock Paper Scissors Game that is semi intelligent
#
#Author: Elijah Andrew Andrushenko
#WSU ID: 011476324
#Completion Time: About 2 Hours
#
#
#In completing this program, I obtained help or worked with the following:
#Nobody


#Title of the game
print("***   Rock   Paper   Scissors   ***")
from random import *

#Store data for statistics
loses = 0
wins = 0
ties = 0

#Keep track of the users move so the computer knows what to counter with
rock = 0
paper = 0
scissors = 0


#Used to stop the while loop when the player hits 'q'
stopper = True

#Allows the player to reply instead of hitting f5 everytime
while stopper == True:

    #prompt the user
    user_input = input("Choose (r)ock, (p)aper, (s)cissors, or (q)uit: ")

    #if the user doesnt hit a valid button tell them they made a mistake
    if user_input != 'r' and user_input != 'p' and user_input != 's' and user_input != 'q':
        print("Please enter a valid value in lower case only. (r, p, s, or q)")

        #When you hit 'q' it gives you the statistics
    if user_input == 'q':
        print("\n")
        print("Game Over")
        print("Computer wins:",loses)
        print("Player wins:",wins)
        print("Ties:",ties)

        #print the opposing counter because it counts paper everytime user enters rock
        print("Rock selected:",paper)
        print("Paper selected:",scissors)
        print("Scissors selected:",rock)

        #stops the while loop
        stopper = False

    #If no favored value computer picks a random choice
    elif rock == paper and rock == scissors and paper == scissors:
        random = randint(1,3)
        
        #1 essentially represent rock 2 for paper and 3 for scissors
        if random == 1:
            if user_input == 'r':
                print("You both choose rock. Tie game.")
                ties += 1
                paper += 1
            elif user_input == 'p':
                print("The computer chooses rock. You win.")
                wins += 1
                scissors += 1
            elif user_input == 's':
                print("The computer chooses rock. You loose.")
                loses += 1
                rock += 1
        elif random == 2:
            if user_input == 'r':
                print("The computer chooses paper. You loose.")
                loses += 1
                paper += 1
            elif user_input == 'p':
                print("You both choose paper. Tie game.")
                ties += 1
                scissors += 1
            elif user_input == 's':
                print("The computer chooses paper. You win.")
                wins += 1
                rock += 1
        elif random == 3:
            if user_input == 'r':
                print("The computer chooses scissors. You win")
                wins += 1
                paper += 1
            elif user_input == 'p':
                print("The compter chooses scissors. You loose.")
                loses += 1
                scissors += 1
            elif user_input == 's':
                print("You both choose scissors. Tie game.")
                ties += 1
                rock += 1

            
            
            
    #If rock is favored the computer chooses paper and all the possible
    #outcomes for the next choice are written out and this is done with
    #paper and scissors as well
    elif rock >= paper and rock >= scissors:
        if user_input == 'r':
            print("You both choose rock. Tie game.")
            ties += 1
            paper += 1
        elif user_input == 'p':
            print("The computer chooses rock. You win.")
            wins += 1
            scissors += 1
        elif user_input == 's':
            print("The computer chooses rock. You loose.")
            loses += 1
            rock += 1
    elif paper >= rock and paper >= scissors:
        if user_input == 'r':
            print("The computer chooses paper. You loose.")
            loses += 1
            paper += 1
        elif user_input == 'p':
            print("You both choose paper. Tie game.")
            ties += 1
            scissors += 1
        elif user_input == 's':
            print("The computer chooses paper. You win.")
            wins += 1
            rock += 1
    elif scissors >= rock and scissors >= paper:
        if user_input == 'r':
            print("The computer chooses scissors. You win")
            wins += 1
            paper += 1
        elif user_input == 'p':
            print("The compter chooses scissors. You loose.")
            loses += 1
            scissors += 1
        elif user_input == 's':
            print("You both choose scissors. Tie game.")
            ties += 1
            rock += 1

        

