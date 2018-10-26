import math
import random
from collections import deque
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def run(arms):
    imgx = 600
    imgy = 600

    root = Tk()
    root.title("Random Fractal Spiral Generator")
    root.geometry('{}x{}'.format(imgx, imgy))
    progress_var = DoubleVar()  # here you have ints but when calc. %'s usually floats
    v = StringVar()
    theLabel = Label(root, textvariable=v)
    v.set("Generating Fractal Spiral, Please wait...")

    theLabel.pack()
    progressbar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progressbar.pack(fill=X, expand=1)

    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()
    xa = -1.5
    xb = 1.5
    ya = -1.5
    yb = 1.5  # view
    n = arms if arms is not 0 else random.randint(2, 9)  # of spiral arms
    a = 2.0 * math.pi / n  # angle between arms
    t = 2.0 * math.pi * random.random()  # rotation angle of central copy
    r1 = 0.1 * random.random() + 0.1  # scale factor of outmost copies of the spiral arms
    r0 = 1.0 - r1  # scale factor of central copy
    ts = math.sin(t) * r0
    tc = math.cos(t) * r0
    maxIt = 64  # max number of iterations allowed
    for ky in range(imgy):
        progress_var.set(100 * ky / (imgy - 1))
        root.update()
        # print(str(100 * ky / (imgy - 1)).zfill(3) + "%")
        for kx in range(imgx):
            x = float(kx) / (imgx - 1) * (xb - xa) + xa
            y = float(ky) / (imgy - 1) * (yb - ya) + ya
            queue = deque([])
            queue.append((x, y, 0))
            while len(queue) > 0:  # iterate points until none left
                (x, y, i) = queue.popleft()
                # apply all (inverse) IFS transformations
                for k in range(n + 1):  # n outmost copies + central copy
                    if k == n:  # central copy
                        # inverse rotation and scaling
                        xnew = (y + x * tc / ts) / (ts + tc * tc / ts)
                        ynew = (y - x / tc * ts) / (tc + ts / tc * ts)
                    else:  # outmost copies on the spiral arms
                        c = k * a  # angle
                        # inverse scaling and translation
                        xnew = (x - math.cos(c)) / r1
                        ynew = (y - math.sin(c)) / r1
                    if xa <= xnew <= xb and ya <= ynew <= yb:
                        if i + 1 == maxIt: break
                        queue.append((xnew, ynew, i + 1))
            pixels[kx, ky] = (i % 16 * 16, i % 8 * 32, i % 4 * 64)

    imgName = "RandomSpiralFractal_" + str(n) + ".png"
    image.save(imgName, "PNG")
    v.set("Fractal Spiral with " + str(n) + " arms generated!")

    root.title("Fractal Spiral with " + str(n) + " arms")
    canvas = Canvas(root, width=imgx, height=imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName))
    canvas.create_image(0, 0, anchor=NW, image=img)
    os.remove(imgName)
    root.mainloop()


run(2)
