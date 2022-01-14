import turtle

import krankenwagen
import weg

run = True

krankenwagenpositions = []


def yooo():
    print(turtle.pos())


def runner():
    while run:
        pass


for i in krankenwagenpositions:
    turtle.hideturtle()
    weg.weg()
    turtle.goto(i[0], i[1])
    krankenwagen.krankenwagen()
