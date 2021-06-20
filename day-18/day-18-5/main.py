import turtle
import random

test = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


direction = [90, 180, 270, 360]
test.pensize(15)
test.speed("fastest")
while range(200):
    test.color(random_color())
    test.forward(100)
    test.right(random.choice(direction))

screen = turtle.Screen()
screen.exitonclick()
