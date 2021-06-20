import turtle

test = turtle.Turtle()
for _ in range(4):
    test.forward(100)
    test.right(90)

screen = turtle.Screen()
screen.exitonclick()