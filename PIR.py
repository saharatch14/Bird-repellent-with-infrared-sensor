#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys, string, os
import requests
import RPi.GPIO as GPIO
import time
import datetime

# LINE notify
url = 'https://notify-api.line.me/api/notify'
token = ''
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

pir_sensor_pin = 21

GPIO.setup(pir_sensor_pin, GPIO.IN)    #Read output from PIR motion sensor

print("Starting PIR motion sensor...")

while(True):
        if(GPIO.input(pir_sensor_pin)):

                # MSG
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                msg = 'Motion Detected: ' + dt

                r = requests.post(url, headers=headers, data = {'message':msg})
                print r.text

                print msg
                os.system("./a")
                time.sleep(3)
        time.sleep(1) #loop delay

GPIO.cleanup()