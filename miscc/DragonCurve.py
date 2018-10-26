import turtle


def turn(i):
    left = (((i & -i) << 1) & i) != 0
    return 'L' if left else 'R'


def curve(iteration):
    return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])


def run(radius):
    turtle.showturtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.title("Dragon Curve Simulation")

    i = 1
    try:
        while True:
            if turn(i) == 'L':
                turtle.circle(-radius, 90, 10)
            else:
                turtle.circle(radius, 90, 10)
            i += 1
    except turtle.Terminator:
        print("Early Termination")


run(5)
