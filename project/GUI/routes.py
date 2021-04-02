import flask
from settingsHandler import SettingsHandler
from videoGrabber.camera import VideoCamera

settings_handler = SettingsHandler()

router = flask.Blueprint("pilot-console", __name__, "/pilot-console")                   #Declaring the custom router

@router.route("/pilot-console")                                                         #Handling /pilot-console
def console_route():
    return flask.render_template("console.html")

@router.route("/settings")
def settings_route():
    settings_data = settings_handler.get_json_settings_data()
    
    return flask.render_template("settings.html", settings=settings_data)

def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(frame) + b'\r\n')

@router.route('/video_feed')
def video_feed():
    return flask.Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')