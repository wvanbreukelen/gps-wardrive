from gpsstatus import getStatus
import time

while True:
	status = getStatus()

	print status

	time.sleep(0.5)
