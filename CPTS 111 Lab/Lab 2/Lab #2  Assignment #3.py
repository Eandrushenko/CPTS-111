try:
#Prompt the user for the time
    starting_hour = input("Enter the starting time hour: ")
    starting_minute = input("Enter the starting time minute: ")
    duration = input("Enter the duration: ")

#Convert strings into integers
    starting_hour = int(starting_hour)
    starting_minute = int(starting_minute)
    duration = int(duration)
except:
    pass

#Convert hours into minutes
starting_hour = (starting_hour) * 60

#Add all the times together
minute_sum = (starting_hour) + (starting_minute) + (duration)
total_time = (minute_sum)

#Convert back into hours
new_hour = total_time // 60
new_hour = new_hour % 12

if new_hour == 0:
    new_hour = 12
    
new_minute = total_time % 60


print("Ending time: " + str(new_hour) + ":" + str(new_minute))

