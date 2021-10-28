import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM5', 9600)

def swipRight():
    ser.write(b'H') 

def swipeLeft():
   ser.write(b'A')
    
time.sleep(2) # wait for the serial connection to initialize