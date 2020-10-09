#!/usr/bin/python
# music starts on turning on an external switch
# https://yura2.hateblo.jp/archive/2016/02/14
# needs a 10 kOhm resistor

import RPi.GPIO as GPIO
import time

PIN=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    pin_status = GPIO.input(PIN)
    print(pin_status)
    time.sleep(0.1)

GPIO.cleanup()
