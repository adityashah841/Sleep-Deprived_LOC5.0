import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor


try:
    while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(4, GPIO.IN)
        pir = MotionSensor(4)
        pir.wait_for_motion()
        print('Motion Detected')
        GPIO.output(17, GPIO.HIGH)
        time.sleep(15)
        pir.wait_for_no_motion()
        print('Motion Stopped')
        GPIO.cleanup()
#         GPIO.output(17, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()