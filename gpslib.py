import os
import time
import sys
from gps import *
#from gpspoller import GpsPoller
import threading

# Setting empty variables before polling for GPS data!
gpsd      = None
long      = None # Location longitude
lat       = None # Location latitude
climb     = None # Climb height in meters
speed     = None # Speed in mp/h (need to convert to km/h, multiply with 1.6??!)


isRunning = False


# The actual GPS poller, polls the GPS module for new data
class GpsPoller(threading.Thread):
	global status
	global watching

	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd
		gpsd = gps(mode=WATCH_ENABLE)
		self.current_value = None
		self.running = True

	def run(self):
		global gpsd, long, lat, climb
		#looping = True
		while gpsp.running:
			gpsd.next()
			lat = gpsd.fix.latitude
			long = gpsd.fix.longitude
			climb = gpsd.fix.climb


# Main action
if __name__ == "__main__":
	print "Hello"
	gpsp = GpsPoller()
	gpsp.start()

	while True:
		print "Latitude: ", gpsd.fix.latitude
                print "Longitude: ", gpsd.fix.longitude


# Check if the GPS module is running properly
def isGPSRunning():
	# Check for GPS status
        if str(lat) == "nan" or lat == 0.0 or lat == None:
       		return False
       	else:
             	return True


# Get the latest longitude
def getLongitude():
	return long

# Get the latest latitude
def getLatitude():
	return lat

# Get the current height in meters (m)
def getHeight():
	return climb

# Start by getting data from the GPS module
def startGPS():
	global isRunning, gpsp
	if isRunning == False:
		try:
			# Start up the GPS poller
			gpsp = GpsPoller()
			gpsp.start()
		except (socket.error):
			print "Cannot start GPS! Please run gpsp!"
			print "Stacktrace: ", traceback.format_exc()
			sys.exit(1)

		isRunning == True
