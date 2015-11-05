import os
import time
import sys
from gps import *
from gpspoller import GpsPoller
import threading

# Setting empty variables before polling for GPS data!
gpsd     = None
long     = None
lat      = None


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
		global gpsd, long, lat
		looping = True
		while gpsp.running:
			try:
				gpsd.next()
				long = gpsd.fix.latitude
				lat = gpsd.fix.longitude
		        except (KeyboardInterrupt, SystemExit):
				print "Pressed! 1"
                		gpsp.running = False


# Main action
if __name__ == "__main__":
	gpsp = GpsPoller()
	gpsp.start()

# Check if the GPS module is running properly
def isGPSRunning():
	# Check for GPS status
        if str(lat) == "nan" or lat == 0.0:
       		return False
       	else:
             	return True		


# Get the latest longitude
def getLongitude():
	return long

# Get the latest latitude
def getLatitude():
	return lat
