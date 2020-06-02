#Assignment: Final Programming Test
#
#Description: This program is made to find my final grade
#
#Author: Elijah Andrushenko
#WSU ID: 011476324
#Completion Time: 1 hour 30 minutes
#
#
#In completing this program, I obtained help or worked with the following:
#Nobody

#obtain the homework and labs
file_name1 = input("Enter your homework file: ")
file_name2 = input("Enter yor labs file: ")

#open the homework file
file1 = open(file_name1, 'r')
lines = file1.readlines()

#set variable that will be useful in the future
my_list1 = []
my_list2 = []
total_score1 = 0
total_score2 = 0

#put the homework information into a list
for line in lines:
    line = line.strip()
    line = int(line)
    my_list1.append(line)

#reverse list so I can pop the grading weight easily
my_list1.reverse()
weight1 = my_list1.pop()

#add the rest of the items in the list
for items in my_list1:
    total_score1 += items

#multiply the amount of items in the list by 100 since they are all out of 100
perfect_score1 = len(my_list1) * 100

#Divide my total score by the the possible score to find the % and then multiply by the weight
score_division1 = (total_score1 / perfect_score1)
homework_score = (score_division1 * weight1)
file1.close()

#do the same with the labs file as what was done with the homework file just
#different values this time
file2 = open(file_name2, 'r')
lines2 = file2.readlines()

for line2 in lines2:
    line2 = line2.strip()
    line2 = int(line2)
    my_list2.append(line2)

my_list2.reverse()
weight2 = my_list2.pop()

for items2 in my_list2:
    total_score2 += items2

perfect_score2 = len(my_list2) * 100
score_division2 = (total_score2 / perfect_score2)
labs_score = (score_division2 * weight2)
file2.close()

#add the two scores to get my final grade
final_grade = homework_score + labs_score

#formating variables
space = "          "
space2 = "      "
space3 = "            "

#end results printed out to look nice
print("Category",space,"Raw Score",space,"Weight")
print(file_name1,space2,"%05.2f"%(homework_score),"%",space3,"%05.2f" %(weight1),"%")
print(file_name2,space,"%05.2f"%(labs_score),"%",space3,"%05.2f"%(weight2),"%")
print("Final Grade:","%05.2f"%(final_grade),"%")







    

    
