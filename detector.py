#This code is responsible for the detection of the student as well as for recording the attendance

import cv2,os
import numpy as np
from PIL import Image 
import pickle
from openpyxl import Workbook
import datetime
book=Workbook()
sheet=book.active
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
cam = cv2.VideoCapture(0)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
font = cv2.FONT_HERSHEY_SIMPLEX
now= datetime.datetime.now()
today=now.day
month=now.month
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #cv2.cv.PutText(cv2.cv.fromarray(im),str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 255) #Draw the text
        cv2.putText(im, str(nbr_predicted), (x,y-40), font, 2, (255,255,255), 3)
        sheet.cell(row=int(nbr_predicted), column=int(today)).value = "Present"
        cv2.imshow('im',im)
        book.save(str(month)+'.xlsx')
        cv2.waitKey(10)
