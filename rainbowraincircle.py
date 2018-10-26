# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from tkinter import *
import random

class a_drop:
    def __init__(self,width, height ):
        self.x=random.randint(0,width)
        self.y=random.randint(0,height)
        self.cv = None
        self.r=0
        self.a=random.randint(1,4)*1.
        self.v = 1
        self.color='#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))

class MyApp(Tk):
    def __init__(self):
        self.nbi=0
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas  = Canvas(fr, height = 720, width = 1280,bg= 'black')
        self.canvas.pack()
        self.drops = []
        return

    def update_drops(self, ):
        self.drops.append(a_drop(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()))
        self.drops.append(a_drop(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()))
        toremove=[]
        for idx, drop_ in enumerate(self.drops):
            self.drops[idx].r += self.drops[idx].v
            self.drops[idx].a -= 0.05
            if self.drops[idx].a  <= 0.:
                toremove.append(idx)
            else:
                if self.drops[idx].cv:
                    self.canvas.delete(self.drops[idx].cv)
                self.drops[idx].cv = self.canvas.create_oval(self.drops[idx].x-self.drops[idx].r, self.drops[idx].y-self.drops[idx].r, self.drops[idx].x+self.drops[idx].r, self.drops[idx].y+self.drops[idx].r)
                self.canvas.itemconfig(self.drops[idx].cv, outline=self.drops[idx].color)
                self.canvas.itemconfig(self.drops[idx].cv, width=self.drops[idx].a)
        for i in toremove:
            self.canvas.delete(self.drops[i].cv)
            self.drops.pop(i)
        self.canvas.update()

        return
def run():
    root = MyApp()
    i=0
    while 1:
        try:
            root.update_drops( )
            root.after(1)
        except Exception:
            print("Terminating")
            exit()


run()