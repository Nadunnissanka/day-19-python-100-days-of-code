import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
