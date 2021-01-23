from PID import PID
import threading 
import time
import math
import cmath
import os.path
import os
from pysondb import db
import json
from myBoat import myBoat 
myBoat = myBoat() 
XCoord = 0 
YCoord = 0
Angle = 0.5*math.pi
DistanceToTarget = 5
DistanceToTargetY = 0.1
FarDistanceModeSpeed = 5
a=db.getDb("db.json")
def control_loop(num): 
    n = 0
    startTime = time.time()
    checkValue = 10
    while 1 > 0:
        
        if(time.time() > startTime):
            startTime += 0.00001
           
            tempComplex = complex(XCoord-myBoat.getXCoordinate(),YCoord-myBoat.getYCoordinate()) #rename to destinationX, destinationY
            tempPolar = cmath.polar(tempComplex)            
            PIDAngle = PIDA.regulator(tempPolar[1]-myBoat.getHeading())
            angle = tempPolar[1]
            if angle < 0:
                angle = angle + 2 * math.pi
            print("Im updating current coordinates and calculating angles + distances")
            print("We are on iteration:", n)
            print("The angle is: ",  tempPolar[1])
            print("The angle PID value is: ", PIDAngle)
            if checkValue > tempPolar[0]:
                checkValue = 15
                print("We are in the close distance step")
                #More vector calculus YAY!
                vf = tempPolar[0] * math.cos (tempPolar[1]-myBoat.getHeading())
                vs = tempPolar[0] * math.sin (tempPolar[1]-myBoat.getHeading())
                print(f"vf is : {vf}")
                print(f"vs is : {vs}")
                closeXspeed = PIDX.regulator(vf)
                closeYspeed = PIDY.regulator(vs)
                myBoat.updateSpeed(closeXspeed,closeXspeed,closeYspeed,"#2C2020")
            else:
                myBoat.updateSpeed(FarDistanceModeSpeed+PIDAngle, FarDistanceModeSpeed-PIDAngle, 0)
                checkValue = 10
            n = n+1
            if n > 2000:
                break

  
def update_db_loop(num): 
    endTime = time.time() + 5
    i = 0
    while 1 > 0:       
        if(time.time()> endTime):
            if os.path.isfile('updatedDB.txt'):
                print("I am updating all values")
                data = a.getAll()
                for x in data:
                    print(x)
                XCoord = data[0]["value"]
                YCoord = data[1]["value"]
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
            if i > 0:
                break
        

            
  
if __name__ == "__main__": 
    PIDA = PID(24,0.01,0.1)
    PIDX = PID(0.4,0.002,0.1)
    PIDY = PID(0.4,0.002,0.1)
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
    myBoat.printMap()