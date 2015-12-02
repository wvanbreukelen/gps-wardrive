# This exports all the data captured by gps-wardrive to a .csv file

# Import required libraries
import sys
import time
import os
import csv
import sqlite3 as sql
import traceback
from subprocess import call

FILE_LOCATION      = "/home/pi/gps-wardrive/wardrive.db"
DEST_FOLDER        = "/home/pi/gps-wardrive/results"

# Do not edit after this line!

fileDest = DEST_FOLDER + "/export_" + str(time.strftime("%X")) + ".csv"

# Check for file existance

if not os.path.exists(FILE_LOCATION):
	print "File " + str(FILE_LOCATION) + " does not exists!"

# Create instance

con = sql.connect(FILE_LOCATION)
cur = con.cursor()

# Receive data, parse to .csv

data = cur.execute("SELECT * FROM network")


print "CSV file destination: " + fileDest

if not os.path.exists(fileDest):
	print "Creating new file..."
	os.system("touch " + fileDest)

print "Writing..."

with open(fileDest, 'wb') as f:
	writer = csv.writer(f)
	#writer.writerow(['ID', 'SSID', 'ENCRYPTION', 'LAT', 'LONG', 'TIME', 'DATE'])
	for row in data:
		writer.writerow(row)

con.close()

# Save file

# All Done!
