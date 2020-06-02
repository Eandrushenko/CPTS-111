#Our main function: where the application logic goes
def main():
    
    #Prompt the user for their height
    height_inches = input("Please enter your height in inches: ")
    
    #Prompt the user for thier weight
    weight_pounds = input("Please enter your weight in lbs: ")

    #Convert user input into floats for calculation
    try:
        height_inches = float(height_inches)
        weight_pounds = float(weight_pounds)
    except:
        print("There was a problem reading your input.   ")
        print("The Progrm will now exit.")
        return

    
    #calculate this person's BMI.  The symbols mean the following:
    # *  = multiply
    # /  = float division
    # ** = exponentiation
    #
    #for a complete listing of numeric operation, see the table on page 58
    bmi =  (weight_pounds * 703) / (height_inches ** 2)
    
    #output the person's BMI along with their weight classification
    print("Your BMI is:", bmi)
    
    #output something different based on their BMI.  The IF statement below
    #starts with the smallest case and works itself up.  Doing so prevents
    #more messy logic problems.  The program flow of a logic statement is
    #always linear.  That is, evaluation always begins with the first IF.
    #When that fails, the program then checks the first ELIF, then the
    #second and so on.  If nothing matches, the program will evaluate the
    #ELSE clause.
    if bmi < 18.5:
        print("According to your BMI, you are underweight.")
        
    #if the BMI is greater than 18.5, then check to see if it's less than 24.9
    elif bmi < 24.9:
        print("According to your BMI, you are of normal weight")
    
    #if the BMI is greater than 24.9, check to see if it's less than 29.9
    elif bmi < 29.9:
        print("According to your BMI, you are overweight")
    
    #ELSE is a catch-all clause.  In our case, it will catch all weights that are
    #greater than 29.9
    else:
        print("According to your BMI, you are obese")          
    
    #we're done calculating BMI, let the user know that the program is finished
    print("Program complete.")
    

#if we're running this file directly, call our main function
if __name__ == '__main__':
    main()
