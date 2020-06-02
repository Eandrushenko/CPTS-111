def main():
    print("---Simple Stats Program---")

    file_name = input("File name: ")
    file = open(file_name, 'r')
    print("File contents read successfully")
    print('\n')
    lines = file.readlines()
    my_list = []
        
    for line in lines:
        line = line.strip()
        line = int(line)
        my_list.append(line)
            
    my_list.sort()
    stopper = True


    def get_median():
        if len(my_list) % 2 == 0:
            finder1 = len(my_list) / 2
            finder2 = finder1 - 1
            average = ((finder1 + finder2) / 2)
            print("The median is",average)

        elif len(my_list) % 2 != 0:
            finder = len(my_list) // 2
            print("The median is",my_list[finder])
        return

    def get_mean():
        total = 0
        i = 0
        while len(my_list) > i:
            total += my_list[i]
            i += 1
            
        average = total / len(my_list)
        print("The mean is", average)
        return

    def get_frequency():
        return

    def get_mode():
        return

    while stopper == True:
        print("Availble actions:")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("6: Exit Program")
        user_input = int(input("Select an option: "))
        if user_input == 1:
            get_mean()
            print('\n')
        elif user_input == 2:
            get_median()
            print('\n')
        elif user_input == 3:
            get_mode()
            print('\n')
        elif user_input == 6:
            stopper = False
            print('\n')
            print("Program Stopped")
        else:
            print("You did not enter a valid action. Please enter a valid action")
            print('\n')



    file.close()
    return
main()
    
