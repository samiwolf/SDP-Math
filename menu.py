from tkinter import *

import os
from PIL import Image, ImageTk


# window call and size
from ipython_genutils.py3compat import execfile

root = Tk()
root.title("Academedia ver. Alpha 1.1")
root.geometry("600x700")

# BG
C = Canvas(root, bg="blue", height=1, width=1)
filename = PhotoImage(file="bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.grid()


def RBGAImage(path):
    return Image.open(path).convert("RGBA")


# Logo
logoRBGA = RBGAImage("logo.png")
logo = ImageTk.PhotoImage(logoRBGA)
logolabel = Label(image=logo)
logolabel.configure(bg="black")
logolabel.grid(padx=70, pady=90)

# Title
app = Frame(root)
app.grid()


# Button Events
#############################################################

########   Physics Functions   #########

def run_double_pendulum():
    from phy import DoublePendulum
    root.execfile('DoublePendulum.py')

def run_mass_spring_damper():
    from phy import mass_spring_damper
    root.execfile('mass_spring_damper.py')

def run_multiple_pendulum():
    from phy import multiple_pendulum
    root.execfile('multiple_pendulum.py')

def run_particle_sim():
    from phy import particle_simulation
    root.execfile('particle_simulation.py')

def run_pendulum():
    from phy import Pendulum
    root.execfile('Pendulum.py')

def run_projectile():
    from phy import projectile_full
    root.execfile('projectile_full.py')

def run_solar():
    from phy import solar1
    root.execfile('solar1.py')

def run_verlet_cloth_1():
    from phy import verlet_cloth_system_mouse
    root.execfile('verlet_cloth_system_mouse.py')

def run_verlet_cloth_2():
    from phy import verlet_cloth_system_mouse2
    root.execfile('verlet_cloth_system_mouse2.py')

def run_verlet_particle():
    from phy import verlet_particle
    root.execfile('verlet_particle.py')

def run_verlet_rigid_body():
    from phy import verlet_rigid_body_mouse
    root.execfile('verlet_rigid_body_mouse.py')



########   Math Functions   #########
def run_bayesian_regression():
    from math_done import bayesian_regression
    root.execfile('bayesian_regression.py')

def run_brownian_motion():
    from math_done import geometric_brownian_motion
    root.execfile('geometric_brownian_motion.py')

def run_derivatives():
    from math_done import derivative
    root.execfile('derivative.py')

def run_eq_grapher():
    from math_done import Eq_grapher
    root.execfile('Eq_grapher.py')

def run_exponential_decay():
    from math_done import exponential_decay
    root.execfile('exponential_decay.py')

def run_fermats_spiral():
    from math_done import Fermat_spiral
    root.execfile('Fermat_spiral.py')

def run_georgias_spiral():
    from math_done import GeorgiasSpiral
    root.execfile('GeorgiasSpiral.py')

def run_histogram():
    from math_done import histogram
    root.execfile('histogram.py')

def run_monte_carlo():
    from math_done import monte_carlo_integration
    root.execfile('monte_carlo_integration.py')

def run_newton_iteration():
    from math_done import newton_iteration
    root.execfile('newton_iteration.py')

def run_taylor_series():
    from math_done import taylor_series
    root.execfile('taylor_series.py')

########   Misc Functions   #########

def run_barnsley_fern():
    from misc import BarnsleyFern
    root.execfile('BarnsleyFern.py')

def run_bubble_sort():
    from misc import bubble_sort_UI, bubble_sort
    root.execfile('bubble_sort_UI.py')

def run_dragon_curve():
    from misc import DragonCurve
    root.execfile('DragonCurve.py')

def run_fractal_tree():
    from misc import FractalTree
    root.execfile('FractalTree.py')

def run_hilbert():
    from misc import Hilbert
    root.execfile('Hilbert.py')

def run_honeycomb():
    from misc import honeycomb
    root.execfile('honeycomb.py')

def run_mandelbrot():
    from misc import InteractiveMandelbrot
    root.execfile('InteractiveMandelbrot.py')

def run_langtons_loop():
    from misc import langtonloop
    root.execfile('langtonloop.py')

def run_langtons_ant():
    from misc import LangtonsAnt
    root.execfile('LangtonsAnt.py')

def run_quasi_crystal():
    from misc import quasicrystal
    root.execfile('quasicrystal.py')

def run_rainbow_click():
    from misc import RainbowClick
    root.execfile('RainbowClick.py')

def run_rainbow_rain():
    from misc import rainbowrain
    root.execfile('rainbowrain.py')

def run_rainbow_rain_circle():
    from misc import rainbowraincircle
    root.execfile('rainbowraincircle.py')

def run_random_fractals():
    from misc import RandomFractalSpiral
    root.execfile('RandomFractalSpiral.py')

def run_siers_triangles():
    from misc import Sierpinski
    root.execfile('Sierpinski.py')

#############################################################
def close_window():
    root.destroy()

def physicsmenu():
    root.withdraw()
    phyroot = Tk()
    phyroot.title("Academedia - Physics Menu")
    phyroot.geometry("600x700")

    Label(phyroot, text = "Physics Menu",  font="Eurostile 20 bold", padx=200, pady=20).grid()

    b1 = Button(phyroot,
           bg="gray",
           fg="white",
           text="Double Pendulum",
           bd=12,
           relief="raised",
           font = "Calibri 9 bold",
           command=run_double_pendulum,
           width=30).grid()

    b2 = Button(phyroot,
            bg="gray",
            fg="white",
            text="Mass Spring Damper",
            bd=12,
            relief="raised",
            command=run_mass_spring_damper,
            font="Calibri 9 bold",
            width=30).grid()

    b3 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Multiple Pendulum",
                bd=12,
                command=run_multiple_pendulum,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b4 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Particle Simulation",
                bd=12,
                command=run_particle_sim,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b5 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Pendulum",
                bd=12,
                command=run_pendulum,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b6 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Projectile",
                bd=12,
                command=run_projectile,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b7 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Solar",
                bd=12,
                command=run_solar,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b8 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Cloth System 1",
                bd=12,
                command=run_verlet_cloth_1,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b9 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Cloth System 2",
                bd=12,
                command=run_verlet_cloth_2,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b10 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Particle",
                bd=12,
                command=run_verlet_particle,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    b11 = Button(phyroot,
                bg="gray",
                fg="white",
                text="Verlet Rigid Body Mouse",
                bd=12,
                command=run_verlet_rigid_body,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()

    exitb = Button(phyroot,
                bg="gray",
                fg="white",
                text="Back",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=10,
                command =lambda:[phyroot.destroy(), recall_window()]).grid()



####################################

def mathsmenu():
    root.withdraw()
    mathroot = Tk()
    mathroot.title("Academedia - Mathematics Menu")
    mathroot.geometry("600x700")

    Label(mathroot, text = "Mathematics Menu",  font="Eurostile 20 bold", padx=155, pady=20).grid()

    b1 = Button(mathroot,
           bg="gray",
           fg="white",
           text="Bayesian Regression",
           bd=12,
           relief="raised",
           font="Calibri 9 bold",
           command=run_bayesian_regression,
           width=30).grid()

    b2 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Brownian Motion",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_brownian_motion,
                width=30).grid()

    b3 = Button(mathroot,
            bg="gray",
            fg="white",
            text="Derivatives",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            command=run_derivatives,
            width=30).grid()

    b4 = Button(mathroot,
            bg="gray",
            fg="white",
            text="Equation Grapher",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            command=run_eq_grapher,
            width=30).grid()

    b5 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Exponential Decay",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_exponential_decay,
                width=30).grid()

    b6 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Fermat's Spiral",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_fermats_spiral,
                width=30).grid()

    b7 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Georgia's Spiral",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_georgias_spiral,
                width=30).grid()

    b8 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Histogram",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_histogram,
                width=30).grid()

    b9 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Monte Carlo Integration",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_monte_carlo,
                width=30).grid()

    b10 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Newton Iteration",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_newton_iteration,
                width=30).grid()

    b11 = Button(mathroot,
                bg="gray",
                fg="white",
                text="Taylor Series",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_taylor_series,
                width=30).grid()

    exitb = Button(mathroot,
            bg="gray",
            fg="white",
            text="Back",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            width=10,
            height=1,
            command=lambda: [mathroot.destroy(), recall_window()]).grid()

####################################

def chemistrysmenu():
    root.withdraw()
    chemroot = Tk()
    chemroot.title("Academedia - Chemistry Menu")
    chemroot.geometry("600x700")

    Label(chemroot, text = "Chemistry menu will be \nimplemented in the future.\n Sorry for the inconvenience.",  font="Eurostile 20 bold", padx=97, pady=20).grid()

    exitb = Button(chemroot,
            bg="gray",
            fg="white",
            text="Back",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            width=30,
            command=lambda: [chemroot.destroy(), recall_window()]).grid()


    b1 = Button(chemroot,
           bg="gray",
           fg="white",
           text="Task 1",
           bd=12,
           relief="raised",
           font="Calibri 9 bold",
           width=30).grid()

    b2 = Button(chemroot,
            bg="gray",
            fg="white",
            text="Task 2",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            width=30).grid()

    b3 = Button(chemroot,
            bg="gray",
            fg="white",
            text="Task 3",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            width=30).grid()
    b4 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b5 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b6 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b7 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b8 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b9 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b10 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b11 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()
    b12 = Button(chemroot,
                bg="gray",
                fg="white",
                text="Task 3",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                width=30).grid()



    #####  Scroll bar  ##########


    frame = Frame(chemroot)
    scroll = Scrollbar(frame)
    text = Text(frame, yscrollcommand=scroll.set)
    button = Button(chemroot)
    # Config
    text.insert(END, '\n'.join("ass"))
    scroll.config(command=text.yview)
    button.config(text=('Close'), command=chemroot.destroy)
    button.focus_set()
    # Packing
    text.grid(side='left', fill='both', expand=1)
    scroll.grid(side='right', fill='y')
    frame.grid(fill='both', expand=1)
    button.grid(ipadx=30)

    ###############################

####################################

def missmenu():
    root.withdraw()
    misroot = Tk()
    misroot.title("Academedia - Miscellaneous Menu")
    misroot.geometry("600x700")

    Label(misroot, text = "Miscellaneous Menu",  font="Eurostile 20 bold", padx=150, pady=20).grid()

    b1 = Button(misroot,
           bg="gray",
           fg="white",
           text="Barnsley Fern",
           bd=12,
           relief="raised",
           font="Calibri 9 bold",
           command=run_barnsley_fern,
           width=30).grid()

    b2 = Button(misroot,
            bg="gray",
            fg="white",
            text="Bubble Sort",
            bd=12,
            relief="raised",
            font="Calibri 9 bold",
            command=run_bubble_sort,
            width=30).grid()

    b3 = Button(misroot,
                bg="gray",
                fg="white",
                text="Dragon Curve",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_dragon_curve,
                width=30).grid()

    b4 = Button(misroot,
                bg="gray",
                fg="white",
                text="Fractal Tree",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_fractal_tree,
                width=30).grid()
    '''
    b5 = Button(misroot,
                bg="gray",
                fg="white",
                text="Hilbert",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_hilbert,
                width=30).grid()
    '''
    b6 = Button(misroot,
                bg="gray",
                fg="white",
                text="Honeycomb",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_honeycomb,
                width=30).grid()

    b7 = Button(misroot,
                bg="gray",
                fg="white",
                text="Interactive Mandelbrot",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_mandelbrot,
                width=30).grid()

    b8 = Button(misroot,
                bg="gray",
                fg="white",
                text="Langton's Loop",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_langtons_loop,
                width=30).grid()

    b9 = Button(misroot,
                bg="gray",
                fg="white",
                text="Langton's Ant",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_langtons_ant,
                width=30).grid()

    b10 = Button(misroot,
                bg="gray",
                fg="white",
                text="Quasi Crystal",
                bd=12,
                relief="raised",
                font="Calibri 9 bold",
                command=run_quasi_crystal,
                width=30).grid()


    b10 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Click",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_click,
                 width=30).grid()

    b11 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Rain",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_rain,
                 width=30).grid()

    '''
    b12 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Rainbow Rain Circles",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_rainbow_rain_circle,
                 width=30).grid()
                 
    b13 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Random Fractal Spiral",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_random_fractals,
                 width=30).grid()    
    '''

    b14 = Button(misroot,
                 bg="gray",
                 fg="white",
                 text="Sierpinski's Triangles",
                 bd=12,
                 relief="raised",
                 font="Calibri 9 bold",
                 command=run_siers_triangles,
                 width=30).grid()


    exitb = Button(misroot,
                   bg="gray",
                   fg="white",
                   text="Back",
                   bd=12,
                   relief="raised",
                   font="Calibri 9 bold",
                   width=10,
                   command=lambda: [misroot.destroy(), recall_window()]).grid()


def recall_window():
    root.deiconify()


#############################################################


# buttons
button1 = Button(app, text="Physics", bd=12, relief="raised", command=physicsmenu, width=15)
button1.configure(bg="#00008B", fg="white", font="Calibri 9 bold")
button1.grid(padx=1, pady=2)

button2 = Button(app, text="Mathematics", bd=12, relief="raised", command=mathsmenu, width=15)
button2.configure(bg="#8B0000", fg="white", font="Calibri 9 bold")
button2.grid(padx=1, pady=2)

button3 = Button(app, text="Chemistry", bd=12, relief="raised", command=chemistrysmenu, width=15)
button3.configure(bg="#006400", fg="white", font="Calibri 9 bold")
button3.grid(padx=1, pady=2)

button4 = Button(app, text="Miscellaneous", bd=12, relief="raised", command=missmenu, width=15)
button4.configure(bg="#BDB76B", font="Calibri 9 bold")
button4.grid(padx=1, pady=2)

button5 = Button(app, text="Exit", bd=12, relief="raised", command=sys.exit, width=15)
button5.configure(bg="gray", fg="white", font="Calibri 9 bold")
button5.grid(padx=1, pady=2)

# start event
root.mainloop()
