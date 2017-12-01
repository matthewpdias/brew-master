#!/usr/bin/env bash
#sudo modprobe w1-gpio
#sudo modprobe w1-therm
export FLASK_APP=app.py && flask run --host=0.0.0.0
