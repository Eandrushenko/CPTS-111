#Assignemnt: Turtle Graphics Shape Generator Homework 4
#
#Description: A program that lets the user draw circles or sqaures as well as affect the size and how many can be drawn
#
#Author: Elijah Andrew Andrushenko
#WSU ID: 011476324
#Completion Time: 2 and a half hours spent
#
#
#In completing this program, I obtained help or worked with the following:
#Nobody


#Get turtle
from turtle import *

#Title and directions
print("*** Turtle Graphics Shape Generator ***")
print("1. Draw Squares")
print("2. Draw Circles")
#Prompt the user to choose circles or sqaures
selection = int(input("Selection: "))
#variable that affects the size and location of the next shapes drawn
counter = 0

#If the user chose 1 then draw squares and prompt the user the size and amount
if selection == 1:
    square_num = int(input("Enter number of squares to draw: "))
    square_width = int(input("Enter a starting square width: "))
    for square_num in range(square_num):
        forward(square_width + counter)
        left(90)
        forward(square_width + counter)
        left(90)
        forward(square_width + counter)
        left(90)
        forward(square_width + counter)
        penup()
        forward(10)
        right(90)
        forward(10)
        right(180)
        pendown()
        counter += 20
#If the user chose 2 then draw circles and prompt the user size and amount        
elif selection == 2:
    circle_num = int(input("Enter number of circles to draw: "))
    circle_radius = int(input("Enter a starting circle radius: "))
    for circle_num in range(circle_num):
        circle(circle_radius + counter)
        penup()
        right(90)
        forward(10)
        left(90)
        pendown()
        counter += 10
#If the user didn't choose 1 or 2 tell the user to do so      
else:
    print("You did not enter a valid number, please try again")
