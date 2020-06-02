print('***Simple Calculator***')
left_value = float(input("Enter left value: "))
operator = input("Enter operator: ")
right_value = float(input("Enter right value: "))

if operator == '*':
    answer = left_value * right_value
elif operator == '/':
    answer = left_value / right_value
elif operator == '+':
    answer = left_value + right_value
elif operator == '-':
    answer = left_value - right_value

print(left_value, operator, right_value, '=', answer)

                    
    
