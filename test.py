from gpslib import *

startGPS()

print "Waiting for GPS fix..."

while True:
	status = isGPSRunning()

	if status == True:
		break;

	time.sleep(0.5)

print "GPS fix successfully found!"
print "Longitude: ", getLongitude()
print "Latitude: ", getLatitude()
print "Height in meters: ", getHeight()

print "Waiting for WiFi connection..."

while True:
	# Check if there is a WiFi connection, if so, break
	time.sleep(0.5)
