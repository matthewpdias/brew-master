from flask import Flask, render_template
import datetime
import subprocess
import os
import filelock
import time

#make sure not to try and read while writing!
lock = filelock.FileLock("/home/pi/Documents/brew-masterlockfile.lock")
lock.timeout = 5

#kick off the temperature polling
subprocess.Popen('python3 /home/pi/Documents/brew-master/log_temp.py', shell=True)

app = Flask(__name__)

#grab the last ten lines off of the log
def get_temps():
    temps = []

    #lock filelock
    with lock:
        string = subprocess.check_output('tail -n 10 /home/pi/Documents/brew-master/data.log', shell=True).decode('utf-8')
    #unlock filelock

    pairs = string.split("\n")
    for pair in pairs:
        if pair:
            value = pair.split(',')
            temps.append({'timestamp' : value[0], 'temp' : value[1]})
    return temps

#the index page, I didn't feel like adding any others
@app.route('/')
def home():
  return render_template('index.html', temps=get_temps(), interval=os.getenv('POLL_INTERVAL', 5))
