import turtle
import random

test = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


test.speed("fastest")


def draw_spirograph(offset):
    for _ in range(int(360 / offset)):
        test.color(random_color())
        test.circle(100)
        test.setheading(test.heading() + offset)
        test.circle(100)


draw_spirograph(50)
screen = turtle.Screen()
screen.exitonclick()
