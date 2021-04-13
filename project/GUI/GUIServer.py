# ---------------------------------------------------------------------
# GUI Server
# The code in this file takes care of creating a flask app instance,
# to host in and to load the all of the routes
#
# Written by Mattia Peiretti on 04/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

import os
import logging
import flask.logging as Flask_logging

from .routes import router
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        TESTING=True,
    )

    app.logger.removeHandler(Flask_logging.default_handler)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(router)                                  # Adding blueprint

    return app

app = create_app()
logging.debug("Created GUI instance")

def runGUI():
    app.run(port=5000, debug=True)