# Bubble Sort Algorithm - www.101computing.net/bubble-sort-algorithm/
import turtle
from time import sleep

topLeft_x = -180
topLeft_y = 160
intDim = 30
gap = 40


def text(myPen, message, x, y, size):
    FONT = ('Calibri', size, 'normal')
    X = myPen.xcor()
    Y = myPen.ycor()
    myPen.penup()
    myPen.goto(x, y)
    myPen.color("#000000")
    myPen.write(message, align="left", font=FONT)
    myPen.goto(X, Y)
    myPen.pendown()


# A procedure to draw the grid on screen using Python Turtle
def drawList(myPen, list, numberOfIterations):
    global topLeft_x, topLeft_y, intDim
    myPen.penup()
    myPen.goto(topLeft_x, topLeft_y)
    myPen.pendown()

    for i in range(0, len(list)):
        # myPen.goto(topLeft_x+i*intDim,topLeft_y-intDim)
        if i < len(list) - numberOfIterations:
            myPen.fillcolor("#FFFFFF")
        else:
            myPen.fillcolor("#01E171")

        myPen.begin_fill()
        for side in range(0, 4):
            myPen.forward(intDim)
            myPen.left(90)
        myPen.end_fill()

        myPen.forward(intDim)
        text(myPen, list[i], topLeft_x + i * intDim + 8, topLeft_y + -4, 20)


def highlightValues(myPen, list, position, color1, color2):
    global topLeft_x, topLeft_y, intDim, gap
    myPen.penup()
    myPen.goto(topLeft_x + position * intDim, topLeft_y + gap)
    myPen.pendown()
    myPen.fillcolor(color1)
    myPen.begin_fill()
    for step in range(0, 2):
        for side in range(0, 4):
            myPen.forward(intDim)
            myPen.left(90)
        myPen.forward(intDim)
        myPen.end_fill()
        myPen.fillcolor(color2)
        myPen.begin_fill()
    myPen.end_fill()

    text(myPen,list[position], topLeft_x + position * intDim + 8, topLeft_y + -4 + gap, 20)
    text(myPen,list[position + 1], topLeft_x + (position + 1) * intDim + 8, topLeft_y + -4 + gap, 20)
    myPen.getscreen().update()
    if color1 != "#FFFFFF":
        sleep(0.2)


# A function to sort a list using a Bubble Sort Algorithm
def run(list):
    myPen = turtle.Turtle()

    turtle.tracer(0)
    myPen.speed(0)
    myPen.color("#000000")
    myPen.hideturtle()

    global topLeft_y, intDim, gap
    drawList(myPen, list, -1)
    topLeft_y = topLeft_y - gap
    drawList(myPen, list, -1)
    topLeft_y = topLeft_y - gap
    myPen.getscreen().update()
    sleep(1)
    numberOfIterations = 0
    changed = True
    while changed:
        changed = False
        for i in range(0, len(list) - numberOfIterations - 1):
            highlightValues(myPen, list, i, "#FF4444", "#FF4444")
            if list[i] > list[i + 1]:
                highlightValues(myPen, list, i, "#00BEED", "#00BEED")
                # swap values
                list[i], list[i + 1] = list[i + 1], list[i]
                highlightValues(myPen, list, i, "#00BEED", "#00BEED")
                changed = True
            if i >= len(list) - numberOfIterations:
                highlightValues(myPen, list, i, "#FFFFFF", "#FFFFFF")
            else:
                highlightValues(myPen, list, i, "#FFFFFF", "#01E171")

        numberOfIterations += 1
        drawList(myPen, list, numberOfIterations)
        topLeft_y = topLeft_y - gap
        myPen.getscreen().update()
        sleep(0.5)
    text(myPen,"Bubble Sort Complete", topLeft_x, topLeft_y, 20)
    myPen.getscreen().update()
