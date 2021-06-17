import art

# Calc
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


ops = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(art.logo)
    num1 = float(input("first num? "))
    continue_op = True
    first = True
    while continue_op:
        for op in ops:
            print(op)
        user_op = input("Pick an operation: ")
        next_num = float(input("next num? "))

        if first:
            print(f"{num1} {user_op} {next_num} = {ops[user_op](num1, next_num)}")
            first = False
            previous_answer = ops[user_op](num1, next_num)

        else:
            print(
                f"{previous_answer} {user_op} {next_num} = {ops[user_op](previous_answer, next_num)}"
            )
            previous_answer = ops[user_op](previous_answer, next_num)

        continue_op = input("y for continue, n for new calculation: ")
        if continue_op == "n":
            calculator()


calculator()
