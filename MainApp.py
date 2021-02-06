from PID import PID
import threading 
import time
import math
import cmath
import os.path
import matplotlib.pyplot as plt
import os
from pysondb import db
import json
from myBoat import myBoat 
myBoat = myBoat() 
XCoord = 0.0
YCoord = 0.0
Angle = 0.5*math.pi
timeData = []
velocityData = []
headingData = []
samplePeriod = 0.25
count = 0
DistanceToTarget = 5
DistanceToTargetY = 0.1
FarDistanceModeSpeed = 5
a=db.getDb("db.json")
def control_loop(num): 
    n = 0
    startTime = time.time()
    checkValue = 1
    while 1 > 0:
        
        if(time.time() > startTime):
            startTime += 0.11
            global count
            global headingData
            global velocityData
            global timeData
            headingData.append(myBoat.getHeading())
            velocityData.append(myBoat.getVelocity())
            timeData.append(count*samplePeriod)
            count = count + 1
            tempComplex = complex(XCoord-myBoat.getXCoordinate(),YCoord-myBoat.getYCoordinate()) #rename to destinationX, destinationY
            tempPolar = cmath.polar(tempComplex)            
            PIDAngle = PIDA.regulator(tempPolar[1]-myBoat.getHeading())
            angle = tempPolar[1]
            if angle < 0:
                angle = angle + 2 * math.pi
            if checkValue > tempPolar[0]:
                checkValue = 1.5
                print("We are in the close distance step")
                print(XCoord)
                print(YCoord)
                print(PIDA.getKp())
                #More vector calculus YAY!
                vf = tempPolar[0] * math.cos (tempPolar[1]-myBoat.getHeading())
                vs = tempPolar[0] * math.sin (tempPolar[1]-myBoat.getHeading())
                closeXspeed = PIDX.regulator(vf)
                closeYspeed = PIDY.regulator(vs)
                myBoat.updateSpeed(closeXspeed,closeXspeed,closeYspeed,"#2C2020")
            else:
                myBoat.updateSpeed(FarDistanceModeSpeed+PIDAngle, FarDistanceModeSpeed-PIDAngle, 0)
                checkValue = 1
            n = n+1
            if n > 250:
                break

  
def update_db_loop(num): 
    endTime = time.time() + 1
    i = 0
    global XCoord
    global YCoord
    while 1 > 0:       
        if(time.time()> endTime):
            if os.path.isfile('updatedDB.txt'):
                print("I am updating all values")
                data = a.getAll()
                for x in data:
                    print(x)
                XCoord = float(data[0]["value"])
                YCoord = float(data[1]["value"])
                PIDA.setKp(float(data[2]["value"]))
                PIDA.setKi(float(data[3]["value"]))
                PIDA.setKd(float(data[4]["value"]))
                PIDX.setKp(float(data[5]["value"]))
                PIDX.setKi(float(data[6]["value"]))
                PIDX.setKd(float(data[7]["value"]))
                PIDY.setKp(float(data[8]["value"]))
                PIDY.setKi(float(data[9]["value"]))
                PIDY.setKd(float(data[10]["value"]))
                os.remove("updatedDB.txt")
            else:
                print("I am checking again in 5 seconds")
                endTime = time.time() +5
                
                i = i + 1
            if i > 4:
                break
        

            
  
if __name__ == "__main__": 
    PIDA = PID(0.0,0.0,0.0)#PID(32,0.01,0.1)
    PIDX = PID(0.0,0.0,0.0)#PID(0.4,0.002,0.1)
    PIDY = PID(0.0,0.0,0.0)#PID(0.4,0.002,0.1)
    n = 0
    t1 = threading.Thread(target=update_db_loop, args=(10,)) 
    t2 = threading.Thread(target=control_loop, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
    #myBoat.printMap()
    plt.figure(2)
    plt.plot(timeData,velocityData)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')  
    plt.show()
