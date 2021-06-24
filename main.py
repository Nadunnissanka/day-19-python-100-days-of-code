import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()

# Color list for turtles
colors = ["red", "blue", "green", "purple", "yellow", "orange"]
list_of_y_positions = [-75, -50, -25, 0, 25, 50, 75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=list_of_y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("User Won!")
            else:
                print(f"User Lose! winning turtle is {winning_color}")
        random_number = random.randint(0, 10)
        turtle.forward(random_number)




screen.exitonclick()
