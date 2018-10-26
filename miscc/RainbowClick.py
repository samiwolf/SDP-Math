import turtle

screen = turtle.Screen()
screen.title("Rainbow Click")
defaultSpread = [15]  # default


class MyTurtle(turtle.Turtle):
    def __init__(self, screen=turtle.Screen()):
        turtle.Turtle.__init__(self)
        self.speed(2)
        self.width(2)
        self.hideturtle()


def create_turtles(screen, n=10):
    for i in range(n):
        MyTurtle(screen)


def move_turtles(screen, x, y, spread, angle=4):
    for i, turtle in enumerate(screen.turtles()):
        turtle.left(angle * (1 + i))
        turtle.forward(spread)

        # x, y = turtle.pos()
        try:
            colors = ["violet", "indigo", "blue", "green", "yellow", "orange",
                      "red"]  # Make a list of colors to picvk from

            turtle.color(colors[int(x + y + i) % 7])
        except:
            pass


def draw_shape(x, y, spread=defaultSpread[0]):
    screen.tracer(0)
    for turtle in screen.turtles():
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
    screen.tracer(1)
    for i in range(spread):
        screen.tracer(0)

        move_turtles(screen, x, y, spread)
        screen.tracer(1)


def run(number_of_turtles):
    create_turtles(screen, number_of_turtles)
    screen.onclick(draw_shape)
    screen.listen()
    turtle.done()


number_of_turtles = 15
run(number_of_turtles)
