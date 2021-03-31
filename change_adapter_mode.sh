#!/bin/bash
sudo ifconfig wlan0 down
echo "down wlan0"
sudo iwconfig wlan0 mode monitor
echo "change wlan0 mode to monitor"
sudo ifconfig wlan0 up
echo "up wlan0"

