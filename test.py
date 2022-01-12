import turtle

counter = 0
counter2 = 0

while counter < 8:
    counter += 1
    while counter2 < 4:
        counter2 += 1
        turtle.forward(100)
        turtle.left(90)
    counter2 = 0
    turtle.forward(100)