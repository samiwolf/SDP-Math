#https://ryancheunggit.gitbooks.io/calculus-with-python/content/05Limits.html
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy.abc import x
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


f = x**3-2*x-6

def init():

    d1 = np.linspace(2, 10, 1000)
    d2 = np.linspace(4, 8, 1000)
    d3 = np.linspace(5, 7, 1000)
    d4 = np.linspace(5.8, 6.2, 100)
    domains = [d1, d2, d3, d4]
    return domains


def makeplot(f,l,d):
        plt.plot(d,[f.evalf(subs={x:xval}) for xval in d],'b',\
                 d,[l.evalf(subs={x:xval}) for xval in d],'r')

def run(f):
    line = 106 * x - 438
    dom = init()
    imgx = 600; imgy = 600

    root = Tk()
    root.title("Random Fractal Spiral Generator")
    root.geometry('{}x{}'.format(imgx, imgy))

    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()



    for i in range(len(dom)):
        plt.subplot(2, 2, i + 1)
        makeplot(f, line, dom[i])
        plt.savefig("Derivatives.png")

    imgName = "Derivatives.png"
    root.title("Derivative")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    #os.remove(imgName)
    root.mainloop()

run(f)