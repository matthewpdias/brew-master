import os
import datetime
import filelock

def insert_temp():
    s = ""
    #pull a data point off of the device
    with open('/sys/bus/w1/devices/28-0516a4123aff/w1_slave') as f:
       s = f.read().split("\n")[1].split(" ")[9].split("=")[1]
    temp = int(s)/1000.0*9.0/5.0+32
    timestamp = datetime.datetime.utcnow()
    string = str(timestamp) + "," + str(temp) + "\n"

    #write the values to the logfile!
    with open('/home/pi/Documents/brew-master/data.log', 'a') as f:
        f.write(string)
