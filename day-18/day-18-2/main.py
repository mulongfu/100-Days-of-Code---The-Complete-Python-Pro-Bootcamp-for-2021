import turtle

test = turtle.Turtle()
for _ in range(10):
    test.forward(10)
    test.penup()
    test.forward(10)
    test.pendown()

screen = turtle.Screen()
screen.exitonclick()
