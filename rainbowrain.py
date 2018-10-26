# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from tkinter import *
import random

class a_drop:
    def __init__(self,x=1,y=1,z=1,cv=None,v=1,l=1,s=1,color=(0,0,0)):
        self.x=x
        self.y=y
        self.z=z
        self.cv=cv
        self.v=v
        self.l=l
        self.s=s
        self.color='#%02x%02x%02x' % color
    def gen(self,width, height,zmin,zmax,speed,length,size):
        self.x=random.randint(0,width)
        self.y =random.randint(-height,0)
        self.z=random.uniform(zmin,zmax)
        self.v=self.z*speed
        self.l=self.z*length
        self.s=(self.z-zmin)*size
        self.color= '#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))

class MyApp(Tk):
    def __init__(self, totalDrops):
        self.nbi=0
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas  = Canvas(fr, height = 600, width = 800,bg= 'gray10')
        self.canvas.pack()
        self.nb_drops = totalDrops
        self.zmin=0.3
        self.zmax=1.
        self.speed=10.
        self.length=10.
        self.size=3.
        self.drops = list(range(self.nb_drops))
        for idx, drop_ in enumerate(self.drops):
            self.drops[idx]=a_drop()
            self.drops[idx].gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.zmin,self.zmax,self.speed,self.length,self.size)
            self.drops[idx].cv =self.canvas.create_line(self.drops[idx].x, self.drops[idx].y, self.drops[idx].x, self.drops[idx].y+self.drops[idx].l,width=self.drops[idx].s)
            self.canvas.itemconfig(self.drops[idx].cv, fill=self.drops[idx].color) # change color
        self.update_drops()
        return

    def update_drops(self ):
        for idx, drop_ in enumerate(self.drops):
            self.drops[idx].y += self.drops[idx].v
            self.canvas.coords(self.drops[idx].cv,self.drops[idx].x, self.drops[idx].y, self.drops[idx].x , self.drops[idx].y+self.drops[idx].l)
            if self.drops[idx].y > self.canvas.winfo_height():
                self.canvas.delete(self.drops[idx].cv)
                self.drops[idx].gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.zmin,self.zmax,self.speed,self.length,self.size)
                self.drops[idx].cv =self.canvas.create_line(self.drops[idx].x, self.drops[idx].y, self.drops[idx].x, self.drops[idx].y+self.drops[idx].l,width=self.drops[idx].s)
                self.canvas.itemconfig(self.drops[idx].cv, fill=self.drops[idx].color)
        self.canvas.update()
        return
def run(totalDrops):
    root = MyApp(totalDrops)
    root.title("Paralax Rainbow Rain")
    i=0
    while 1:
        try:
            root.update_drops()
            root.after(1)
        except Exception:
            print("Terminating")
            exit()

number_of_drops = 500
run(number_of_drops)