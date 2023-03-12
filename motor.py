import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

# Motor A pins
enA = 12
in1 = 16
in2 = 18

# Motor B pins
enB = 22
in3 = 11
in4 = 13

# Set up GPIO pins as output
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# Set PWM frequency
pwmA = GPIO.PWM(enA, 100)
pwmB = GPIO.PWM(enB, 100)

# Set initial duty cycle to 0%
pwmA.start(0)
pwmB.start(0)

# Move motor forward
def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwmA.ChangeDutyCycle(50)
    pwmB.ChangeDutyCycle(50)

# Move motor backward
def backward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    pwmA.ChangeDutyCycle(50)
    pwmB.ChangeDutyCycle(50)

# Stop motor
def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)

# Move motor forward for 1 second, then stop
forward()
print('forward')
time.sleep(1)
stop()

# Move motor backward for 1 second, then stop
backward()
print('backward')
time.sleep(1)
stop()

# Clean up GPIO pins
GPIO.cleanup()