print("*** 2x2 Matrix Calculator ***")
print("1. Multiply two matrices together")
print("2. Find the inverse of a matrix")

selection = int(input("Choose an option: "))
print("\n")


if selection == 1:               
    print("Matrix #1")
    one_a = float(input("Enter a number for spot A: "))
    one_b = float(input("Enter a number for spot B: "))
    one_c = float(input("Enter a number for spot C: "))
    one_d = float(input("Enter a number for spot D: "))

    print("Matrix #2")
    two_a = float(input("Enter a number for spot A: "))
    two_b = float(input("Enter a number for spot B: "))
    two_c = float(input("Enter a number for spot C: "))
    two_d = float(input("Enter a number for spot D: "))

    three_a = ((one_a * two_a) + (one_b * two_c))
    three_b = ((one_a * two_b) + (one_b * two_d))
    three_c = ((one_c * two_a) + (one_d * two_c))
    three_d = ((one_c * two_b) + (one_d * two_d))

    print("\n")
    print("--- Solution Matrix ---")
    print("In spot A:", three_a)
    print("In spot B:", three_b)
    print("In spot C:", three_c)
    print("In spot D:", three_d)

    stop = int(input("exit: "))
elif selection == 2:
    print("Enter your matrix values")
    one_a = float(input("Enter a number for spot A: "))
    one_b = float(input("Enter a number for spot B: "))
    one_c = float(input("Enter a number for spot C: "))
    one_d = float(input("Enter a number for spot D: "))
    multiplier = (1/ ((one_a * one_d) - (one_b * one_c)))

    inverse_a = (multiplier * one_d)
    inverse_b = (multiplier * (-1 * one_b))
    inverse_c = (multiplier * (-1 * one_c))
    inverse_d = (multiplier * one_a)
    print("\n")
    print("---Inverse of Matrix---")
    print("In spot A:", inverse_a)
    print("In spot B:", inverse_b)
    print("In spot C:", inverse_c)
    print("In spot D:", inverse_d)


              
