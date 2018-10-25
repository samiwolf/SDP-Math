import numpy as np
from matplotlib import pyplot as plt
import os

from tkinter import *

from PIL import ImageTk, Image

def gmb():
    S0 = 100  # initial stock price
    K = 100  # strike price
    r = 0.05  # risk-free interest rate
    sigma = 0.50  # volatility in market
    T = 1  # time in years
    N = 100  # number of steps within each simulation
    deltat = T / N  # time step
    i = 1000  # number of simulations
    discount_factor = np.exp(-r * T)  # discount factor

    S = np.zeros([i, N])
    t = range(0, N, 1)

    for y in range(0, i - 1):
        S[y, 0] = S0
        for x in range(0, N - 1):
            S[y, x + 1] = S[y, x] * (np.exp((r - (sigma ** 2) / 2) * deltat + sigma * deltat * np.random.normal(0, 1)))
        plt.plot(t, S[y])

    plt.title('Simulations %d Steps %d Sigma %.2f r %.2f S0 %.2f' % (i, N, sigma, r, S0))
    plt.xlabel('Steps')
    plt.ylabel('Stock Price')
    plt.savefig("Brownian Motion.png")

    C = np.zeros((i - 1, 1), dtype=np.float16)
    for y in range(0, i - 1):
        C[y] = np.maximum(S[y, N - 1] - K, 0)
    return C, discount_factor

#no parameter
def run():
    CC, DF = gmb()
    CallPayoffAverage = np.average(CC)
    CallPayoff = DF * CallPayoffAverage
    print(CallPayoff)
    imgx = 600; imgy = 600
    root = Tk()
    root.geometry('{}x{}'.format(imgx, imgy))

    image = Image.new("RGB", (imgx, imgy))

    imgName = "Brownian Motion.png"
    root.title("Brownian Motion Simulation")
    canvas = Canvas(root, width = imgx, height = imgy)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(imgName), master=root)
    canvas.create_image(0, 0, anchor=NW, image=img)
    #os.remove(imgName)
    root.mainloop()
run()