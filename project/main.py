# ---------------------------------------------------------------------
# MAIN
# The code in this file takes care of initializing all of the needed 
# systems in order to make the software work...
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

import os 
import sys
from project.settingsHandler import SettingsHandler
import project.GUI.GUIServer as GUI
import logging, logging.config

# Setting python path
sys.path.insert(0, os.path.abspath(".."))

# Quick Settings
GUI_DEBUG = True

# Setting up logger
logging.config.dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

logger = logging.getLogger("main_logger")


# Initializing the settingsHandler
settings_handler = SettingsHandler()

SETTINGS_TEMPLATE_FILE_PATH = os.path.abspath("../data/settings/settingsTemplate.json")  # Settings data
settings_handler.load_settings_template_file(SETTINGS_TEMPLATE_FILE_PATH)                        # Loading data

SETTINGS_FILE_PATH = os.path.abspath("../data/settings/settingsData.json")  # Settings data
settings_handler.load_settings_data_file(SETTINGS_FILE_PATH)                        # Loading data

# Starting the GUI server

GUI.app.run(debug=GUI_DEBUG);                                                   # Running the GUI server












