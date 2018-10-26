import turtle

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.speed(10)
turtle.title("Sierpinski Triangle Simulation")
screen = turtle.Screen()
screen.colormode(255)  # to use the RGB codes for the colors


# function to have the turtle draw a triangle, the basic unit of our fractal
def draw_triangle(vertices, color):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(vertices[1][0], vertices[1][1])
    my_turtle.goto(vertices[2][0], vertices[2][1])
    my_turtle.goto(vertices[0][0], vertices[0][1])
    my_turtle.end_fill()


# the same midpoint function we wrote for the chaos game
def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


# recursive function that draws the different "levels" of the fractal
def run(vertices, level):
    # the different colors we'll use to draw the fractals
    # in RGB format
    colors = [(0, 150, 189), (4, 150, 116), (216, 95, 30), (193, 33, 57), (129, 41, 199),
              (102, 205, 135), (51, 187, 204)]
    draw_triangle(vertices, colors[level])
    # call function recursively to draw all levels of fractal
    if level > 0:
        # draw first segment of fractal
        # the vertices being passed in are the bottom corner of the first
        # section, the bottom corner of the second section, and the bottom
        # corner of the third section.
        try:
            run([vertices[0],
                 midpoint(vertices[0], vertices[1]),
                 midpoint(vertices[0], vertices[2])],
                level - 1)
            run([vertices[1],
                 midpoint(vertices[0], vertices[1]),
                 midpoint(vertices[1], vertices[2])],
                level - 1)
            run([vertices[2],
                 midpoint(vertices[2], vertices[1]),
                 midpoint(vertices[0], vertices[2])],
                level - 1)
        except Exception:
            print("Early Termination")
            exit()


vertices = [[-200, -100], [0, 200], [200, -100]]
level = 4  # how many recursions deep do we want to draw the fractal

run(vertices, level)
