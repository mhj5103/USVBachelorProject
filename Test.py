import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
from Axes import Axes
from Point import Point
from myBoat import myBoat 
from PID import PID
print("Start of Program")
myBoat = myBoat()
myBoat.printInfo()
myBoat.setHeading(500,500)
myBoat.printInfo()
for i in range(20):
    print("________________________________________")
    print("iteration " + str(i) )
    print(myBoat.getXCoordinate())
    myBoat.updateSpeed(10.0,10.0,0.0)
for i in range(20):
    print("________________________________________")
    print("iteration " + str (i+20))
    
    myBoat.updateSpeed(10,-10,0,"#2C2020")
for i in range(20):
    myBoat.updateSpeed(10,10,0)
myBoat.convertInput(1100)
myBoat.printMap()