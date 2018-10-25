# Graphing Algorithm - www.101computing.net/graphing-algorithm
import turtle
import math

def init():
    myPen = turtle.Turtle()
    myPen.speed(0)

    screen = turtle.Screen()
    screen.bgcolor("#000000")
    return myPen,screen

# A procedure to draw both the X and Y axis on screen
def drawAxis(myPen):
    # X Axis
    myPen.penup()
    myPen.goto(-200, 0)
    myPen.pendown()
    myPen.goto(200, 0)
    # Y Axis
    myPen.penup()
    myPen.goto(0, -200)
    myPen.pendown()
    myPen.goto(0, 200)

def drawFunc(func, myPen):
    pass


def drawLine(a, b, myPen):
    myPen.penup()
    for x in range(-200, 201):
        y = a * x + b
        myPen.goto(x, y)
        myPen.pendown()

    myPen.penup()
    myPen.goto(-180, 180)
    # Work out and display the mathematical equation
    equation = ""
    if a == 0:
        equation = " y = " + str(b)
    else:
        if b > 0:
            equation = " y = " + str(a) + "x + " + str(b)
        elif b < 0:
            equation = " y = " + str(a) + "x " + str(b)
        else:
            equation = " y = " + str(a)

    ## issue here
    #     myPen.write(equation, None, None, ("Arial", 16, "normal"))


# Main Program Starts Here
def run():
    myPen, screen = init()
    myPen.color("white")
    drawAxis(myPen)
    myPen.pensize(2)
    myPen.color("#FF59F7")
    drawLine(1.5, -40, myPen)
    screen.tracer(0)

run()