import sqlite3 as sql
import sys
import os.path

file = 'wardrive.db'

con = sql.connect(file)

cur = con.cursor()

if os.path.exists(file):
	try:
		cur.execute("DROP TABLE gpslog")
	except sql.Error, e:
		print "No gpslog table found!";

cur.execute("CREATE TABLE gpslog(id INTEGER PRIMARY KEY, longitude TEXT, latitude TEXT, climb TEXT, time TEXT, date TEXT)")

print "Created new database!"
