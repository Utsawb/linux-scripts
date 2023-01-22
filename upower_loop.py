import os
from time import sleep

while True:
    os.system("upower -i /org/freedesktop/UPower/devices/battery_BAT0")
    sleep(1.0)
