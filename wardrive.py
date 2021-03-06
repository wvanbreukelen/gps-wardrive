from gpslib import *
from wifilib import *
import sqlite3 as sql
import sys
import os
import traceback

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
	con = sql.connect('/home/pi/gps-wardrive/wardrive.db')

	cur = con.cursor()
except sql.Error, e:
	print "[ERROR] Error creating DB conn %s:" % e.args[0]
	print "Stacktrace: ", traceback.format_exc()
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

	try:
		if wifistuff is not None:
			
			amount = len(wifistuff)

			# id INTEGER PRIMARY KEY, longitude TEXT, latitude TEXT, climb TEXT, time TEXT, date TEXT)
			statement1 = "INSERT INTO gpslog VALUES (NULL, " + lon + ", " + lat + ", " + climb + ", '" + curtime + "', '" + curdate + "')"

			try:
				cur.execute(statement1)
			except (sql.OperationalError):
				print "Error running statement 1!"
				print "Stacktrace: ", traceback.format_exc()
			
			for network in wifistuff:
				try:
					if network.ssid in latestSSIDs:
						amount = amount - 1
					else:
						networkType = getEncryptionType(network)
						latestSSIDs.append(network.ssid)

						# id INTEGER PRIMARY KEY, ssid TEXT, encryption TEXT, longitude TEXT, latitude TEXT, time TEXT, date TEXT)
						statement2 = "INSERT INTO network VALUES (NULL, '" + network.ssid + "', '" + networkType + "', '" + lon + "', '" + lat + "', '" + curtime + "', '" + curdate + "')"
						try:
							cur.execute(statement2)
						except (sql.OperationalError):
							print "Exception was thrown during sqlite statement!"
				except (AttributeError):
					print "[WARNING] Cannot grab wifi SSID attribute!"
					#print network.ssid
					print "Stacktrace: ", traceback.format_exc()
					#os.system("sudo bash /home/pi/gps-wardrive/gps-wardrive.sh")

			print "Received " + str(amount) + " wifi points!"

			con.commit()

			time.sleep(5)
	except TypeError:
		print "[ERROR] Wifi array is empty, try again next time..."
		print "Stacktrace: ", traceback.format_exc() 
