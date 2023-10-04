import RPii.GPIO as GPIO

import time

GPIO.Setmode(GPIO.BOARD)

GPIO.Setup(3,GPIO.OUT)

while true:
    GPIO.output(3,true)
    time.Sleep(1)
    GPIO.output(3,False)
    time.sleep(1)