#Our main function: where the application logic goes
def main():
    
    #tells the user what our program does
    print("This program illustrates a chaotic function")
    
    #Get input from the user.  Note that we leave a space after the colon.
    user_response = input("Enter a number between 0 and 1: ")
    number_of_loops = input("How many times should the program loop: ")
    
    #Right now, the user_input variable is just a string.  In order to be
    #useful, we need to convert that string to an decimal.  However, not all
    #strings can be converted to decimals.  To account for this, we must
    #place a try/except block around this action.
    try:
        seed = float(user_response)
        number_of_loops = int(number_of_loops)
        
    except:
        
        #This block of code will only execute if Python couldn't convert
        #the user's response into an integer.  We could try to handle 
        #this problem more intelligently, but for now, we'll just print
        #an error and exit.
        print("There was a problem reading your input.  ")
        print("The program will now exit.")
        return  
    
    #loop 10 times.
    for i in range(number_of_loops):
        
        #modify our seed value
        seed = 3.9 * seed * (1 - seed)
        
        #output the current value of our seed
        print(seed)
    
    #we're done with the loop, let the user know that the program is finished
    print("Program complete.")

#if we're running this file directly, call our main function
if __name__ == '__main__':
    main()
