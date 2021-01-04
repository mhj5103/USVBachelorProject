
import threading 
import time

def control_loop(num): 
    n = 5
    while True:
        n += 1
        print(n)
        if n > 100:
            break
        time.sleep(2)
  
def update_db_loop(num): 
    n = 5
    while True:
        n -= 1
        print(n)
        if n < -100:
            break
        time.sleep(2)
  
if __name__ == "__main__": 

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