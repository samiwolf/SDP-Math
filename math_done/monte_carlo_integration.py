#http://barnesanalytics.com/monte-carlo-integration-in-python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os

from tkinter import *

from PIL import ImageTk, Image

def easy_function(x):
    return((3)*(x**2))

def hard_function(x):
    return((1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2))



def integrate(x1,x2,func=easy_function,n=100000):
    X=np.linspace(x1,x2,1000)
    y1=0
    y2=max((func(X)))+1
    print(x1,x2,y1,y2)
    area=(x2-x1)*(y2-y1)
    check=[]
    xs=[]
    ys=[]
    for i in range(n):
        x=np.random.uniform(x1,x2,1)
        xs.append(x)
        y=np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(func(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return(np.mean(check)*area,xs,ys,check)

def run():
    X = np.linspace(-20, 20, 1000)
    plt.plot(X, easy_function(X))
    plt.savefig("mci0.png")
    plt.plot(X, hard_function(X))
    plt.savefig("mci1.png")
    plt.show()

    _, x, y, c = integrate(0.3, 2.5, n=100)
    df = pd.DataFrame()
    df['x'] = x
    df['y'] = y
    df['c'] = c

    X = np.linspace(0.3, 2.5, 200)
    plt.plot(X, easy_function(X))
    plt.scatter(df[df['c'] == 0]['x'], df[df['c'] == 0]['y'], color='red')
    plt.scatter(df[df['c'] == 1]['x'], df[df['c'] == 1]['y'], color='blue')
    plt.savefig("mci2.png")

    imgx = 600; imgy = 600
    root = Tk()
    root.geometry('{}x{}'.format(imgx, imgy))

    image = Image.new("RGB", (imgx, imgy))

    imgName = "mci2.png"
    root.title("Monte Carlo Integration")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName))
    canvas.create_image(0, 0, anchor=NW, image=img)
    os.remove(imgName)
    root.mainloop()


run()