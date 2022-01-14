import turtle


def draw_text(text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, font=("Arial", 16, "normal"))
