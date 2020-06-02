#Assignment: Blackjack
#
#Description: A Blackjack program that uses cards 2-11 where the uses plays against the computer
#
#Author: Elijah Andrushenko
#WSU ID: 011476324
#Completion Time: 3 hours 30 minutes
#
#
#In completing this program, I obtained help or worked with the following:
#Nobody


from random import *

#Store data
player_deal = 0
player_total = 0
computer_deal = 0
computer_total = 0

#Stoppers
play_again = True
asker = 'h'
stopper = True
stopper2 = True

print("***     Simple Blackjack     ***\n")

asker = input("Would you like to hit (h) or stand (s): ")

#Loop to prompt multiple times    
while play_again == True:

    #What happens when you 'hit'
    if asker == 'h' and stopper == True:
        player_deal = 0
        player_deal += randint(2,11)
        player_total += player_deal
        print("You are dealt a", player_deal)
        print("Your score is:", player_total)

      
      #What happens when you 'BUST'
        if player_total > 21:
            print("Your score is over 21. BUST!")
            print("You lose!")
            stopper = False
            play_again = input("Play again? (y/n): ")
            if play_again == 'y':
                play_again = True
                stopper = True
                stopper2 = True
                player_total = 0
                computer_total = 0
            elif play_again == 'n':
                play_again = False

        #What happens when you Blackjack        
        elif player_total == 21:
            print("Your score is 21. Blackjack! ")
            print("You win!")
            stopper = False
            play_again = input("Play again? (y/n): ")
            if play_again == 'y':
                play_again = True
                stopper = True
                stopper2 = True
                player_total = 0
                computer_total = 0
            elif play_again == 'n':
                play_again = False

        #Prompt when you don't BUST or Blackjack        
        elif player_total < 21:
            asker = input("Would you like to hit (h) or stand (s): ")
            stopper2 = True

    #Initialize computer play after 'stand'        
    elif asker == 's' and stopper2 == True:
        computer_deal = 0
        computer_deal += randint(2,11)
        computer_total += computer_deal
        print("Computer is dealt a", computer_deal)
        print("Computer score is:", computer_total)

        #What happens when computer 'BUST'
        if computer_total > 21 and stopper2 == True:
            print("Computer score is over 21. BUST!")
            print("You win!")
            stopper2 = False
            play_again = input("Play again? (y/n): ")
            if play_again == 'y':
                play_again = True
                stopper = True
                stopper2 = True
                asker = 'h'
                player_total = 0
                computer_total = 0
            elif play_again == 'n':
                play_again = False

        #What happens when computer 'Blackjack'     
        elif computer_total == 21 and stopper2 == True:
            print("Computer score is 21. Blackjack!")
            print("You lose")
            stopper2 = False
            play_again = input("Play again? (y/n): ")
            if play_again == 'y':
                play_again = True
                stopper = True
                stopper2 = True
                asker = 'h'
                player_total = 0
                computer_total = 0
            elif play_again == 'n':
                play_again = False

        #What happens when computer reaches 17 and has a higher score than player   
        elif computer_total >= 17 and computer_total > player_total and stopper2 == True:
            print("Computer stands")
            print("Computer score is", computer_total, "Your score is", player_total)
            print("You lose!")
            stopper2 = False
            play_again = input("Play again? (y/n): ")
            if play_again == 'y':
                play_again = True
                stopper = True
                stopper2 = True
                asker = 'h'
                player_total = 0
                computer_total = 0
            elif play_again == 'n':
                play_again = False
                
        #What happens when computer reaches 17 and has a lower score than player    
        elif computer_total >= 17 and computer_total <= player_total and stopper2 == True:
            print("Computer score is lower than or equal to player score, and is forced to hit")
            computer_deal = 0
            computer_deal += randint(2,11)
            computer_total += computer_deal
            print("Computer is dealt a", computer_deal)
            print("Computer score is:", computer_total)

        #Possible outcomes when cpu over 17 but less than player score
            if computer_total > 21 and stopper2 == True:
                print("Computer score is over 21. BUST!")
                print("You win!")
                stopper2 = False
                play_again = input("Play again? (y/n): ")
                if play_again == 'y':
                    play_again = True
                    stopper = True
                    stopper2 = True
                    asker = 'h'
                    player_total = 0
                    computer_total = 0
                elif play_again == 'n':
                    play_again = False
                
            elif computer_total == 21 and stopper2 == True:
                print("Computer score is 21. Blackjack!")
                print("You lose")
                stopper2 = False
                play_again = input("Play again? (y/n): ")
                if play_again == 'y':
                    play_again = True
                    stopper = True
                    stopper2 = True
                    asker = 'h'
                    player_total = 0
                    computer_total = 0
                elif play_again == 'n':
                    play_again = False
                
            elif computer_total >= 17 and computer_total > player_total and stopper2 == True:
                print("Computer stands")
                print("Computer score is", computer_total, "Your score is", player_total)
                print("You lose!")
                stopper2 = False
                play_again = input("Play again? (y/n): ")
                if play_again == 'y':
                    play_again = True
                    stopper = True
                    stopper2 = True
                    asker = 'h'
                    player_total = 0
                    computer_total = 0
                elif play_again == 'n':
                    play_again = False

#When player says 'n' when prompted to play again                    
if play_again == False:
    print("Thanks for playing!")

        
        
    
    

