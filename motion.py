import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_pin=4

GPIO.setup(PIR_pin,GPIO.IN)
try:
    time.sleep(2)
    print('ready')
    while True:
        if GPIO.input(PIR_pin):
            print('motion Detected')
            time.sleep(1)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Quit')
    GPIO.cleanup()