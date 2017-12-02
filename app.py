from flask import Flask, render_template
import datetime
import subprocess
import os
import filelock
import time

app = Flask(__name__)


#os.getenv('POLL_INTERVAL', 5)

#def kick_off_writes():
#    subprocess.


def get_temps():
    temps = []
    #grab the last ten lines off of the log
    string = subprocess.check_output('tail -n 10 /home/pi/Documents/brew-master/data.log', shell=True).decode('utf-8')
    pairs = string.split("\n")
    for pair in pairs:
        if pair:
            value = pair.split(',')
            temps.append({'timestamp' : value[0], 'temp' : value[1]})
    return temps


@app.route('/')
def home():
  return render_template('index.html', temps=get_temps(), interval=os.getenv('POLL_INTERVAL', 5))
