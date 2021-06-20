import turtle as turtle_module
import random

test = turtle_module.Turtle()


def forward():
    test.forward(30)


def backforward():
    test.backward(30)


def turn_left():
    test.setheading(test.heading() + 10)


def turn_right():
    test.setheading(test.heading() - 10)


def clear():
    test.clear()
    test.penup()
    test.home()
    test.pendown()


screen = turtle_module.Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backforward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
