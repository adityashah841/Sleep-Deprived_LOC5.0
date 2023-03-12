import Adafruit_DHT as adht
import time

sensor = adht.DHT22
pin = 4

while True:
    humidity, temperature = adht.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature, Humidity: {temperature}, {humidity}')
    else:
        print('Failed')
    time.sleep(1)