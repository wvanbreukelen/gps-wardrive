from gpslib import *
import sqlite3 as sql
import sys

# Start the GPS logger
startGPS()

print "Waiting for GPS fix..."

# Wait until a new GPS fix has displayed
while True:
	status = isGPSRunning()

	if status == True:
		break;

	time.sleep(0.5)

# Print out some basic info
print "GPS fix successfully found!"
print "Longitude: ", getLongitude()
print "Latitude: ", getLatitude()
print "Height in meters: ", getHeight()

# Try to create a sqlite DB connection
try:
	con = sql.connect('wardrive.db')

	cur = con.cursor()
except sql.Error, e:
	print "Error creating DB conn %s:" % e.args[0]
	sys.exit(1)

# Start to log the GPS information to a XML file
while True:
	lon = str(getLongitude())
	lat = str(getLatitude())
	climb = str(getHeight())
	curdate = str(time.strftime("%x"))
	curtime = str(time.strftime("%X"))

	statement = "INSERT INTO gpslog VALUES (NULL, " + lon + ", " + lat + ", " + climb +", '" + curtime + "', '" + curdate + "')"
	cur.execute(statement)
	con.commit()
	print "Logged to DB!"

	time.sleep(5)

#print "Waiting for WiFi connection..."

#while True:
	# Check if there is a WiFi connection, if so, break
	#time.sleep(0.5)
