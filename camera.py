import requests
import io
import picamera

# Capture an image from the Raspberry Pi camera
camera = picamera.PiCamera()
stream = io.BytesIO()
camera.capture(stream, format='jpeg')
image_binary = stream.getvalue()

# Send the image data in a POST request to the API endpoint
url = 'https://c730-2402-3a80-4166-a8c5-69c2-2f77-8b6-e502.in.ngrok.io/ml/ml_cv/'
headers = {'Content-Type': 'image/jpeg'}
response = requests.post(url, headers=headers, data=image_binary)

print(response.status_code)
camera.close()
