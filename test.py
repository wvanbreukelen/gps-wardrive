from gpslib import *

startGPS()

while True:
	status = isGPSRunning()

	print status

	time.sleep(0.5)
