def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go():
    turn_left()
    climb = 0
    while not right_is_clear():
        move()
        climb += 1
    turn_right()
    move()
    turn_right()
    for i in range(climb):
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        go()
    else:
        move()
