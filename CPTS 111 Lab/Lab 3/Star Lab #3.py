from turtle import *
input_file = open ('star.txt', 'r')
lines = input_file.readlines()
for line in lines:
    pieces = line.split(',')
    x = int(pieces[0])
    y = int(pieces[1])
    goto(x,y)
input_file.close()
