from gpslib import *
from wifilib import *
import sqlite3 as sql
import sys
import os

# Check if python has root permissions
if os.getuid() != 0:
	print("Please run as root!")
	sys.exit(1)

# Start the GPS logger
startGPS()
print "Starting wifi... This process can take a couple of seconds"
startWifi()

while True:
	if isWifiRunning():
		break;
	time.sleep(0.5)

print "[SUCCESS] Started wifi!"

print "Waiting for GPS fix..."

# Wait until a new GPS fix has displayed
while True:
	status = isGPSRunning()

	if status == True:
		break;

	time.sleep(0.5)

# Print out some basic info
print "[SUCCESS] GPS fix successfully found!"

print "Longitude: ", getLongitude()
print "Latitude: ", getLatitude()

# Try to create a sqlite DB connection
try:
	con = sql.connect('wardrive.db')

	cur = con.cursor()
except sql.Error, e:
	print "[ERROR] Error creating DB conn %s:" % e.args[0]
	sys.exit(1)

latestSSIDs = []

# Start to log the GPS information to a database
while True:
	lon = str(getLongitude())
	lat = str(getLatitude())
	climb = str(getHeight())
	curdate = str(time.strftime("%x"))
	curtime = str(time.strftime("%X"))

	# Get Wifi stuff
	wifistuff = getLatestPolledNetworks()
	encryptions = countEncryptionTypes(wifistuff)
	amount = len(wifistuff)

	# id INTEGER PRIMARY KEY, longitude TEXT, latitude TEXT, climb TEXT, time TEXT, date TEXT)
	statement1 = "INSERT INTO gpslog VALUES (NULL, " + lon + ", " + lat + ", " + climb + ", '" + curtime + "', '" + curdate + "')"
	try:
		cur.execute(statement1)
	except (OperationalError):
		print "[WARNING] Cannot log gps instance!"

	for network in wifistuff:
		if network.ssid in latestSSIDs:
			amount = amount - 1
		else:
			networkType = getEncryptionType(network)
			latestSSIDs.append(network.ssid)

			# id INTEGER PRIMARY KEY, ssid TEXT, encryption TEXT, longitude TEXT, latitude TEXT, time TEXT, date TEXT)
			statement2 = "INSERT INTO network VALUES (NULL, '" + network.ssid + "', '" + networkType + "', '" + lon + "', '" + lat + "', '" + curtime + "', '" + curdate + "')"
			cur.execute(statement2)

	print "Received " + str(amount) + " wifi points!"

	con.commit()
	time.sleep(5)
