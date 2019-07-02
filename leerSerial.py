import serial
import time

arduino=serial.Serial('/dev/ttyUSB0',9600, timeout = 3.0)
print('conectado')

while True:
	while arduino.inWaiting() > 0:
		sig = arduino.readline()
		print(sig)
arduino.close()