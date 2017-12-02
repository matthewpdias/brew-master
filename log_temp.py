import os
import datetime
import filelock
import time

#make sure not to try and read while writing!
lock = filelock.FileLock("/home/pi/Documents/brew-master/lockfile.lock")
lock.timeout = 5

#write temperature and time to the log, and return the temp to the main loop
def insert_temp():
    s = ""
    #pull a data point off of the device
    with open('/sys/bus/w1/devices/28-0516a4123aff/w1_slave') as f:
       s = f.read().split("\n")[1].split(" ")[9].split("=")[1]
    temp = int(s)/1000.0*9.0/5.0+32
    timestamp = datetime.datetime.utcnow()
    string = str(timestamp) + "," + str(temp) + "\n"

    #write the values to the logfile!

    #lock filelock
    with lock:
        with open('/home/pi/Documents/brew-master/data.log', 'a') as f:
            f.write(string)
    #unlock filelock
    return temp

#main loop, execute forever!
while True:
    temp = insert_temp()
    if temp > os.getenv('MAX_TEMPERATURE', 75):
        #send email TOO HOT!
        print("TOO HOT!")
    elif temp < os.getenv('MIN_TEMPERATURE', 55):
        #send email TOO COLD!
        print("TOO COLD!")
    else:
        pass
    time.sleep(os.getenv('POLL_INTERVAL', 5))
