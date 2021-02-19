import serial
import time 

class arduinoSerial:
    def __init__(self, usbPort):
        self.ser = serial.Serial(usbPort, 9600)
        time.sleep(10)
        self.ser.write(b'2')

    def updatePWM(self, updatePWMvalue):
        bytePWMvalue = bytearray(updatePWMvalue, "ASCII")
        self.ser.write(bytePWMvalue)