import turtle
import random

test = turtle.Turtle()
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
direction = [90, 180, 270, 360]
test.pensize(15)
test.speed("fastest")
while range(200):
    test.color(random.choice(colours))
    test.forward(100)
    test.right(random.choice(direction))

screen = turtle.Screen()
screen.exitonclick()
