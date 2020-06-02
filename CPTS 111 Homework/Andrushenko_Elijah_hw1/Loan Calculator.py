#Assignment: Loan Calculator
#
#Description: A program that calculates your entered loan values
#
#Author: Elijah Andrew Andrushenko
#WSU ID: 011476324
#Completion Time: 4 Hours
#
#
#In completing this program, I obtained help or worked with the following:
#Ali Al-Kefly and I referenced back to the bmi calculator that we did in lab





def main():
    
    #Prompt the user for their Total Loan Amount
    loan_amount = input("Enter your Total Loan Amount in dollars: ")

    #Prompt the user for their Annual Interest Rate
    interest_rate = input("Enter your Annual Interest Rate in percent: ")

    #Prompt the user for their Loan Duration
    loan_duration = input("Enter your Loan Duration in years: ")

    #Convert user inout into floats for calculation
    try:
        loan_amount = float(loan_amount)
        interest_rate = float(interest_rate)
        loan_duration = float(loan_duration)
    except:
        print("There was an error reading your input")
        print("The program will now exit.")
        return

    #Calculate Monthly Interest Rate
    mir = (interest_rate) / (12 * 100)

    #Output the Monthly Interest Rate
    print("Your Monthly Interest Rate is", mir)

    #Calculate Monthly Payment
    mp = (loan_amount * mir) / 1 - (1 + mir)

    #Output the Monthly Payment
    print("Your Monthly Payment i", mp)
    

    
if __name__ == '__main__':
    main()

        
    
