#camera.py
# import the necessary packages
import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(1)
    
    def __del__(self):
        #releasing camera
        self.video.release()

    def get_frame(self):
       #extracting frames
        ret, frame = self.video.read()
        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()