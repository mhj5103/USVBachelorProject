
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
from Axes import Axes
from Point import Point
from myBoat import myBoat 
from PID import PID
import logging
print("Start of Program")
myBoat = myBoat()
logging.basicConfig(filename='app.log', filemode='w', format='%(message)s', level=logging.INFO)
timeData = []
velocityData = []
headingData = []
samplePeriod = 0.25
count = 0

#This functions produces the log file
def logThisLine(iteration):
    logging.info(f"We are on iteration : {iteration}")
    logging.info(f"X position is : {myBoat.getXCoordinate()}")
    logging.info(f"Y position is : {myBoat.getYCoordinate()}")
    logging.info(f"Heading is : {myBoat.getHeading()}")
    logging.info(f"Velocity is : {myBoat.getVelocity()}")
    logging.info(f"Direction is : {myBoat.getDirection()/2*math.pi*360}")

#This functions runs the first test scenario as described in the report
def fowardTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    count = count + 1
    for i in range(50):
        myBoat.updateSpeed(10.0,10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    for i in range (50):
        myBoat.updateSpeed(0.0,0.0,0.0)
        velocityData.append(myBoat.getVelocity())
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.figure(1)
    plt.show()
def backwardTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    count = count + 1
    for i in range(50):
        myBoat.updateSpeed(-10.0,-10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    for i in range (50):
        myBoat.updateSpeed(0.0,0.0,0.0)
        velocityData.append(myBoat.getVelocity())
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.figure(1)
    plt.show()

def rotateLeftTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    headingData.append(myBoat.getHeading())
    count = count + 1
    for i in range(400):
        myBoat.updateSpeed(10.0,-10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.figure(1)
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.show()
    plt.figure(2)
    plt.plot(timeData,headingData)
    plt.ylabel('Heading (m/s)')
    plt.xlabel('Time (s)')  
    plt.show()

def rotateRightTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    headingData.append(myBoat.getHeading())
    count = count + 1
    for i in range(400):
        myBoat.updateSpeed(-10.0,10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.figure(1)
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')
    plt.show()
    plt.figure(2)
    plt.plot(timeData,headingData)
    plt.ylabel('Heading (radians)')
    plt.xlabel('Time (s)')  
    plt.show()


def turnLeftTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    headingData.append(myBoat.getHeading())
    count = count + 1
    for i in range(50):
        myBoat.updateSpeed(10.0,0.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    for i in range(50):
        myBoat.updateSpeed(10.0,10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.figure(2)
    plt.plot(timeData,headingData)
    plt.ylabel('Heading (radians)')
    plt.xlabel('Time (s)')  
    plt.show()

def turnRightTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    headingData.append(myBoat.getHeading())
    count = count + 1
    for i in range(50):
        myBoat.updateSpeed(0.0,10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    for i in range(50):
        myBoat.updateSpeed(10.0,10.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.figure(2)
    plt.plot(timeData,headingData)
    plt.ylabel('Heading (radians)')
    plt.xlabel('Time (s)')  
    plt.show()

def noMotionTestCase():
    count = 0
    velocityData.append(myBoat.getVelocity())
    timeData.append(count*samplePeriod)
    headingData.append(myBoat.getHeading())
    count = count + 1
    for i in range(50):
        myBoat.updateSpeed(0.0,0.0,0.0)
        velocityData.append(myBoat.getVelocity())
        headingData.append(myBoat.getHeading()% (2*math.pi))
        timeData.append(count*samplePeriod)
        logThisLine(count)
        count = count + 1
    plt.figure(2)
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')  
    plt.show()

backwardTestCase()
myBoat.printMap()