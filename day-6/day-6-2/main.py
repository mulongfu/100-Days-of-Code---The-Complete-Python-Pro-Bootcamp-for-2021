def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(0, 6):
    go()
