# Libs
import flask

# Controllers
import project.controllers.settingsController as settingsController
import project.controllers.pilotConsoleController as pilotConsoleController
import project.controllers.webConsoleController as webConsoleController
from project.agentsHandler import AgentsHanlder

agents_handler = AgentsHanlder()

router = flask.Blueprint(
    "pilot-console", __name__, "/pilot-console"
)  # Declaring the custom router


@router.route("/pilot-console")  # Handling /pilot-console
def console_route():
    return flask.render_template("console.html")


@router.route("/video_feed")
def video_feed_route():
    return pilotConsoleController.get_vision_feed()


@router.route("/settings", methods=["GET", "POST"])
def settings_route():
    return settingsController.render_settings()


@router.route("/reload-settings", methods=["POST"])
def reload_settings_route():
    return settingsController.reload_settings()


@router.route("/log_stream", methods=["GET"])
def log_stream_route():
    return webConsoleController.get_HTML_logstream()


@router.route("/web-console", methods=["GET"])
def web_console():
    return flask.render_template("WebLogs.html")


@router.route("/agents-checkup", methods=["GET"])
def agents_checkup():
    return flask.render_template("agentsCheckup.html", data=agents_handler.get_status())
