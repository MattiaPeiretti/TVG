import flask

router = flask.Blueprint("pilot-console", __name__, "/pilot-console")

@router.route("/pilot-console")
def console_route():
    return flask.render_template("console.html")

@router.route("/settings")
def settings_route():

    return flask.render_template("settings.html")