import serial
import time
from pyautogui import press

#arduino serial setup. Get COM from arduino IDE
arduinoSerialData = serial.Serial('COM5', 9600)

while True:
    #get Arduino data
    arduinoString = arduinoSerialData.readline()
    string_n = arduinoString.decode()
    FSR = int(string_n)
    
    #Open right hand to press a
    if FSR < 10:
        key = press('a')
        
        

