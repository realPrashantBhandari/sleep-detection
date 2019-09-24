import cv2
import numpy as np
import dlib
from math import hypot
import math
import time


font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0) 
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1,p2):
    return ( int((p1.x+p2.x)/2) , int((p1.y+p2.y)/2) )

def find_length(p1,p2):
    length = hypot((p1[0]-p2[0]) , (p1[1]-p2[1]))
    return(int(length))
start_count = 0
sleep_status = 0
sleep = 0
while True:
    _,frame = cap.read()
    #frame = raw_frame.copy()
    #frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.putText(frame,"Sleep:",(10,60), font, 1, (0,0,0))

    faces = detector(gray)
    cv2.putText(frame,str(sleep_status),(100,60), font, 1, (255,0,255)) # changing the sleep status
    i = 0
    for face in faces:
        if i == 0:

            landmarks = predictor(gray, face)
            # Left eye
            leye_lpoint = (landmarks.part(36).x,landmarks.part(36).y)
            leye_rpoint = (landmarks.part(39).x,landmarks.part(39).y)
            leye_centertop = midpoint(landmarks.part(37), landmarks.part(38))
            leye_centerbottom = midpoint(landmarks.part(41), landmarks.part(40))
            
            # Right eye
            reye_lpoint = (landmarks.part(42).x,landmarks.part(42).y)
            reye_rpoint = (landmarks.part(45).x,landmarks.part(45).y)
            reye_centertop = midpoint(landmarks.part(43), landmarks.part(44))
            reye_centerbottom = midpoint(landmarks.part(47), landmarks.part(46))

            #angle
            lcheek = (landmarks.part(1).x,landmarks.part(1).y)
            rcheek = (landmarks.part(15).x,landmarks.part(15).y)
            temp = (landmarks.part(1).x,landmarks.part(15).y)
            angle_diag = find_length(lcheek,rcheek)
            angle_hori = find_length(lcheek,temp)
            angle_rad = math.acos(angle_hori/angle_diag)
            angle = (angle_rad*180)/(2*math.pi)
            cv2.putText(frame,str(angle),(200,50), font, 1, (255,0,255))
            
            # Draw Line
            hor_line_leye = cv2.line(frame, leye_lpoint, leye_rpoint, (0,255,0),1)
            hor_line_reye = cv2.line(frame, reye_lpoint, reye_rpoint, (0,255,0),1)
            ver_line_leye = cv2.line(frame, leye_centertop, leye_centerbottom, (0,255,0),1)
            ver_line_reye = cv2.line(frame, reye_centertop, reye_centerbottom, (0,255,0),1)
            cheek_line = cv2.line(frame, lcheek, rcheek, (0,255,0),1)
            # finding length
            leye_verlength = find_length(leye_centertop,leye_centerbottom)
            reye_verlength = find_length(reye_centertop,reye_centerbottom)
            leye_horlength = find_length(leye_lpoint,leye_rpoint)
            reye_horlength = find_length(reye_lpoint,reye_rpoint)
            
            # Blink detection
            if leye_verlength == 0:
                leye_verlength=1
            if reye_verlength == 0:
                reye_verlength=1
            leye_ratio = leye_horlength/leye_verlength
            reye_ratio = reye_horlength/reye_verlength

            start = time.time()
            blinking_ratio = (leye_ratio+reye_ratio)/2
            
            # conditional statements to check if a person is asleep or not
            if blinking_ratio >5 or angle <34:
                start = time.time()
            elif blinking_ratio <= 5 or angle >34:
                end = time.time()

            if end != 0 and start != 0:
                if (start - end >5):
                    sleep_status = 1          
                else:
                    sleep_status = 0
                    
                if sleep_status == 1 and sleep == 0:
             
                    sleep = 1
                elif sleep_status == 0 and sleep ==1:
                    
                    sleep = 0
            i=i+1
            

        


    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cv2.destroyAllWindows
cap.release()
