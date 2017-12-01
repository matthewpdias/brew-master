from flask import Flask, render_template
from flask_script import Manager, Server
from flask_pymongo import PyMongo
import datetime
import threading

class MyServer(Server):
  def __call__(self, app, *args, **kwargs):
    poll_and_insert_temps()
    return Server.__call__(self, app, *args, **kwargs)

app = Flask(__name__)
manager = Manager(app)
mongo = PyMongo(app)

manager.add_command('runserver', MyServer())


if __name__ == "__main__":
  manager.run()

@app.route('/')
def home():
  ##poll the sensor and write the value to mongo
  s = ""
  with open('/sys/bus/w1/devices/28-0516a4123aff/w1_slave') as f:
     s = f.read().split("\n")[1].split(" ")[9].split("=")[1]
  temp = int(s)/1000.0*9.0/5.0+32
  timestamp = datetime.datetime.utcnow()
  temperature = {'timestamp': timestamp, 'temp': temp}
 
  print("inserting into db:")
  print(temperature)
  mongo.db.temperature.insert_one(temperature)

  ##get values to output
  print("reading from db:")

  temps = mongo.db.teperature.find( {} ).limit(10)
  for entry in temps:
    

  print(temps)

  return render_template('index.html', temps=temps)

