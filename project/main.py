# ---------------------------------------------------------------------
# MAIN
# The code in this file takes care of initializing all of the needed 
# systems in order to make the software work...
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

# Setting python path
import os, sys
sys.path.insert(0, os.path.abspath(".."))

from project.settingsHandler import SettingsHandler
import project.GUI.GUIServer as GUI

# Quick Settings
GUI_DEBUG = True


# Initializing up the settingsHandler
settings_handler = SettingsHandler()

SETTINGS_TEMPLATE_FILE_PATH = os.path.abspath("../data/settings/settingsTemplate.json")  # Settings data
settings_handler.load_settings_template_file(SETTINGS_TEMPLATE_FILE_PATH)                        # Loading data

SETTINGS_FILE_PATH = os.path.abspath("../data/settings/settingsData.json")  # Settings data
settings_handler.load_settings_data_file(SETTINGS_FILE_PATH)                        # Loading data

# Starting the GUI server

GUI.app.run(debug=GUI_DEBUG);                                                   # Running the GUI server












