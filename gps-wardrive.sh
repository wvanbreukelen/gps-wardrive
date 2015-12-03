#!/usr/bin/env
sleep 10s
sudo pkill -9 python
sudo pkill -9 iw
sudo ifconfig wlan0 up
echo Starting gpsd deamon...
sudo pkill -9 gpsd
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
echo Started gpsd deamon!
echo Starting gps-wardrive...
sudo pkill -9 python
#sudo python /home/pi/gps-wardrive/prepareDB.py
sudo python /home/pi/gps-wardrive/wardrive.py &
echo Succesfully started gps-wardrive!
