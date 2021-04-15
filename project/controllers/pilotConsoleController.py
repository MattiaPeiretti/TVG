# Libs
import flask

# Modules
from project.visionGrabber.device import Device

def get_vision_feed():
    return flask.Response(generate_frame_from_view(Device()), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frame_from_view(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(frame) + b'\r\n')