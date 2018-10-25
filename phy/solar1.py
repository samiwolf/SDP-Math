from __future__ import print_function, absolute_import
from PIL import ImageGrab
from tkinter import *
import numpy as np
import random
def volume(m):
    return 4. * np.pi * (m**3) / 3.

class particule:
    def __init__(self,):
        self.x=0
        self.y=0
        self.v=[0,0]
        self.a=[0,0]
        self.m=1.
        self.cv=None
    def gen(self,width, height,zmin,zmax,amin,amax,mmin,mmax):
        self.x=random.randint(0,width)
        self.y =random.randint(0,height)
        phi = np.arctan(float(self.y-height/2.)/(float(self.x-width/2.)+0.0001))
        if np.sign(float(self.x-width/2.))==-1:
            phi=phi+np.pi
        print(self.x-width/2.,self.y-height/2.,phi)
        r=zmax#random.uniform(0.,zmax)
        self.v=[-r*np.sin(phi),r*np.cos(phi)]
        #-r*np.sin(phi),-r*np.cos(phi)]
        # self.v=[random.uniform(-zmax,zmax), random.uniform(-zmax,zmax)]
        self.a = [0,0]#[random.uniform(amin,amax), random.uniform(amin,amax)]
        self.m=random.uniform(mmin,mmax)
        self.color= '#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))

class MyApp(Tk):
    def __init__(self):
        self.nbi=0
        self.totalparticules=0
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas  = Canvas(fr, height = 728, width = 1288,bg= 'black')
        self.canvas.pack()
        nb_particules = 300
        self.zmin=1.
        self.zmax=1.1
        self.amin=0.
        self.amax=0.
        self.mmin=1.
        self.mmax=8.
        self.size=3.
        self.A = (self.canvas.winfo_reqwidth()/2,self.canvas.winfo_reqheight()/2)
        self.M=100
        self.G=1.
        self.lim=10000
        self.dt = 0.01
        self.particules = list(range(nb_particules+1))

        for idx, p_ in enumerate(self.particules):
            if idx ==0:
                self.particules[idx]=particule()
                self.particules[idx].gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),0,0,0,0,30,30)
                self.particules[idx].x = self.canvas.winfo_reqwidth()/2
                self.particules[idx].y = self.canvas.winfo_reqheight()/2
                self.color = '#%02x%02x%02x' % ( (255,255,255))
                self.particules[idx].cv =self.canvas.create_oval(self.particules[idx].x-self.particules[idx].m, self.particules[idx].y-self.particules[idx].m, self.particules[idx].x+self.particules[idx].m, self.particules[idx].y+self.particules[idx].m)
                self.canvas.itemconfig(self.particules[idx].cv, fill=self.particules[idx].color) # change color
            else:
                self.particules[idx]=particule()
                self.particules[idx].gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.zmin,self.zmax,self.amin,self.amax,self.mmin,self.mmax)
                self.particules[idx].cv =self.canvas.create_oval(self.particules[idx].x-self.particules[idx].m, self.particules[idx].y-self.particules[idx].m, self.particules[idx].x+self.particules[idx].m, self.particules[idx].y+self.particules[idx].m)
                self.canvas.itemconfig(self.particules[idx].cv, fill=self.particules[idx].color) # change color
        self.update_drops()

        self.canvas.bind("<Button-1>", self.click )


        return
    def click(self, event):
        print( (event.x, event.y))
        self.A=(event.x, event.y)

    def update_drops(self ):
        print(len(self.particules))
        if len(self.particules)<100 :
            # self.totalparticules+=1
            # print(self.totalparticules)
            p = particule()
            p.gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.zmin,self.zmax,self.amin,self.amax,self.mmin,self.mmax)
            self.particules.append(p)
            self.particules[-1].cv =self.canvas.create_oval(self.particules[-1].x-self.particules[-1].m, self.particules[-1].y-self.particules[-1].m, self.particules[-1].x+self.particules[-1].m, self.particules[-1].y+self.particules[-1].m)
            self.canvas.itemconfig(self.particules[-1].cv, fill=self.particules[-1].color) # change color


        for idx, p_ in enumerate(self.particules):
            if idx >0:
                for idy , py_ in enumerate(self.particules):
                    if idx != idy:
                        dx=  (self.particules[idy].x - self.particules[idx].x)
                        dy= (self.particules[idy].y  -self.particules[idx].y)
                        d = ((dx)**2 + (dy)**2)**0.5
                        f = self.G * (volume(self.particules[idy].m)) / (d**2)

                        dx/=d
                        dy/=d
                        self.particules[idx].a=[f*dx,f*dy]
                        if abs(self.particules[idx].a[0])>self.lim:
                            self.particules[idx].a[0]=np.sign(self.particules[idx].a[0])*self.lim
                        if abs(self.particules[idx].a[1])>self.lim:
                            self.particules[idx].a[1]=np.sign(self.particules[idx].a[1])*self.lim
                        self.particules[idx].v=[self.particules[idx].v[0]+self.particules[idx].a[0]*self.dt,self.particules[idx].v[1]+self.particules[idx].a[1]*self.dt]

                        self.particules[idx].x +=  self.particules[idx].v[0]*self.dt
                        self.particules[idx].y +=  self.particules[idx].v[1]*self.dt

            self.canvas.coords(self.particules[idx].cv,self.particules[idx].x-self.particules[idx].m, self.particules[idx].y-self.particules[idx].m, self.particules[idx].x+self.particules[idx].m, self.particules[idx].y+self.particules[idx].m)

        toremove=[]
        for idx, p_ in enumerate(self.particules):
            if not(idx in toremove):
                closest=None
                dm=999999999999
                for idy, py_ in enumerate(self.particules):
                    if not(idx in toremove) and (idy != idx):
                        dx =self.particules[idx].x - self.particules[idy].x
                        dy =self.particules[idx].y - self.particules[idy].y
                        d= (dx**2+dy**2)**.5
                        if dm>d:
                            dm=d
                            closest = idy
                if closest!=None and self.particules[idx].m > self.particules[closest].m :
                    if dm<self.particules[idx].m:
                        toremove.append(closest)
                        v1 =  4. * np.pi * (self.particules[idx].m**3) / 3.
                        v2 =  4. * np.pi * (self.particules[closest].m**3) / 3.
                        m=((v1+v2)*3./(4*np.pi))**(1./3.)

                        if idx != 0:
                            m1=volume(self.particules[idx].m)
                            m2=volume(self.particules[closest].m)
                            self.particules[idx].v[0]=(self.particules[idx].v[0]*m1+ m2*(self.particules[closest].v[0])) / (m1+m2)
                            self.particules[idx].v[1]=(self.particules[idx].v[1]*m1+ m2*(self.particules[closest].v[1])) / (m1+m2)
                            self.particules[idx].m = m
            self.particules[idx].x +=  self.particules[idx].v[0]*self.dt
            self.particules[idx].y +=  self.particules[idx].v[1]*self.dt
        toremove=list(set(toremove))
        for i in sorted(toremove,reverse=True):
            self.canvas.delete(self.particules[i].cv)
            self.particules.pop(i)
        self.canvas.update()

        return


def run():
    root2 = MyApp()

    i = 0
    while 1:
        root2.update_drops()
        root2.after(1)

run()
