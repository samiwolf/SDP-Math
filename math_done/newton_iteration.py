#https://ryancheunggit.gitbooks.io/calculus-with-python/content/05Limits.html
import PIL
import numpy as np
import matplotlib.pyplot as plt
import sympy


import os

from tkinter import *

from PIL import ImageTk, Image


def mysqrt(c, x=1, maxiter=10, prt_step=False):
    for i in range(maxiter):
        x = 0.5 * (x + c / x)
        if prt_step == True:

            print("After {0} iteration, the root value is updated to {1}".format(i + 1, x))
    return x


#mysqrt(2, maxiter=4, prt_step=True)
# After 1 iteration, the root value is updated to 1.5
# After 2 iteration, the root value is updated to 1.41666666667
# After 3 iteration, the root value is updated to 1.41421568627
# After 4 iteration, the root value is updated to 1.41421356237
# result : 1.4142135623746899

f = lambda x: x**2-2*x-4
l1 = lambda x: 2*x-8
l2 = lambda x: 6*x-20
x = np.linspace(0,5,100)

def run(f):
    plt.plot(x, f(x), 'black')
    plt.plot(x[30:80], l1(x[30:80]), 'blue', linestyle='--')
    plt.plot(x[66:], l2(x[66:]), 'blue', linestyle='--')

    l = plt.axhline(y=0, xmin=0, xmax=1, color='black')
    l = plt.axvline(x=2, ymin=2.0 / 18, ymax=6.0 / 18, linestyle='--')
    l = plt.axvline(x=4, ymin=6.0 / 18, ymax=10.0 / 18, linestyle='--')

    plt.text(1.9, 0.5, r"$x_0$", fontsize=18)
    plt.text(3.9, -1.5, r"$x_1$", fontsize=18)
    plt.text(3.1, 1.3, r"$x_2$", fontsize=18)

    plt.plot(2, 0, marker='o', color='r')
    plt.plot(2, -4, marker='o', color='r')
    plt.plot(4, 0, marker='o', color='r')
    plt.plot(4, 4, marker='o', color='r')
    plt.plot(10.0 / 3, 0, marker='o', color='r')
    plt.savefig("Newton Iteration.png")

    imgx = 600; imgy = 600
    root = Tk()
    root.geometry('{}x{}'.format(imgx, imgy))

    image = Image.new("RGB", (imgx, imgy))

    imgName = "Newton Iteration.png"
    root.title("Newton Iteration")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    #os.remove(imgName)
    root.mainloop()




def NewTon(f, s=1, maxiter=100, prt_step=False):
    for i in range(maxiter):

        s = s - f.subs(x, s) / f.diff().subs(x, s)
        if prt_step == True:
            print("After {0} iteration, the solution is updated to {1}".format(i + 1, s))
    return s

f = lambda x: x**2-2*x-4
run(f)