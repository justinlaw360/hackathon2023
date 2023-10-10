import serial
import time
SerialObj = serial.Serial('COM6')

SerialObj.baudrate = 9600
SerialObj.bytesize = 8
SerialObj.parity = 'N'
SerialObj.stopbits = 1
time.sleep(3)
SerialObj.write(b'A')
SerialObj.close()