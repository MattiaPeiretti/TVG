import flask
from settingsHandler import SettingsHandler

settings_handler = SettingsHandler()

router = flask.Blueprint("pilot-console", __name__, "/pilot-console")                   #Declaring the custom router

@router.route("/pilot-console")                                                         #Handling /pilot-console
def console_route():
    return flask.render_template("console.html")

@router.route("/settings")
def settings_route():
    settings_data = settings_handler.get_json_settings_data()
    
    return flask.render_template("settings.html", settings=settings_data)