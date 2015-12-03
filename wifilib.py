#!/usr/bin/env python


# Import the required libraries
import os
import sys
import time
import threading
from wifi import Cell, Scheme
from wifi.exceptions import InterfaceError

# The wifi interface
interface = 'wlan0'

# The latest scanned networks
latestNetworks = None

# Wifi library

class WifiPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.running = True

	def run(self):
		global latestNetworks
		global wifip

		hotfix = False
		while self.running:

			try:
				latest = None

				try:
					latest = scanForNetworks()

					hotfix = False
				except (InterfaceError):
					print "[ERROR] Cannot find new networks right now, trying to make it work..."
					if hotfix == False:
						print "Doing the hotfix..."
						os.system("sudo ifconfig wlan0 up")
						time.sleep(2)
						hotfix = True
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
	# Constants
	encWPA2 = 0
	encWPA = 0
	encWEP = 0
	encNone = 0

	if networks == None:
		return;

	for network in networks:
		encryption = getEncryptionType(network)

		print encryption

		if encryption == "wpa2":
			encWPA2 = encWPA2 + 1
		elif encryption == "wpa":
			encWPA = encWPA + 1
		elif encryption == "wep":
			encWEP = encWEP + 1
		elif encryption == "none":
			encNone = encNone + 1
		else:
			print "Encryption type cannot been resolved, type of: ", encryption

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
