import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
from Axes import Axes
from Point import Point
class myBoat:
    def __init__(self, VelocityX, VelocityY, Heading, drag, k):
        self.VelocityX = VelocityX
        self.VelocityY = VelocityY
        self.Heading = Heading
        self.drag = drag
        self.k = k * 2 * math.pi
        self.x = 0
        self.y = 0
        self.xHeading = 0
        self.yHeading = 0
        self.axes = Axes(xlim=(-50000,50000), ylim=(-50000,50000), figsize=(9,7))

    def updateSpeed(self, VelocityRight, VelocityLeft, VelocityMiddle):
        self.VelocityX = self.VelocityX - self.VelocityX*self.drag + math.sin(self.Heading)*VelocityMiddle + math.cos(self.Heading) * VelocityLeft + math.cos(self.Heading) * VelocityRight
        self.VelocityY = self.VelocityY - self.VelocityY*self.drag + math.cos(self.Heading)*VelocityMiddle + math.sin(self.Heading) * VelocityLeft + math.sin(self.Heading) * VelocityRight
        self.Heading = self.Heading + (VelocityLeft-VelocityRight)*self.k
        self.x = self.x + self.VelocityX
        self.y = self.y + self.VelocityY
        self.axes.addPoint(Point(self.x,  self.y, color='#ffa500'))

    def printInfo(self):
        print("The speed on x-axis is: ")
        print(self.VelocityX)
        print("The speed on y-axis is: ")
        print(self.VelocityY)
        print("The heading is: ")
        print(self.Heading)
        print("The destination is: ")
        print(self.xHeading)
        print(self.yHeading)

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
