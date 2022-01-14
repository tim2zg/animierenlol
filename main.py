import turtle

import krankenhaus
import weg
import krankenwagen
import time

run = True
wn = turtle.Screen()

# This turns off screen updates
wn.tracer(0)

turtle.speed(0)

krankenwagenpositions = [[-370, 120], [-380, 120], [-390, 120], [-400, 120], [-350, 120], [0, 200], [-200, 200], [-200, 0]]


def runner():
    while run:
        #  Forward
        for i in range(120):
                turtle.reset()
                turtle.clear()
                turtle.hideturtle()
                weg.weg()
                turtle.penup()
                turtle.left(180)
                turtle.goto(360, -160)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(i + -370, 120)
                turtle.pendown()
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(120):
                turtle.reset()
                turtle.clear()
                turtle.hideturtle()
                weg.weg()
                turtle.penup()
                turtle.left(180)
                turtle.goto(360, -160)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(-220, 120 - i)
                turtle.pendown()
                turtle.right(90)
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(260):
                turtle.reset()
                turtle.clear()
                turtle.hideturtle()
                weg.weg()
                turtle.penup()
                turtle.left(180)
                turtle.goto(360, -155)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(i + -220, -75)
                turtle.pendown()
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(120):
                turtle.reset()
                turtle.clear()
                turtle.hideturtle()
                weg.weg()
                turtle.penup()
                turtle.left(180)
                turtle.goto(360, -160)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(-220, 120 - i)
                turtle.pendown()
                turtle.right(90)
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()


runner()




wn.mainloop()
