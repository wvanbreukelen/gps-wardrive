import sys
import time
import os
import sqlite3 as sql
import simplekml

FILE_LOCATION      = "/home/pi/gps-wardrive/wardrive.db"

# Check for file existance
if not os.path.exists(FILE_LOCATION):
	print "File " + str(FILE_LOCATION) + " does not exists!"

con = sql.connect(FILE_LOCATION)
cur = con.cursor()

cur.execute("SELECT * FROM network WHERE encryption = 'wpa2' GROUP BY ssid")

kml = simplekml.Kml()

while True:

	row = cur.fetchone()

	if row == None:
		print "No more entries left, done!"
		break;

	print "Logging entry..."

	print "Lat: " + str(row[3]) + " Long: " + str(row[4]) + " Encryption: " + str(row[2])

	pnt = kml.newpoint(name=row[1], coords=[(str(row[3]), str(row[4]))])

	if str(row[2]) == "wpa2":
		pnt.style.iconstyle.color = simplekml.Color.green
	elif str(row[2]) == "wep":
		pnt.style.iconstyle.color = simplekml.Color.orange
	elif str(row[2]) == "none":
		pnt.style.iconstyle.color = simplekml.Color.red
	else:
		print "Error in processing result, unknown encryption type: " + str(row[2])


kml.save("test.kml")
