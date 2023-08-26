import cv2
import numpy as np
import dlib
from grabscreen import grab_screen

mon = (30,200,910,700)
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("dat/shape_predictor_68_face_landmarks.dat")

while True:
    frame = grab_screen(region=mon)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #_, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        #x1 = face.left()
        #y1 = face.top()
        #x2 = face.right()
        #y2 = face.bottom()
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, face)

        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)


    #cv2.imshow("Frame", frame)
    small_screen = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('Frame', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB ))
    #cv2.imshow('Frame', cv2.cvtColor(small_screen, cv2.COLOR_BGR2RGB ))
    key = cv2.waitKey(1)
    if key == 27:
        break
    if cv2.waitKey(33) == ord('a'):
        print ("pressed a")
        cv2.moveWindow('Frame', 40, 30)
        #break