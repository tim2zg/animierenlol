import turtle

import krankenwagen
import weg

run = True

krankenwagenpositions = []


def runner():
    while run:
        for i in krankenwagenpositions:
            weg.weg()
            turtle.goto(i[0], i[1])
            krankenwagen.krankenwagen()


runner()
