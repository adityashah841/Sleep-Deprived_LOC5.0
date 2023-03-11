import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_pin=4

GPIO.setup(PIR_pin,GPIO.IN)
#GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
time.sleep(2)
GPIO.cleanup(17)
time.sleep(2)
try:
    #GPIO.output(17, GPIO.HIGH)
    #time.sleep(5)
    #GPIO.output(17, GPIO.LOW)
    print('ready')
    while True:
        GPIO.setup(17, GPIO.OUT)
        if GPIO.input(PIR_pin):
            GPIO.output(17, GPIO.HIGH)
            print('motion Detected')
            time.sleep(15)
        else:
            #GPIO.setup(17, GPIO.OUT)
            GPIO.cleanup(17)
            #GPIO.setup(17, GPIO.OUT)
            print("motion stopped")
            time.sleep(1)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Quit')
    GPIO.cleanup()
