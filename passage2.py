import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_pin=4

GPIO.setup(PIR_pin,GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
#GPIO.output(17, GPIO.HIGH)
#time.sleep(2)
#GPIO.cleanup(17)
#time.sleep(2)
try:
    #GPIO.output(17, GPIO.HIGH)
    #time.sleep(5)
    #GPIO.output(17, GPIO.LOW)
    print('ready')
    sum_=0
    t1=t2=0
    while True:
        GPIO.setup(17, GPIO.OUT)
        if GPIO.input(PIR_pin):
            GPIO.output(17, GPIO.HIGH)
            t1 = time.time()
            print('motion Detected')
            time.sleep(15)
        else:
            #GPIO.setup(17, GPIO.OUT)
            t2 = time.time()
            td = t2-t1
            if td>0 and t1!=0:
                sum_+=td
            GPIO.cleanup(17)
            #GPIO.setup(17, GPIO.OUT)
            print("motion stopped")
            time.sleep(1)
        time.sleep(0.1)
except KeyboardInterrupt:
    url = f'https://591c-2402-3a80-138e-3664-fc45-ab4c-9faf-6608.in.ngrok.io/ml/ml_light_time/{sum_}'
    response = requests.get(url)
    print(response.status_code)
   
    if response.status_code!=200:
        break
    print('Quit')
    GPIO.cleanup()
