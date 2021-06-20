import turtle as turtle_module
import random


screen = turtle_module.Screen()
screen.setup(500, 400)
race_on = False
bet = screen.textinput(title="Bet ", prompt="Color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for i in range(6):
    test = turtle_module.Turtle(shape="turtle")
    test.color(color[i])
    test.penup()
    test.goto(x=-230, y=-100 + (45 * i))
    all_turtles.append(test)

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == bet:
                print(f"You've won! the {winner_color}!")
            else:
                print(f"You've lost! the winner turtle is {winner_color}")

        rand_distant = random.randint(0, 10)
        turtle.forward(rand_distant)


screen.exitonclick()
