from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from keras.models import load_model
import pandas as pd
import cv2
from PIL import Image
from io import BytesIO
import numpy as np
import time
from flask import make_response

# Number of people in image
num = None

# Load the pre-trained Haar cascade classifier for human body detection
human_cascade = cv2.CascadeClassifier('D:/Vijay/DJSCE/LOC_Hackathon/backend/ml/haarcascade_fullbody.xml')

# Load the HOG pre-trained people detection model
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Create your views here.
@api_view(["GET"])
def test_ml_ac(request, temp, hum):
    # temp = request.data.get('temp')
    # hum = request.data.get('hum')
    temp = float(temp)
    hum = float(hum)
    model = load_model("D:/Vijay/DJSCE/LOC_Hackathon/backend/ml/AC_pred.h5")
    d = {
        'temp': [temp],
        'hum': [hum],
    }
    df = pd.DataFrame(d)
    temp_pred = model.predict(df)[0][0]
    print(temp_pred)
    data = {'temp_pred': f'{temp_pred}'}
    return JsonResponse(data, status=status.HTTP_200_OK)

@api_view(["GET"])
def test_ml_geyser(request, temp):
    temp = float(temp)
    model = load_model("D:/Vijay/DJSCE/LOC_Hackathon/backend/ml/Geyser_pred.h5")
    d = {
        "temp": [temp],
    }
    df = pd.DataFrame(d)
    temp_pred = model.predict(df)[0][0]
    print(temp_pred)
    return JsonResponse({'temp_pred': f'{temp_pred}'}, status=status.HTTP_200_OK) 

@csrf_exempt
def test_cv(request):
    global num
    #cap = cv2.VideoCapture(0)

    # Open the video capture device (webcam)
    #cap = cv2.VideoCapture(0)

    #while True:
    # Read a frame from the video capture device
    #ret, frame = cap.read()

    if request.method == "GET":
        # image_data = request.body
        url = "https://192.168.117.57:8080/video"
        cap = cv2.VideoCapture(url)
        ret, frame = cap.read()
        # image = Image.open(BytesIO(image_data))
        # print(type(image))
        # cv2.imshow('frame', np.array(image))
        # cv2.imwrite('output_old.jpg', np.array(image))
        cv2.imwrite('output_old.jpg', frame)

        # Load the input image
        image = cv2.imread('output_old.jpg')

        # Resize the image to improve detection performance
        image = cv2.resize(image, (640, 480))

        # Perform people detection
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        # Draw the detected bounding boxes on the image
        for (x, y, w, h) in rects:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the image with the detected bounding boxes
        cv2.imshow('Detected People', image)
        num = len(rects)
        # Print the number of detected people
        print('Number of People:', len(rects))

        # cv2.waitKey(0)
        cv2.destroyAllWindows()


        # time.sleep(10)
        # Convert the frame to grayscale
        # gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

        # Detect human bodies in the grayscale frame using the Haar cascade classifier
        # humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw a rectangle around each detected human body
        #for (x, y, w, h) in humans:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #. Display the frame with the human bodies detected
        #cv2.imshow('frame', frame)

        # Count the number of humans detected
        # num_humans = len(humans)
        # print('Number of humans:', num_humans)

        # Wait for a key press
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #   break

    # Release the video capture device and close all windows
    #cap.release()
        # cv2.destroyAllWindows()
        return JsonResponse({'success': 'Success'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Error'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def test_cv_get(request):
    if request.method == 'GET':
        return JsonResponse({"num": f"{num}"})

time_light = 0
time_motor = 0

@csrf_exempt
def test_time_sum_light(request, time):
    if request.method == "GET":
        time_light = ((0.06) * float(time)) / 3600
        print(float(time) / 3600)
        print()

@csrf_exempt
def test_time_sum_motor(request, time1, time2):
    if request.method == "GET":
        time_motor = ((time1 + time2) * 0.09) / 3600
        print(float(time1) / 3600)
        print(float(time2) / 3600)
        print()

@api_view(["GET"])
def dashboard(request): 
     return JsonResponse({"time_light": f"{time_light}","time_motor": f"{time_motor}"})