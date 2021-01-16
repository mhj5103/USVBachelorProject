from PID import PID
import threading 
import time
import math
import os.path
import os
from pysondb import db
import json 
XCoord = 0
YCoord = 0
Angle = 0.5*math.pi
DistanceToTarget = 5
DistanceToTargetY = 0.1
a=db.getDb("db.json")
def control_loop(num): 
    n = 0
    startTime = time.time()
    while 1 > 0:
        
        if(time.time() > startTime):
            startTime += 0.25
            print("Im updating current coordinates and calculating angles + distances")
            print("We are on iteration:", n)
            print("First PID value is: ", PID1.regulator(Angle))
            print("Second PID value is: ", PID2.regulator(DistanceToTarget))
            print("Third PID value is: ", PID3.regulator(DistanceToTargetY))
            n += 1
            if(n > 120):
                break

  
def update_db_loop(num): 
    endTime = time.time() + 5
    while 1 > 0:       
        if(time.time()> endTime):
            if os.path.isfile('updatedDB.txt'):
                print("I am updating all values")
                data = a.getAll()
                for x in data:
                    print(x)
                XCoord = data[0]["value"]
                YCoord = data[1]["value"]
                PID1.setKp(float(data[2]["value"]))
                PID1.setKi(float(data[3]["value"]))
                PID1.setKd(float(data[4]["value"]))
                PID2.setKp(float(data[5]["value"]))
                PID2.setKi(float(data[6]["value"]))
                PID2.setKd(float(data[7]["value"]))
                PID3.setKp(float(data[8]["value"]))
                PID3.setKi(float(data[9]["value"]))
                PID3.setKd(float(data[10]["value"]))
                os.remove("updatedDB.txt")
            else:
                print("I am checking again in 5 seconds")
                endTime = time.time() +5
        

            
  
if __name__ == "__main__": 
    PID1 = PID(0.0,0.0,0.0)
    PID2 = PID(0.0,0.0,0.0)
    PID3 = PID(0.0,0.0,0.0)
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