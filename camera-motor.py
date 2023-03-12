import RPi.GPIO as GPIO
import time

import requests
import io
import picamera

# Set the proportional gain for the feedback loop
kp = 0.1
SEQ = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]
# Initialize the current speed and error
current_speed = 0
error = 0
#delay = 0.005
# Capture an image from the Raspberry Pi camera
def step_motor(delay, steps):
    for i in range(steps):
        for j in range(8):
            GPIO.output(IN1, SEQ[j][0])
            GPIO.output(IN2, SEQ[j][1])
            GPIO.output(IN3, SEQ[j][2])
            GPIO.output(IN4, SEQ[j][3])
            time.sleep(delay)
stream = io.BytesIO()
delay = 0.005
steps = 512
while True:
    camera = picamera.PiCamera()
    camera.capture(stream, format='jpeg')
    image_binary = stream.getvalue()


    # Send the image data in a POST request to the API endpoint
    url = 'https://c730-2402-3a80-4166-a8c5-69c2-2f77-8b6-e502.in.ngrok.io/ml/ml_cv/'
    #headers = {'Content-Type': 'image/jpeg'}

    #response = requests.post(url, headers=headers, data=image_binary)
    response = requests.get(url)
    print(response.status_code)
    #camera.close()
    if response.status_code!=200:
        break
    
    import requests

    response = requests.get('https://c730-2402-3a80-4166-a8c5-69c2-2f77-8b6-e502.in.ngrok.io/ml/ml_cv_get')
    json_response = response.json()

    # Access the data from the JSON response
    num = int(json_response['num'])
    print(num)

    #num = response.data

    # Define GPIO pins for the stepper motor
    IN1 = 17
    IN2 = 18
    IN3 = 27
    IN4 = 22

    # Set up the GPIO pins for the stepper motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


    # Set the desired speed of the motor (in steps per second)
    #desired_speed_1 = 50
    #desired_speed_3 = 150
    #if num<3:
    #    desired_speed=desired_speed_1
    #else:
    #    desired_speed=desired_speed_3



    # Perform image processing to determine the desired speed
    # (e.g. calculate the average brightness of the frame)
    # ...



    # Adjust the speed of the motor based on the error
    if num >= 0 and num < 1:
        # Increase the speed by turning on the appropriate GPIO pins
        #GPIO.output(IN1, GPIO.HIGH)
        #GPIO.output(IN2, GPIO.LOW)
        #GPIO.output(IN3, GPIO.LOW)
        #GPIO.output(IN4, GPIO.HIGH)
        delay = 0.01   # set delay time for stepping
        steps = 256    # set number of steps for one revolution
        step_motor(delay, steps)
        #time.sleep(0.5) # wait for half second
        #try:
        #    time.sleep(1/(current_speed*kp))
        #    current_speed += 1
        #except:
        #    pass
    elif num >= 1:
        # Decrease the speed by turning on the appropriate GPIO pins
        #GPIO.output(IN1, GPIO.LOW)
        #GPIO.output(IN2, GPIO.HIGH)
        #GPIO.output(IN3, GPIO.HIGH)
        #GPIO.output(IN4, GPIO.LOW)
        delay = 0.0013   # set delay time for stepping
        steps = 600    # set number of steps for one revolution
        step_motor(delay, steps)
        #time.sleep(0.5) # wait for half second
        #try:
        #    time.sleep(1/(current_speed*kp))
        #    current_speed -= 1
        #except:
        #    pass
    # Wait for a short period before processing the next frame
    time.sleep(0.01)
    GPIO.cleanup()
    camera.close()
