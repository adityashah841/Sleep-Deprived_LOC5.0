import Adafruit_DHT as adht
import time
import requests

sensor = adht.DHT22
pin = 24

while True:
    humidity, temperature = adht.read_retry(sensor, pin)
    temp_f = (temperature * (9 / 5)) + 32
    
    url = f'https://c730-2402-3a80-4166-a8c5-69c2-2f77-8b6-e502.in.ngrok.io/ml/ml_ac/{temp_f}/{humidity}'
    response = requests.get(url)
    print(response.status_code)
   
    if response.status_code!=200:
        break
    if humidity is not None and temperature is not None:
        print(f'Temperature, Humidity: {temperature}, {humidity}')
    else:
        print('Failed')
    time.sleep(1)