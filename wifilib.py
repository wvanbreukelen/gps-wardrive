#!/usr/bin/env python

import os
import sys
from wifi import Cell, Scheme

# The wifi interface
interface = 'wlan0'

# Check if python has root permissions
if os.getuid() != 0:
	print("Please run as root!")
	sys.exit(1)

# Scan for wireless networks
def scanForNetworks():
	return Cell.all(interface)

# Scan all wireless networks for their encryption type
def scanEncryption():
	# Variables
	encWPA2 = 0
	encWPA = 0
	encWEP = 0
	encNone = 0

	cells = scanForNetworks()

	for network in cells:
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

	return (encWPA2, encWPA, encWEP, encNone)

# Get the encryption type of a wireless network
def getEncryptionType(network):
	if network.encrypted:
		return network.encryption_type
	else:
		return None

# Get the SSID of a network
def getSSID(network):
	return network.ssid;
