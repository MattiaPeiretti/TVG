import flask
import subprocess
import time
import logging
from project.settingsHandler import SettingsHandler
from project.visionGrabber.device import Device

settings_handler = SettingsHandler()

router = flask.Blueprint("pilot-console", __name__, "/pilot-console")                   #Declaring the custom router

@router.route("/pilot-console")                                                         #Handling /pilot-console
def console_route():
    return flask.render_template("console.html")

@router.route('/video_feed')
def video_feed():
    return flask.Response(gen(Device()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@router.route("/settings", methods=["GET", "POST"])
def settings_route():
    if flask.request.method == "POST":
        new_settings_data = flask.request.form
        for key, value in new_settings_data.items():
            settings_handler.set_setting(key, value)
    
    settings_template = settings_handler.get_settings_template()
    settings_data = settings_handler.get_settings_data()
    
    return flask.render_template("settings.html", settings_template=settings_template, settings_data=settings_data)


@router.route("/reload-settings", methods=['POST'])
def reload_settings():
    settings_handler.reload_settings_template()
    return flask.redirect("/settings")

#TODO: Restructure in appropriate file
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(frame) + b'\r\n')

# adjusted flask_logger
def flask_logger():
    """creates logging information"""
    with open("log.log") as log_info:
        for i in range(25):
            data = log_info.read()
            yield data.encode()
            time.sleep(0.1)
        # Create empty job.log, old logging will be deleted
        #open("log.log", 'w').close()

@router.route("/log_stream", methods=["GET"])
def stream():
    """returns logging information"""
    return flask.Response(flask_logger(), mimetype="text/plain", content_type="text/event-stream")

