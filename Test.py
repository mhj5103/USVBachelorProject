import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
from Axes import Axes
from Point import Point
from myBoat import myBoat 
from PID import PID
print("Start of Program")
myBoat = myBoat(0,0,0,0.3,0.001)
myBoat.printInfo()
myBoat.setHeading(500,500)
myBoat.printInfo()
for i in range(20):
    myBoat.updateSpeed(10,10,0)
for i in range(20):
    myBoat.updateSpeed(10,0,0)
for i in range(20):
    myBoat.updateSpeed(10,10,0)

myBoat.printMap()