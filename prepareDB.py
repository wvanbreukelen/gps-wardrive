import sqlite3 as sql
import sys
import os.path

file = 'wardrive.db'

con = sql.connect(file)

cur = con.cursor()

if os.path.exists(file):
	try:
		cur.execute("DROP TABLE gpslog")
		cur.execute("DROP TABLE network")
	except sql.Error, e:
		print "Not all tables have been deleted, no worry :)";

print "Creating tables..."

cur.execute("CREATE TABLE gpslog(id INTEGER PRIMARY KEY, longitude TEXT, latitude TEXT, climb TEXT, time TEXT, date TEXT)")
cur.execute("CREATE TABLE network(id INTEGER PRIMARY KEY, ssid TEXT, encryption TEXT, longitude TEXT, latitude TEXT, time TEXT, date TEXT)")

print "Successfully created tables!"
