from project.settingsHandler import SettingsHandler
import project.GUI.GUIServer as GUI

# Quick Settings

GUI_DEBUG = True


# Initializing up the settingsHandler

SETTINGS_FILE_PATH = "../data/settingsTemplate.json"                            # Settings data
SettingsHandler().load_settings_file(SETTINGS_FILE_PATH)                        # Loading data

# Starting the GUI server

GUI.app.run(debug=GUI_DEBUG);                                                   # Running the GUI server












