import time
import turtle

import displaycorona
import krankenhaus
import krankenwagen
import weg
import write

run = True
wn = turtle.Screen()
wn.tracer(0)
turtle.speed(0)


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
                turtle.goto(360, -155)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(i + -370, 115)
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
                turtle.goto(360, -155)
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
                turtle.goto(i + -220, -70)
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
                turtle.goto(360, -155)
                turtle.pendown()
                krankenhaus.krankenhaus()
                turtle.penup()
                turtle.home()
                turtle.goto(115, -75 + i)
                turtle.left(90)
                turtle.pendown()
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(30):
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
                turtle.goto(80 + i, 75)
                turtle.pendown()
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(200):
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
                turtle.goto(140, 70 - i)
                turtle.pendown()
                turtle.right(90)
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        for i in range(80):
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
                turtle.goto(140 + i, -223)
                turtle.pendown()
                krankenwagen.krankenwagen()
                # Update the screen to see the changes
                wn.update()

        turtle.penup()
        turtle.home()
        turtle.pendown()
        displaycorona.runner(-260, -210, 5)
        write.draw_text("Corona Zahlen:", -260, -150)
        wn.update()
        time.sleep(2)


runner()
wn.mainloop()
