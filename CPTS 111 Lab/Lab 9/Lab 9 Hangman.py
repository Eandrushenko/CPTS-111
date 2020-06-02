from words import *
from random import *
random_words = choice(possible_words)
word_as_list = list()
current_guess = 0
num_guesses = len(random_words)
correct_guess = False

for letter in random_words:
    word_as_list.append('_')
while current_guess < num_guesses and correct_guess == False:
    has_match = False
    has_dash = False
    print('You have',num_guesses - current_guess,'incorrect guesses left.')
    for letter in word_as_list:
        print(letter,end=' ')
    print('\n')
    user_guess = input("Guess a letter: ")

    for i in range(len(word_as_list)):
        if random_words[i] == user_guess[0]:
            has_match = True
            word_as_list[i] = user_guess[0]
        elif word_as_list[i] == '_':
            has_dash = True
    if has_dash == False:
        correct_guess = True
    if has_match == False:
        current_guess += 1
if correct_guess == True:
    print(random_words)
    print('Congratualtions! You Win!')
else:
    print('You are out of Guesses, You Lose!')
    print('The correct word was:',random_words)
                   
