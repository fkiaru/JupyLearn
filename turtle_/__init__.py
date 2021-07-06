import os.path
import math
import time
from ipywidgets import widgets
from notebook import nbextensions
from traitlets import Unicode, List
from IPython.display import display

__version__ = '0.5'

def install_js():
    pkgdir = os.path.dirname(__file__)
    nbextensions.install_nbextension(os.path.join(pkgdir, 'mobilechelonianjs'),
                                     user=True)

class Turtle(widgets.DOMWidget):
    """ Help on turtle :
        inline turtle object
        
        methods:
        
        
    """
    _view_module = Unicode("nbextensions/mobilechelonianjs/turtlewidget").tag(sync=True)
    _view_name = Unicode('TurtleView').tag(sync=True)
    # TODO: Make this an eventful list, so we're not transferring the whole
    # thing on every sync
    points = List(sync=True)
    param =  List(sync=True)
    initTest = List(sync=True)
    SIZE = 400
    OFFSET = 20
    def __init__(self,sXY=[500,350],bkColor="#FFFFAA",tColor='#008A00'):
        '''Create a Turtle.

        Example::

            t = Turtle()
        '''
        self.initTest = [sXY[0],sXY[1],bkColor,tColor]
        self.points = []
        self.param=[]
        #print('call super');
        super(Turtle, self).__init__()
        #print('called super');
        #print(self.param);
        install_js()
        display(self)
        self.pen = 1
        self.speedVar = 1
        self.color = "black"
        self.bearing = 90
        
        self.points = []
        self.param=[]
        self.home()
        time.sleep(0.1)
    def penDown(self):
        '''Put down the pen. Turtles start with their pen down.

        Example::

            t.pendown()
        '''
        self.pen = 1

    def penUp(self):
        '''Lift up the pen.

        Example::

            t.penup()
        '''
        self.pen = 0

    def speed(self, speed):
        '''Change the speed of the turtle (range 1-10).

        Example::

            t.speed(10) # Full speed
        '''
        self.speedVar = min(max(1, speed), 10)

    def right(self, num):
        '''Turn the Turtle num degrees to the right.

        Example::

            t.right(90)
        '''
        num=int(num)
        self.bearing += num
        self.bearing = self.bearing%360
        self.b_change = num
        self._add_point()

    def left(self, num):
        '''Turn the Turtle num degrees to the left.

        Example::

            t.left(90)
        '''
        num=int(num)
        self.bearing -= num
        self.bearing = self.bearing%360
        self.b_change = -num
        self._add_point()

    def forward(self, num):
        '''Move the Turtle forward by num units.

        Example:

            t.forward(100)
        '''
        sXY=self.param[0]["sXY"]
        self.posX += round(num * math.sin(math.radians(self.bearing)), 1)
        self.posY -= round(num * math.cos(math.radians(self.bearing)), 1)

        if self.posX < Turtle.OFFSET:
            self.posX = Turtle.OFFSET
        if self.posY < Turtle.OFFSET:
            self.posY = Turtle.OFFSET

        if self.posX > sXY[0] - Turtle.OFFSET:
            self.posX = sXY[0] - Turtle.OFFSET
        if self.posY > sXY[1] - Turtle.OFFSET:
            self.posY = sXY[1]- Turtle.OFFSET

        self.b_change = 0
        self._add_point()

    def backward(self, num):
        '''Move the Turtle backward by num units.

        Example::

            t.backward(100)
        '''
        sXY=self.param[0]["sXY"]
        self.posX -= round(num * math.sin(math.radians(self.bearing)), 1)
        self.posY += round(num * math.cos(math.radians(self.bearing)), 1)

        if self.posX < Turtle.OFFSET:
            self.posX = Turtle.OFFSET
        if self.posY < Turtle.OFFSET:
            self.posY = Turtle.OFFSET

        if self.posX > sXY[0] - Turtle.OFFSET:
            self.posX = sXY[0] - Turtle.OFFSET
        if self.posY > sXY[1] - Turtle.OFFSET:
            self.posY = sXY[1]- Turtle.OFFSET

        self.b_change = 0
        self._add_point()

    def penColor(self, color):
        '''Change the color of the pen to color. Default is black.

        Example::

            t.pencolor("red")
        '''
        self.color = color
    def bkColor(self,nbkC):
        '''Change the background color. 

        Example::

            t.bkColor("white")
        '''
        
        self.param[0]["bkC"]=nbkC
        self.param= self.param+[0] # update !!
        self.param.pop()# remove last!
        
    def penWidth(self,penS):
        '''Change the pen width. zero is no pen

        Example::

            t.pendWidth(2)
        '''
        self.pen=penS
        self.param[0]["pS"]=penS
        self.param= self.param+[0] # update !!
        self.param.pop()# remove last!
        
    def tColor(self,tColor):
        '''Change the turtle color

        Example::

            t.tColor("yellow")
        '''
        self.param[0]["tC"]=tColor
        self.param= self.param+[0] # update !!
        self.param.pop()# remove last!
        
    def tShowStatus(self,state):
        ''' Change the turtle show status

        Example::

            t.tShowStatus(1) % show
            t.tShowStatus(1) % hide
            
        '''
        self.param[0]["tS"]=state
        self.param= self.param+[0] # update !!
        self.param.pop()# remove last!
        
    def hide(self):
        ''' Hide the turtle show status

        Example::

            t.hide() 
        '''
        self.tShowStatus(0)
    def show(self):
        ''' Show the turtle show status

        Example::

            t.show() 
        '''
        self.tShowStatus(1)    
        
    def setPosition(self, x, y, bearing=None):
        """Change the position of the turtle.

        Example::

            t.setposition(100, 100)
        """
        self.posX = x
        self.posY = y
        if bearing is None:
            self._add_point()
        elif isinstance(bearing, int):
            self.setbearing(bearing)
        else:
            raise ValueError("Bearing must be an integer")

    def setBearing(self, bearing):
        """Change the bearing (angle) of the turtle.

        Example::

            t.setbearing(180)
        """
        diff = self.bearing - bearing
        self.b_change = diff
        self.bearing = bearing
        self._add_point()
        self.b_change = 0

    def _add_point(self):
        if len(self.param)==0:
            #("self.initTest ",self.initTest)
            p1 = dict(sXY=[self.initTest[0],self.initTest[1]],
            bkC=self.initTest[2],tC=self.initTest[3],tS=1,pS=3,
            tClear=0)
            self.param= self.param+[p1]
            #print("created param")
        else:
            #print("do not update")
            self.param= self.param+[0] # update !!
            self.param.pop()# remove last!
        p = dict(p=self.pen, lc=self.color, x=self.posX, y=self.posY,
                 b=self.b_change, s=self.speedVar)
        self.points = self.points + [p]

    def circle(self, radius, extent=360):
        """Draw a circle, or part of a circle.

        From its current position, the turtle will draw a series of short lines,
        turning slightly between each. If radius is positive, it will turn to
        its left; a negative radius will make it turn to its right.

        Example::

            t.circle(50)
        """
        temp = self.bearing
        self.b_change = 0;
        tempSpeed = self.speedVar
        self.speedVar = 1

        for i in range(0, (extent//2)):
            n = math.fabs(math.radians(self.b_change) * radius)
            if(radius >= 0):
                self.forward(n)
                self.left(2)
            else:
                self.forward(n)
                self.right(2)
        if(radius >= 0):
            self.bearing = (temp + extent)
        else:
            self.bearing = (temp - extent)
        self.speedVar = tempSpeed
# SHORTS
    def fd(self,x):
        """ short for 'forward' 
        """
        self.forward(x)
    def bk(self,x):
        """ short for 'backward' 
        """
        self.backward(x)
    def rt(self,x):
        """ short for 'right turn' 
        """
        self.right(x)
    def lt(self,x):
        """ short for 'left turn' 
        """
        self.left(x)
    def up(self):
        """ short for 'penUp' 
        """
        self.penUp()
    def dw(self):
        """ short for 'penDown' 
        """
        self.penDown()
    def pendown(self):
        """ other name  'penDown' 
        """
        self.penDown()
    def penup(self):
        """ other name for 'penUp' 
        """
        self.penUp()
    def pencolor(self,x):
        """ other namefor 'pencColor' 
        """
        self.penColor(x)
        
    def home(self):
        '''Move the Turtle to its home position.

        Example::

            t.home()
        '''
        
        if len(self.param)==0:
            sXY=[self.initTest[0],self.initTest[1]]
        else:
            sXY=self.param[0]["sXY"]
        self.posX = sXY[0]//2
        self.posY = sXY[1]//2
        if 90 < self.bearing <=270:
            self.b_change = - (self.bearing - 90)
        else:
            self.b_change = 90 - self.bearing
        self.bearing = 90
        self._add_point()