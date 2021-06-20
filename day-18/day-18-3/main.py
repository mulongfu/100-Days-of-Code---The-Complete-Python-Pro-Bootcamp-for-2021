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

for i in range(3, 11):
    test.color(random.choice(colours))
    for _ in range(i):
        test.forward(100)
        test.right(360 / i)

screen = turtle.Screen()
screen.exitonclick()
