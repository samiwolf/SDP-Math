from numpy import *
from matplotlib.pyplot import *
import os

from tkinter import *

from PIL import ImageTk, Image

def expodecay():
    I = 1
    a = 2
    T = 4
    dt = 0.2
    Nt = int(round(T / dt))  # no of time intervals
    u = zeros(Nt + 1)  # array of u[n] values
    t = linspace(0, T, Nt + 1)  # time mesh
    theta = 1  # Backward Euler method

    u[0] = I  # assign initial condition
    for n in range(0, Nt):  # n=0,1,...,Nt-1
        u[n + 1] = (1 - (1 - theta) * a * dt) / (1 + theta * dt * a) * u[n]

    # Compute norm of the error
    u_e = I * exp(-a * t) - u  # exact u at the mesh points
    error = u_e - u
    E = sqrt(dt * sum(error ** 2))
    print('Norm of the error: %.3E' % E)

    # Compare numerical (u) and exact solution (u_e) in a plot
    plot(t, u, 'r--o')
    t_e = linspace(0, T, 1001)  # very fine mesh for u_e
    u_e = I * exp(-a * t_e)
    plot(t_e, u_e, 'b-')
    legend(['numerical, theta=%g' % theta, 'exact'])
    xlabel('t')
    ylabel('u')
    savefig("Exponential Decay.png")

def run():
    expodecay()
    imgx = 600; imgy = 600
    root = Tk()
    root.geometry('{}x{}'.format(imgx, imgy))

    image = Image.new("RGB", (imgx, imgy))
    pixels = image.load()

    imgName = "Exponential Decay.png"
    root.title("Exponential Decay")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    #os.remove(imgName)
    root.mainloop()

run()