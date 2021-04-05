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
        return SettingsHandler.__instance                                                   # inirialized instance..

    def __init__(self):
        self.save_file_path = ''

    def load_settings_file(self, file):
        self.settings_raw = load_json(file, "Settings file not found at:")                  #Loading settigs dict from file
        self.save_file_path = file
        self.parse_settings()

    def reload_settings(self):
        self.settings_raw = load_json(self.save_file_path, "Settings file not found at:")   #Loading settigs dict from file
        self.parse_settings()

    def parse_settings(self):
        self.parsed_data = self.settings_raw['sections']                                    #Select only specific settings data
        
    def get_json_settings_data(self):
        return self.parsed_data
