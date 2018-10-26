# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
import numpy as np
from tkinter import *
import random
import colorsys
import itertools

def startpatern():
    return [[0,2,2,2,2,2,2,2,2,0,0,0,0,0],
            [2,1,7,0,1,4,0,1,4,2,0,0,0,0],
            [2,0,2,2,2,2,2,2,0,2,0,0,0,0],
            [2,7,2,0,0,0,0,2,1,2,0,0,0,0],
            [2,1,2,0,0,0,0,2,1,2,0,0,0,0],
            [2,0,2,0,0,0,0,2,1,2,0,0,0,0],
            [2,7,2,0,0,0,0,2,1,2,0,0,0,0],
            [2,1,2,2,2,2,2,2,1,2,2,2,2,2],
            [2,0,7,1,0,7,1,0,7,1,1,1,1,1],
            [0,2,2,2,2,2,2,2,2,2,2,2,2,2]]


def colorT(c):
    return '#%02x%02x%02x' % tuple(c)

class LangtonsLoop(Tk):
    def __init__(self):
        self.nbi=0


        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        width =np.int(800)
        height = np.int(600)
        self.canvas  = Canvas(fr, height = height, width = width)#,bg= 'black')
        self.canvas.pack()
        self.w = int(width/10)
        self.h = int(height/10)
        self.Matpoint = np.zeros((self.h*2,self.w*2),dtype=int)
        self.Matpointcopy = np.zeros((self.h*2,self.w*2),dtype=int)
        P = np.array(startpatern())
        # self.Matpoint[self.h//2-P.shape[0]//2:self.h//2+P.shape[0]//2, self.w//2-P.shape[1]//2:self.w//2+P.shape[1]//2] = P
        self.Matpoint[self.h-P.shape[0]//2:self.h+P.shape[0]//2, self.w-P.shape[1]//2:self.w+P.shape[1]//2] = P

        self.scale = width/float(self.w)
        if self.scale > height/float(self.h):
            self.scale = height/float(self.h)
        self.ant = [self.h//2,self.w//2]


        o=self.canvas.create_rectangle(0, 0,width,height)
        self.canvas.itemconfig(o, fill="black")

        self.circle=self.Matpoint.tolist()

        self.color = ['black','blue','red','green','yellow','pink','white','cyan']

        self.rules_str = np.loadtxt('misc\LangtonsLoopRules.txt',dtype='str')
        self.rules = np.array([[int(i) for i in rule] for rule in self.rules_str])

        zero        =[]
        one         =[]
        two         =[]
        three       =[]
        four        =[]
        five        =[]
        six         =[]
        seven       =[]
        for k in list(self.rules):
            if k[0]==0:
                zero.append(k)
            elif k[0]==1:
                one.append(k)
            elif k[0]==2:
                two.append(k)
            elif k[0]==3:
                three.append(k)
            elif k[0]==4:
                four.append(k)
            elif k[0]==5:
                five.append(k)
            elif k[0]==6:
                six.append(k)
            elif k[0]==7:
                seven.append(k)
        self.rules = [np.array(zero), np.array(one), np.array(two), np.array(three), np.array(four), np.array(five) , np.array(six), np.array(seven)]


        for i in range(self.Matpoint.shape[0]):
            for j in range(self.Matpoint.shape[1]):
                self.circle[i][j]=self.canvas.create_oval((j-self.w//2)*self.scale, (i-self.h//2)*self.scale,(j-self.w//2)*self.scale+self.scale, (i-self.h//2)*self.scale+self.scale)
                self.canvas.itemconfig(self.circle[i][j], fill=self.color[self.Matpoint[i,j]])
        self.canvas.update()
        self.end =True

    def update(self ):
        listchange =[]
        self.Matpointcopy = self.Matpoint+0
        for i in range(1,self.Matpoint.shape[0]-1):
            for j in range(1,self.Matpoint.shape[1]-1):

                cur = self.Matpointcopy[i,j]
                neighbor1 = [self.Matpointcopy[i-1,j],self.Matpointcopy[i,j+1],self.Matpointcopy[i+1,j],self.Matpointcopy[i,j-1]]
                neighbor2 = [self.Matpointcopy[i,j-1],self.Matpointcopy[i-1,j],self.Matpointcopy[i,j+1],self.Matpointcopy[i+1,j]]
                neighbor3 = [self.Matpointcopy[i+1,j],self.Matpointcopy[i,j-1],self.Matpointcopy[i-1,j],self.Matpointcopy[i,j+1]]
                neighbor4 = [self.Matpointcopy[i,j+1],self.Matpointcopy[i+1,j],self.Matpointcopy[i,j-1],self.Matpointcopy[i-1,j]]

                permut = [neighbor1,neighbor2,neighbor3,neighbor4]
                if cur == 0 and (neighbor1 == [0,0,0,0]):
                    pass
                else:
                    for vec in permut:
                        idx = np.where((vec == self.rules[cur][:,1:5]).all(1))[0]
                        if  not idx.size == 0:
                            idx = idx[0]
                            self.Matpoint[i,j] = self.rules[cur][idx,5]
                            if not cur == self.Matpoint[i,j]:
                                listchange.append([i,j])
                            break

        for idx in listchange:
            self.canvas.itemconfig(self.circle[idx[0]][idx[1]], fill=self.color[self.Matpoint[idx[0],idx[1]]])



        # print(self.Matpoint)

        self.canvas.update()

        return
def run():
    root = LangtonsLoop()
    root.title("Langton's Loop")
    i=0
    while root.end:
        try:
            root.update( )
            root.after(10)
            i+=1
        except Exception:
            root.close_window()
            #print("Terminating")
            #exit()

run()