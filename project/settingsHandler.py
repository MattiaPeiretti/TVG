# ---------------------------------------------------------------------
# SETTINGS HANDLER
# This class takes care of handling and writing the global settings.
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

import json
import os

def load_json(file_path, custom_error="JSON file not found at: "):
    if not os.path.exists(file_path):                                                       #Checking wether the settings files exists
            raise ValueError("{} {}".format(custom_error, file_path))                       #Throwing error and returning

    with open(file_path) as data_file:                                                      #Open json file
            json_dict = json.load(data_file)                                                #Load json data

    return json_dict 

class SettingsHandler(object):
    __instance = None                                                                       #Instance shared varaible

    #Singleton
    def __new__(cls, *args, **kwargs):                                                      # Checking upon initialization that the class 
        if not SettingsHandler.__instance:                                                  # hasn't already been initialized
            SettingsHandler.__instance = object.__new__(cls)                                # if so returning the already
        return SettingsHandler.__instance                                                   # initialized instance..

    def __init__(self):
        self.settings_template = {}
        self.settings_template_filepath = ""

        self.settings_data = {}
        self.settings_data_filepath = ""

    # Settings UI

    def load_settings_template_file(self, file):
        self.settings_template = load_json(file, "Settings template file not found at:")    #Loading settings dict from file
        self.settings_template_filepath = file
        
    def reload_settings_template(self):
        self.settings_template = load_json(self.settings_template_filepath,
         "Settings file not found at:")                                                     #Loading settings dict from file
        
    def get_settings_template(self):
        return self.settings_template['sections']

    # Settings Data

    def load_settings_data(self, file):
        self.settings_data = load_json(file, "Settings template file not found at:")
        self.settings_data_filepath = file

    def reload_settings_data(self):
        self.settings_data = load_json(self.settings_data_filepath, 
                                        "Settings template file not found at:")

    def get_setting(self, setting):
        pass

    def set_setting(self, setting, value):
        pass

