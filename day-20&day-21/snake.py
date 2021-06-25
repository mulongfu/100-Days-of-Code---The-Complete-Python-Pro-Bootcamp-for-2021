import turtle


class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            snake_0 = turtle.Turtle()
            snake_0.shape("square")
            snake_0.color("white")
            snake_0.penup()
            snake_0.setx(0 - 20 * i)
            self.snake.append(snake_0)
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
