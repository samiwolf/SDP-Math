import turtle

myTurtle = turtle.Turtle()
myTurtle.showturtle()
myTurtle.hideturtle()
turtle.title("Hilbert's Space Filling Curve Simulation")
myTurtle.speed(0)


def hilbert2(size, rule, angle, depth):
    if depth > 0:
        try:
            antiClockWise = lambda: hilbert2(size, "anticlockwise", angle, depth - 1)
            clockWise = lambda: hilbert2(size, "clockwise", angle, depth - 1)
            left = lambda: myTurtle.left(angle)
            right = lambda: myTurtle.right(angle)
            forward = lambda: myTurtle.forward(size)
            if rule == "anticlockwise":
                left();
                clockWise();
                forward();
                right();
                antiClockWise();
                forward();
                antiClockWise();
                right();
                forward();
                clockWise();
                left();
            if rule == "clockwise":
                right();
                antiClockWise();
                forward();
                left();
                clockWise();
                forward();
                clockWise();
                left();
                forward();
                antiClockWise();
                right();
        except Exception:
            print("Terminating")
            # exit()


hilbert2(10, "clockwise", 90, 10)
