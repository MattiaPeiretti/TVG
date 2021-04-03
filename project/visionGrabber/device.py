# ---------------------------------------------------------------------
# DEVICE
# This module takes care of handling the video devices.
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

# Libs
import cv2

# Modules
from project.settingsHandler import SettingsHandler
import project.baseConfig as base_config


class Device(object):
    def __init__(self):
        #capturing video
        # self.video_device = cv2.VideoCapture(base_config.DEFAULT_DEVICE_ID or SettingsHandler().get_setting("DEVEICE_ID"))
        #TODO: Implement settings handler device setting
        self.video_device = cv2.VideoCapture(1)

    def __del__(self):
        #releasing camera
        self.video_device.release()

    def get_frame(self):
       #extracting frames
        ret, frame = self.video_device.read()
        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()