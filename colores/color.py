import cv2
import numpy as np

def camera(R,b,label):
    cam=cv2.VideoCapture(0)
    Muno=np.ones((5,5),np.uint8)

    #definirn limite inferior


    while True:
        rest,frame=cam.read()
    #rano de busqueda de colores
        rangomax=np.array(R)
        rangomin=np.array(b)

        #funcion de busqueda
        mascare=cv2.inRange(frame,rangomin,rangomax)
        opening= cv2.morphologyEx(mascare,cv2.MORPH_OPEN,Muno)
        maskRedvis = cv2.bitwise_and(frame, frame, mask=mascare)




        #rectangulo y nombre
        x,y,w,h= cv2.boundingRect(opening)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        cv2.putText(frame,label, (x, y - 10),2,0.7,(0,0,0),2,cv2.LINE_AA)

        #cv2.circle(frame,(x+w/2,y+h/2),6,(0,0,100))
        cv2.imshow('camara',frame)
        cv2.imshow('verde',mascare)
        cv2.imshow('color',maskRedvis)
        k = cv2.waitKey(1)

        if k==ord('x'):
            break
