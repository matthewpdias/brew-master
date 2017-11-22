from flask import Flask, render_template
from flask_pymongo import PyMongo
import datetime
import threading

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def run():
  return render_template('index.html', temps=get_temp())

def get_temp():
  threading.Timer(5.0, get_temp).start()
  with file('/sys/bus/w1/devices/28-0516a4123aff/w1_slave') as f:
     s = f.read().split("\n")[1].split(" ")[9].split("=")[1]
  temp = int(s)/1000.0*9.0/5.0+32
  temp = 98.3


  timestamp = datetime.datetime.utcnow()
  
  temperature = {'timestamp' : timestamp, 'temp' : temp}
  mongo.db.temperature.insert_one(temperature)

  return temperatures