

import base64
import io
import requests
import cv2
import numpy as np

from bs4 import BeautifulSoup
from PIL import Image

search_term = 'Ravi_Teja'
num_pics = 50
domain = 'www.google.com'
path = '/search'
params = {'tbm': 'isch', 'q': search_term}
stored = 0


def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    xmlFile = '/home/saibharadwaj/PycharmProjects/DSP/FaceRecognition/training_data/lbpcascade_frontalface.xml'
    xmlFile = '/home/saibharadwaj/PycharmProjects/DSP/FaceRecognition/training_data/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(xmlFile)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if (len(faces) == 0):
        return None, None

    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h], faces[0]


while True:  # stored < num_pics:     # True
    url = 'https://' + domain + path + '?'
    for key, value in params.items():
        url += key + '=' + value.replace(' ', '+') + '&'
    print('url is', url)
    response = requests.get(url=url)
    page = BeautifulSoup(response.text, 'lxml')
    print('-' * 50)
    print('page is', page)
    print('-' * 50)

    images = page.findAll('img')
    x = 0

    for img in images:
        print('-'*50)
        print('img is', img)
        print('-'*50)
        image_bytes = requests.get(img['src']).content
        image = base64.b64encode(image_bytes)
        image = base64.b64decode(image)
        image = Image.open(io.BytesIO(image))
        print(image, type(image))
        i1 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # face, rect = detect_face(i1)
        # if face is None:
        #     cv2.imshow('No face', i1)
        # # else:
        # #     cv2.imshow('face present', i1)
        cv2.waitKey(1000)

        image.save(io.BytesIO(), format='jpeg')
        image.save(search_term + 'image' + str(x) + '.png')
        print('x is', x)
        x += 1

    break

    stored += x

    if stored > num_pics:
        break
