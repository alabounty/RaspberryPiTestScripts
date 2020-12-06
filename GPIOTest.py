#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

#change your channel to whatever GPIO pin you want to test
channel = 8
GPIO.setmode(GPIO.BCM)  
# Setup your channel
GPIO.setup(channel, GPIO.IN)

# To test the value of a pin use the .input method
# Loops through a few times so you can see if it changes
try:
    i=1
    while (i<=30):
        channel_is_on = GPIO.input(channel)  # Returns 0 if OFF or 1 if ON
        print (channel_is_on)
        sleep(.5)
        i += 1

# clean up
finally:
    GPIO.cleanup()         
