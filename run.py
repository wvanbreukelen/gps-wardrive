#!/usr/bin/env python

import os
import sys
import time
import threading
from wifi import Cell, Scheme
from wifi.exceptions import InterfaceError

# The wifi interface
interface = 'wlan0'

latestNetworks = None

class WifiPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.running = True

	def run(self):
		global latestNetworks
		while self.running:
			try:
				latest = None
				try:
					latest = scanForNetworks()
				except (InterfaceError):
					print "[ERROR] Cannot find new networks right now, try again next time..."
				latestNetworks = latest
			except (KeyboardInterrupt, SystemExit):
				self.running = False
				self.join()

			time.sleep(0.3)

def startWifi():
	wifip = WifiPoller()
	wifip.start()

def isWifiRunning():
	if latestNetworks == None:
		return False
	return True

# Get the latest scanned wifi networks
def getLatestPolledNetworks():
	return latestNetworks

# Scan for wireless networks
def scanForNetworks():
	return Cell.all(interface)

# Scan all wireless networks for their encryption type
def scanEncryption():
	cells = scanForNetworks()

	return countEncryptionTypes(cells)

def countEncryptionTypes(networks):
	# Variables
	encWPA2 = 0
	encWPA = 0
	encWEP = 0
	encNone = 0

	for network in networks:
		encryption = getEncryptionType(network)

		if encryption == "wpa2":
			encWPA2 = encWPA2 + 1
		elif encryption == "wpa":
			encWPA = encWPA + 1
		elif encryption == "wep":
			encWEP = encWEP + 1
		elif encryption == Null:
			encNone = encNone + 1
		else:
			print "Encryption type cannot been resolved, type of ", encryption

	return [encWPA2, encWPA, encWEP, encNone]

# Get the encryption type of a wireless network
def getEncryptionType(network):
	if network.encrypted:
		return network.encryption_type
	else:
		return None

# Get the SSID of a network
def getSSID(network):
	return network.ssid;
