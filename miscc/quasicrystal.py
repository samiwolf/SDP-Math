import math
import random
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


def run():
    imgx = 600;
    imgy = 600

    root = Tk()
    root.title("Random Quasicrystal Generator")
    root.geometry('{}x{}'.format(imgx, imgy))
    progress_var = DoubleVar()  # here you have ints but when calc. %'s usually floats
    v = StringVar()
    theLabel = Label(root, textvariable=v)
    v.set("Generating Quasicrystal, Please wait...")

    theLabel.pack()
    progressbar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progressbar.pack(fill=X, expand=1)

    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    f = random.random() * 40 + 10  # frequency
    p = random.random() * math.pi  # phase
    n = random.randint(10, 20)  # of rotations
    print(f, p, n)

    for ky in range(imgy):
        progress_var.set(100 * ky / (imgy - 1))
        root.update()
        y = float(ky) / (imgy - 1) * 4 * math.pi - 2 * math.pi
        for kx in range(imgx):
            x = float(kx) / (imgx - 1) * 4 * math.pi - 2 * math.pi
            z = 0.0
            for i in range(n):
                r = math.hypot(x, y)
                a = math.atan2(y, x) + i * math.pi * 2.0 / n
                z += math.cos(r * math.sin(a) * f + p)
            c = int(round(255 * z / n))
            pixels[kx, ky] = (c, c, c)  # grayscale

    imgName = "quasicrystal.png"
    image.save(imgName, "PNG")
    v.set("Quasicrystal Structure Generated!")

    root.title("Quasicrystal")
    canvas = Canvas(root, width=imgx, height=imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    os.remove(imgName)

    root.mainloop()


run()
