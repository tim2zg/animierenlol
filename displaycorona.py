import turtle

import displaycoronanumbers
import getcorona


def runner(x, y, size):  # Draws the runner on the screen
    counter = 0  # Counter for the number of times the runner has been drawn
    turtle.penup()  # Pulls the pen up
    turtle.goto(x, y)  # Moves the turtle to the starting position
    turtle.left(90)  # Turns the turtle to the left
    corona = getcorona.getcovid()  # Gets the corona data
    corona_string = str(corona)  # Converts the corona data to a string
    for i in corona_string:  # Loops through the corona data
        counter = counter + 1  # Adds one to the counter
        if i == "1":  # If the corona data is 1
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_one(size)  # Displays the number one
        elif i == "2":  # If the corona data is 2
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_two(size)  # Displays the number two
        elif i == "3":  # If the corona data is 3
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_three(size)  # Displays the number three
        elif i == "4":  # If the corona data is 4
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_four(size)  # Displays the number four
        elif i == "5":  # If the corona data is 5
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_five(size)  # Displays the number five
        elif i == "6":  # If the corona data is 6
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_six(size)  # Displays the number six
        elif i == "7":  # If the corona data is 7
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_seven(size)  # Displays the number seven
        elif i == "8":  # If the corona data is 8
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_eight(size)  # Displays the number eight
        elif i == "9":  # If the corona data is 9
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_nine(size)  # Displays the number nine
        elif i == "0":  # If the corona data is 0
            turtle.pendown()  # Puts the pen down
            displaycoronanumbers.display_zero(size)  # Displays the number zero
        turtle.penup()  # Pulls the pen up
        turtle.goto(x, y)  # Moves the turtle to the starting position
        turtle.penup()  # Pulls the pen up
        turtle.forward(counter * 10 * size)  # Moves the turtle forward
        turtle.left(90)  # Turns the turtle to the left

