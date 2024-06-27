
#import kivy
#from kivy.uix.label import Label
#from kivy.app import App
import cv2
#import pyttsx3
"""
camera='''

BoxLayout:
    orientation:'horizonatl'
    Camera:
        resolution:(1920,1080)
        id:cam
        play:True




'''

"""

class myCamera():
    cap=cv2.VideoCapture(0)
    print("camera index..")
    
    global frame
    if cap.isOpened()==True:
        
        _,frame=cap.read()
        print('true')
    else:
        print("FALSE")
    while True:
        
        cap.release()
    
    

   
mycamera=myCamera()
