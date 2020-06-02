def main():

    import turtle
    import cmath


    first_x = int(input("Enter first x coordinate: "))
    first_y = int(input("Enter first y coordinate: "))
    first_coord = (first_x, first_y)
    second_x = int(input("Enter second x coordinate: "))
    second_y = int(input("Enter second y coordinate: "))

#drawing axis
    turtle.pendown()
    turtle.forward(-250)
    turtle.forward(500)
    turtle.forward(-250)
    turtle.left(90)
    turtle.forward(250)
    turtle.forward(-500)
    turtle.forward(250)
    turtle.right(90)

    turtle.penup()
#drawing line
    turtle.goto(first_x, first_y)
    turtle.pendown()
    turtle.dot()

    direction = turtle.towards(second_x, second_y)
    distance = ((((second_x - first_x) ** 2) + ((second_y - first_y) ** 2)) ** (float(1/2)))
    turtle.left(direction)
    print(float(direction))
    turtle.forward(float(distance))
    print(distance)
    turtle.dot()


if __name__ == ' __main__':
    main()
    

