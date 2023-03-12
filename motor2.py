import RPi.GPIO as GPIO
import time

# Define GPIO pins for ULN2003
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# Define sequence for stepping the motor
# Use half-step sequence (8 steps per revolution)
SEQ = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

# Define function for stepping the motor
def step_motor(delay, steps):
    for i in range(steps):
        for j in range(8):
            GPIO.output(IN1, SEQ[j][0])
            GPIO.output(IN2, SEQ[j][1])
            GPIO.output(IN3, SEQ[j][2])
            GPIO.output(IN4, SEQ[j][3])
            time.sleep(delay)

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Move motor
try:
    while True:
        delay = 0.001   # set delay time for stepping
        steps = 5000     # set number of steps for one revolution
        step_motor(delay, steps)
        #time.sleep(0.5) # wait for half second
except KeyboardInterrupt:
    GPIO.cleanup()
