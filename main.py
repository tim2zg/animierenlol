import turtle


def runner():
    turtle.speed(0)
    while True:
        turtle.forward(10)
        print(turtle.position())
        turtle.right(1)

runner()