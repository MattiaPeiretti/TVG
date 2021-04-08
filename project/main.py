# Setting python path
import os, sys
sys.path.insert(0, os.path.abspath(".."))

from project.settingsHandler import SettingsHandler
import project.GUI.GUIServer as GUI

# Quick Settings
GUI_DEBUG = True


# Initializing up the settingsHandler

SETTINGS_FILE_PATH = os.path.abspath("../data/settings/settingsTemplate.json")  # Settings data
SettingsHandler().load_settings_template_file(SETTINGS_FILE_PATH)                        # Loading data

# Starting the GUI server

GUI.app.run(debug=GUI_DEBUG);                                                   # Running the GUI server












