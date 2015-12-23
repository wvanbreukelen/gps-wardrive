sleep 5
sudo rm -f /home/pi/final_log.txt
sudo pkill python
sudo pkill gps
sudo pkill iw
sudo ifconfig wlan0 up
echo Starting gpsd deamon...
sudo pkill -9 gpsd
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
echo Started gpsd deamon!
echo Starting gps-wardrive...
sudo pkill -9 python
#sudo python /home/pi/gps-wardrive/prepareDB.py
sudo python /home/pi/gps-wardrive/wardrive.py > /home/pi/final_log.txt 2>&1 &
echo Succesfully started gps-wardrive!
