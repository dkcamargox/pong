import serial
import io
ser = serial.Serial('COM6', 9600)
while True:
     cc=str(ser.readline())
     print(cc[2:][:-5])
