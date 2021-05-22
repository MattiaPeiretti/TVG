# ---------------------------------------------------------------------
# MAIN
# The code in this file takes care of initializing all of the needed
# systems in order to make the software work...
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

# Setting python path

# Libs
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import project.GUI.GUIServer as GUI
import logging, logging.config

# Modules
import project.customFormatters as customFormatters
from project.settingsHandler import SettingsHandler
from project.constants import Constants
from project.agentsHandler import AgentsHanlder
from project.weblogger.server import run_server


# Setting up the constants hanlder so that
# the dynamic constants are generated properly
constants = Constants()

# Quick Settings
LOG_LEVEL = "DEBUG" if constants.ENV_DEBUG else "INFO"


# Setting up logger
logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "()": customFormatters.WebConsoleFormatter
            },  # Adding custom formatter for the logs (to add colors)
            "console": {"()": customFormatters.ConsoleFormatter},
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "console",
            },
            "file": {
                "()": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "filename": f"{constants.LOG_STORE_PATH}/consoleOut.log",
                "maxBytes": 1024,
                "backupCount": 0,
                "encoding": "utf8",
            },
        },
        "root": {
            "level": LOG_LEVEL,  # Setting log level... ...To debug if GUI_DEBUG
            "handlers": ["wsgi", "file"],
        },
    }
)

logging.info("Logger initialized successfully")

# Initializing the settingsHandler
settings_handler = SettingsHandler()

SETTINGS_TEMPLATE_FILE_PATH = os.path.abspath(
    "../data/settings/settingsTemplate.json"
)  # Settings data
settings_handler.load_settings_template_file(
    SETTINGS_TEMPLATE_FILE_PATH
)  # Loading data

SETTINGS_FILE_PATH = os.path.abspath(
    "../data/settings/settingsData.json"
)  # Settings data
settings_handler.load_settings_data_file(SETTINGS_FILE_PATH)  # Loading data

agents_handler = AgentsHanlder()

agents_handler.push_agent(run_server, "WebLoggerSocketsServer")

agents_handler.run_all()
# Starting the GUI server
# GUI.app.run(debug=GUI_DEBUG);                                                                 # Running the GUI server

GUI.build_and_run_GUI_server(5000, constants.ENV_DEBUG)
# Running the GUI server
logging.info("Launched GUI instance")
