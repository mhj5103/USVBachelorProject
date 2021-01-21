import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
from Axes import Axes
from Point import Point
import cmath
class myBoat:
    def __init__(self):
        self.printInfoVar = 0
        self.VelocityX = 0.0
        self.VelocityY = 0.0
        self.Velocity = 0.0 # m/s
        self.Heading = 0.0 # is the angle where the boat is facing.
        self.Direction = 0.0 # Is the angle in which direction the boat is moving 
        self.kf = 4 # The drag coefficient from the forward movement
        self.ks = 8 # The drag coeffictient from the sideway movement
        self.mm = 0.0005 * 2 * math.pi  # How quickly the boat changes heading
        self.x = 0.0 # Current x coordinate
        self.y = 0.0 # Current y coordinate
        self.axes = Axes(xlim=(-400,400), ylim=(-400,400), figsize=(9,7))
        self.weight = 4.0 # kg
        self.samplePeriod = 0.25 # s

    def updateSpeed(self, NewtonRight, NewtonLeft, NewtonMiddle, colour = "#ffa500"):
        #Velocity vector
        
        if NewtonRight > 10 :
            NewtonRight = 10
        if NewtonLeft > 10 :
            NewtonLeft = 10
        temp1 = NewtonLeft
        temp2 = NewtonRight
        print(f"NewtonRight is : {temp1}")
        print(f"Newtonleft is : {temp2}")
        print(f"XCoord is : {self.x}")
        print(f"YCoord is : {self.y}")
        vx = self.Velocity * math.cos(self.Direction)
        vy = self.Velocity * math.sin(self.Direction)
       
        # We now rotate the axis so it alligns it self with the boat, so the boats is exactly along the x and y axis in the new coordinate system
        alpha = self.Direction
        theta = self.Heading
        
        vf = self.Velocity * math.cos (alpha - theta)
        vs = self.Velocity * math.sin (alpha - theta)
        

        # We now calculate the drag on the boat
        dragf = -vf * self.kf
        drags = -vs * self.ks
        
        #We can now rotate the drag back into our original coordinate system
        dragx = dragf * math.cos(theta) - drags * math.sin(theta)
        dragy = dragf * math.sin(theta)  + drags * math.cos(theta)
        
        #We can now calculate the thrust we have from the 2 engines
        tx = (NewtonLeft + NewtonRight) * math.cos(self.Heading)
        ty = (NewtonLeft + NewtonRight) * math.sin(self.Heading)

        if self.printInfoVar == 1:
            print(f"vx is : {vx}")
            print(f"vy is : {vy}")
            print(f"alpha is : {alpha}")
            print(f"theta is : {theta}")
            print(f"vf is : {vf}")
            print(f"vs is : {vs}")
            print(f"dragf is : {dragf}")
            print(f"drags is : {drags}")
            print(f"dragx is : {dragx}")
            print(f"dragy is : {dragy}")
            print(f"tx is : {tx}")
            print(f"ty is : {ty}")
        #We can add up the total forces and add the total velocity added to the boat in the sampling period
        vnewx = vx + (dragx + tx) * self.samplePeriod / self.weight
        vnewy = vy + (dragy + ty) * self.samplePeriod / self.weight
        
        #We can now calculate the variables we need for next cycle
        self.Velocity = math.sqrt(math.pow(vnewx,2) + math.pow(vnewy,2))
        tempComplex = complex(vnewx,vnewy)
        self.Direction = cmath.phase(tempComplex)
        self.Heading = self.Heading + (NewtonRight - NewtonLeft) * self.mm

        #Updating the current position
        self.x = vnewx + self.x
        self.y = vnewy + self.y

        #Updating the map with coordinates
        self.axes.addPoint(Point(self.x,  self.y, color=colour))

        # source for vector math https://en.wikipedia.org/wiki/Rotation_of_axes#:~:text=If%20the%20curve%20(hyperbola%2C%20parabola,called%20a%20transformation%20of%20coordinates.

    def printInfo(self):
        print("The velocity is: ")
        print(self.Velocity)
        print("The heading is: ")
        print(self.Heading)
        print("The Direction is: ")
        print(self.Direction)

    def printMap(self):
        self.axes.draw()

    def getXCoordinate(self):
        return self.x

    def getYCoordinate(self):
        return self.y 

    def getDiffDistance(self):
        a = math.pow((self.xHeading-self.x),2)
        b = math.pow((self.yHeading-self.y),2)
        return math.sqrt(a+b)

    def getDiffAngle(self):
        a = self.xHeading-self.x
        b = self.yHeading-self.y
        return math.atan(b/a)

    def setHeading(self, xheading, yheading):
        self.xHeading = xheading
        self.yHeading = yheading
        
    def convertInput(self, input):
        #polynomial = [-5.8859e-27,5.2262e-23,-1.0801e-19,-5.3918e-16, 3.9074e-12,-1.1351e-08,1.9300e-05,-2.0620e-02,1.3693e+01,-5.1876e+03,8.5959e+05]
        polynomial = [0.000000021706, -0.000095639135, 0.143970308054, -74.013419146878]
        convertedResult = 0
        i = 3
        for x in polynomial:
            convertedResult = x * pow(input,i) + convertedResult
            i = i - 1
        print(convertedResult)
