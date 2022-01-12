import time
import turtle

import displaycoronanumbers


def runner(x, y):
    counter = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(90)
    #  corona = getcorona.getcovid()
    corona = 5678  # Offline :/
    corona_string = str(corona)
    for i in corona_string:
        counter = counter + 1
        if i == "1":
            turtle.pendown()
            displaycoronanumbers.display_one()
        elif i == "2":
            turtle.pendown()
            displaycoronanumbers.display_two()
        elif i == "3":
            turtle.pendown()
            displaycoronanumbers.display_three()
        elif i == "4":
            turtle.pendown()
            displaycoronanumbers.display_four()
        elif i == "5":
            turtle.pendown()
            displaycoronanumbers.display_five()
        elif i == "6":
            turtle.pendown()
            displaycoronanumbers.display_six()
        elif i == "7":
            turtle.pendown()
            displaycoronanumbers.display_seven()
        elif i == "8":
            turtle.pendown()
            displaycoronanumbers.display_eight()
        elif i == "9":
            turtle.pendown()
            displaycoronanumbers.display_nine()
        elif i == "0":
            turtle.pendown()
            displaycoronanumbers.display_zero()
        turtle.penup()
        turtle.goto(x, y)
        turtle.penup()
        turtle.forward(counter * 100)
        turtle.left(90)
        time.sleep(1)


runner(50, 50)
