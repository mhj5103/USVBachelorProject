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
XCoord = 50.0
YCoord = -50.0
Angle = 0.5*math.pi
DistanceToTarget = 5
DistanceToTargetY = 0.1
FarDistanceModeSpeed = 5
a=db.getDb("db.json")
def control_loop(num): 
    n = 0
    startTime = time.time()
    while 1 > 0:
        
        if(time.time() > startTime):
            startTime += 0.01
           
            tempComplex = complex(XCoord-myBoat.getXCoordinate(),YCoord-myBoat.getYCoordinate())
            tempPolar = cmath.polar(tempComplex)            
            PIDAngle = PIDA.regulator(tempPolar[1])
            print("Im updating current coordinates and calculating angles + distances")
            print("We are on iteration:", n)
            print("The angle is: ",  tempPolar[1])
            print("The angle PID value is: ", PIDAngle)
            myBoat.updateSpeed(FarDistanceModeSpeed-PIDAngle, FarDistanceModeSpeed+PIDAngle, 0)
            n = n+1
            if n > 400:
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
                PIDD.setKp(float(data[5]["value"]))
                PIDD.setKi(float(data[6]["value"]))
                PIDD.setKd(float(data[7]["value"]))
                PID3.setKp(float(data[8]["value"]))
                PID3.setKi(float(data[9]["value"]))
                PID3.setKd(float(data[10]["value"]))
                os.remove("updatedDB.txt")
            else:
                print("I am checking again in 5 seconds")
                endTime = time.time() +5
                i = i + 1
            if i > 0:
                break
        

            
  
if __name__ == "__main__": 
    PIDA = PID(3,0.05,0.04)
    PIDD = PID(0.2,0.0,0.01)
    PID3 = PID(0.0,0.0,0.0)
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