#Our function method: where the application logic goes
def main():
    
    #start with 99 bottles of beer on the wall
    bottles_of_beer = 99
    
    #Make this really easy by using a loop.  Note that we're using a slightly
    #more complicated version of the range function.  Here's the breakdown of
    #the parameters:
    #range(bottles_of_beer, 0, -1)
    #parameter 1        - Start the counter at the number stored in the 
    #(bottles_of_beer)    variable bottles_of_beer
    #                   
    #parameter 2        - End at the number zero
    #(0)           
    #
    #parameter 3        - Step backwards.  That is, start at 99 and count down 
    #(-1)                 to the number zero.
    
    for bottles_left in  range(bottles_of_beer, 0, -1):

    #In most cases we can say bottles
        if bottles_left > 2:
            print(bottles_left, "bottles of beer on the wall,", end=" ")
            print(bottles_left, "bottles of beer")
            print("Take one down and pass it around,", end=" ")
            print(bottles_left -1, "bottles of beer on the wall.\n")

        #When two items are left, we say "bottles" when referring to how
        #Many bottles are on the wall, and "bottle" when referring to how
        #Many bottles remain after we take one down
        elif bottles_left == 2:
            print(bottles_left, "bottles of beer on the wall,", end=" ")
            print(bottles_left, "bottles of beer")
            print("Take one down and pass it around,", end= " ")
            print(bottles_left -1, "bottle of beer on the wall.\n")

        #When only one bottle remains, say "bottle" when referring to how many
        #bottles are on the wall, and "no more" when referring to how many
        #bottles remain after we take the last one down
        else:
            print(bottles_left, "bottle of beer on the wall,", end=" ")
            print(bottles_left, "bottle of beer")
            print("Take one down and pass it around,", end= " ")
            print("No more bottles of beer on the wall.\n")
            
            

            
        
        
        #In this loop, bottles_left will equal the number of bottles that need
        #to be pulled down from the wall
        
        #Print the number of bottles left on the wall.  While I could just use
        #one really long PRINT statement, I've broken it up for two reasons:
        # 1 - It's a long-held standard to try to limit each line of code to 80
        #     characters.  Doing so makes the document easier to print as
        #     wordwrapping in code can get confusing.
        #
        # 2 - To demonstrate Python's "end=" parameter.  Normally, Python
        #     will output a newline ("\n") character at the end of each PRINT
        #     statement.  However, it is often the case that we don't want
        #     a newline character to follow each print.  In these cases, we
        #     use the "end=" parameter.  Doing so substitutes whatever is in
        #     the quotation marks with the newline character.  In this example,
        #     I'm simply substituting a space (" ") for the newline
            
        
        #For the final one, subtract one from the number of bottles left.
        #Note that the variable bottles_left doesn't actually get modified
        #because we aren't saving the value anywhere.   

    #manually print the last line of the song
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    
#if we're running this file directly, call our main function
if __name__ == '__main__':
    main()
