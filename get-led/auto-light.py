--------------------import RPi.GPIO as GPIO-*****************************************************************************************************************************************************************************************************************************************************
import time
GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led, GPIO.OUT)
phototransistor=6
GPIO.setup(phototransistor, GPIO.IN)
state=1
while True:
    if GPIO.input(phototransistor):
        state=0
        GPIO.output(led, state)
        time.sleep(0.2)
    else:
        state=1
        GPIO.output(led, state)
        time.sleep(0.2)------