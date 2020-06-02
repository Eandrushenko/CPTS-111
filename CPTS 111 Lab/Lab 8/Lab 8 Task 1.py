prompt = ('y')
while prompt == 'y':
    test = (input("Enter an expression: "))
    expression = list()
    pieces = test.split(" ")
    for piece in pieces:
        piece.isnumeric()
        if piece.isnumeric():
            piece = int(piece)
            expression.append(piece)
        else:
           right = expression.pop()
           left = expression.pop()
           if piece == '+':
               result = (left + right)
           elif piece == '-':
               result = (left - right)
           elif piece == '/':
               result = (left / right)
           elif piece == '*':
               result = (left * right)

           expression.append(result)
    print("Result", expression.pop())
    prompt = input("Would you like to keep going? (y/n): ")
else:
    print("Program Complete")
            

    


    

