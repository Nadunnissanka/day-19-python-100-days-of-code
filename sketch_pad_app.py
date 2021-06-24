import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.fd(10)


def move_backward():
    turtle.bk(10)


def move_left():
    turtle.lt(10)


def move_right():
    turtle.rt(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
