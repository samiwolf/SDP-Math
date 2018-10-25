from tkinter import *
import math
import time

class MyGui:    #(fold) 
    def __init__(self):
        self.canvas_width  = 400
        self.canvas_height = 400

    def initGui(self):
        SLIDER_INIT = 5
        RADIO_INIT  = 1
        self.radio_value   = SLIDER_INIT
        self.slider_value  = RADIO_INIT

        tk = Tk()
        tk.title("Riemann Sum")
        tk.resizable(0,0)
        self.canvas = Canvas(tk, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0,column=0,columnspan=2,rowspan=5)

        #Radio buttons
        self.radio_choice  = IntVar()
        self.radio_choice.set(RADIO_INIT)
        radio_options = [("left",1),("middle",2),("right",3)]

        Label(tk, text="""Choose an endpoint""", justify=LEFT,padx=20).grid(row=0,column=2)

        for txt,val in radio_options:
            Radiobutton(tk,
                        text=txt,
                        padx=20,
                        variable=self.radio_choice,
                        value=val,
                        command=self.updateCanvas).grid(row=0,column=val+2)

        #Slider button
        self.mySlide=Scale(tk, 
                      from_=1, 
                      to=50, 
                      orient=HORIZONTAL, 
                      length=200,
                      command=self.updateCanvas)
        self.mySlide.grid(row=1,column=3)
        self.mySlide.set(SLIDER_INIT)

        #Labels
        self.area_label  = Label(tk,text="Computed Area: ")
        self.area_label.grid(row=2,column=2)
        self.error_label = Label(tk,text="Error: ")
        self.error_label.grid(row=3,column=2)

        mainloop()

    def updateCanvas(self, other=None):
        #Define some local variables
        c = self.canvas
        numInts  = self.mySlide.get()
        endpoint = self.radio_choice.get()
        leftEndPoint = 0
        lengthOfInt  = 1.0/numInts
        YHEIGHT = 2.0
        XWIDTH  = 1.0
        cwidth  = self.canvas_width/XWIDTH
        cheight = self.canvas_height/YHEIGHT
       
        c.delete("all")

        #A function which determines the height of the function
        @staticmethod
        def getHeight(end, left, length):
            # gives the left, middle, or right endpoint depending on end.
            point = left + (end-1)*length/2
            return 1+point*point

        # Loop over the intervals and draw the rectangles. Also keep track
        # of the area
        total_area = 0
        for it in range(1,numInts+1):
            height = getHeight.__func__(end=endpoint,left=leftEndPoint,
                                length=lengthOfInt)
            total_area = total_area+height*lengthOfInt
            #Since the y-axis is inverted, we need to use 1-height, and
            #convert everything to pixels
            x1 = leftEndPoint*cwidth
            x2 = x1 + lengthOfInt*cwidth
            y  = (YHEIGHT-height)*cheight
            
            c.create_rectangle(x1,self.canvas_width,x2,y,fill="red")

            #Once finished this rectangle, update
            leftEndPoint = leftEndPoint+lengthOfInt

        # Once the rectangles have been drawn, draw the function
        xy=[]
        for it in range(1,self.canvas_width+1):
            #X coordinate
            xy.append(it)
            #Y coordinate
            xy.append(self.canvas_height-int(200*(1+math.pow(it/400.0,2))))

        c.create_line(xy,fill='blue', width=2)

        # Update the labels
        self.area_label['text']="Computed Area: {0:>0.06f}".format(total_area)
        self.error_label['text']="Error Percentage: {0:>0.6f}".format(4.0/3-total_area)
# (end)

if __name__ == '__main__':
    thegui = MyGui()
    thegui.initGui()

