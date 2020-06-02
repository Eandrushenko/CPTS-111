from turtle import *

user_input = int(input("Enter Loop Count: "))
counter = 0

for user_input in range(user_input):
    counter += 1
    forward(counter)
    left(90)
