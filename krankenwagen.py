import turtle


def krankenwagen():
    turtle.left(90)
    turtle.color("black")
    turtle.fd(40)
    turtle.rt(90)
    turtle.fd(60)
    turtle.rt(40)
    turtle.fd(30)
    turtle.rt(140)
    turtle.fd(35)
    turtle.rt(90)
    turtle.fd(20)
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(10)
    turtle.end_fill()
    turtle.pu()
    turtle.fd(10)
    turtle.rt(90)
    turtle.fd(10)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor("red")
    for m in range(4):
        turtle.fd(5)  # rotes kreuz
        turtle.lt(90)
        turtle.fd(6)
        turtle.rt(90)
        turtle.fd(6)
        turtle.lt(90)
    turtle.begin_fill()
    turtle.pu()
    turtle.fd(30)
    turtle.lt(90)
    turtle.fd(30)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(15)
    turtle.lt(90)
    for m in range(20):
        turtle.fd(1)  # erster Radbogen
        turtle.rt(10)
    turtle.lt(113)
    turtle.fd(20)
    turtle.lt(90)
    for b in range(20):
        turtle.fd(1)  # zweiter radbogen
        turtle.rt(10)
    turtle.lt(110)
    turtle.fd(28)
    turtle.lt(90)
    turtle.fd(20)
    turtle.pu()
    turtle.lt(180)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(28)
    turtle.lt(87)
    turtle.pd()
    for g in range(40):
        turtle.fd(1)
        turtle.rt(10)
    turtle.pu()
    turtle.rt(46)
    turtle.fd(35)
    turtle.pd()
    for a in range(40):
        turtle.fd(1)
        turtle.rt(10)
