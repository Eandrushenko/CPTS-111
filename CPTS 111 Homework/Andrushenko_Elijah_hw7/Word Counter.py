#Assignment: Word Counter
#
#Description: This program measures how many paragraphs, words, lines, and characters in a text file.
#
#Author: Elijah Andrushenko
#WSU ID: 011476324
#Completion Time: 6-7 hours
#
#
#In completing this program, I obtained help from or worked with the following:
#Nobody


#Obtain the file and the file we are parsing
file_name = input("Please Enter a file to parse: ")
parse_name = input("Please Enter a destination file: ")
print("Program Complete.")
file = open(file_name, 'r')
parse = open(parse_name, 'w')
lines = file.readlines()

#Lists used in the functions below
my_list = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
my_list6 = []
count = 1

#function used to find the paragraph count
def paragraph():
    for line in lines:
        line = line.strip()
        line = line.split('\n')
        if len(line[0]) == 0:
            my_list6.append(line)
    result = (len(my_list6))
    return result

#function used to find all the characters
def total_char1():
    for line in lines:
        line = line.strip()
        for letters in line:
            my_list.append(letters)
    total = (len(my_list))
    return total

#function used to find all characters excluding spaces
def total_char2():
    for line in lines:
        line = line.strip()
        for letters in line:
            if letters != (" "):
                my_list2.append(letters)
    total = (len(my_list2))
    return total

#function used to find the number of words in the text file
def word_count():
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        for words in line:
            my_list3.append(words)
    total = (len(my_list3))
    return total

#function used to find the number of line in the text file
def line_count():
    for line in lines:
        line = line.strip()
        line = line.split('\n')
        my_list4.append(line)
    total = (len(my_list4))
    return total

#variable for the overflowing lines
finder = 0
j = 0

#output file results
for line in lines:
    line = line.strip()
    print(count, line, file=parse)
    count += 1
border = "--------------------------------------------------------------------------------"
print(border, file=parse)
print("paragraphs:", paragraph() + 1, file=parse)
print("words:", word_count(), file=parse)
print("characters (no spaces):", total_char2(), file=parse)
print("characters (with spaces):", total_char1(), file=parse)
print("total lines:", line_count(), file=parse)
print("overflowing lines:", end=" ",file=parse)

#program to find the overflow lines
#could not figure out how to successfully withdraw the value using a function
for line in lines:
    line = line.strip()
    line = line.split('\n')
    finder += 1
    if len(line[0]) >= 80:
        my_list5.append(finder)

my_list5.reverse()
while j < len(my_list5):
    popped = my_list5.pop()
    print(popped, end=" ", file=parse)

#close the files
file.close()
parse.close()
