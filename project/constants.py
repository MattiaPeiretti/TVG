# Libs
import os

class Constants(object):
    __instance = None                                                                       # Instance shared varaible

    #Singleton
    def __new__(cls, *args, **kwargs):                                                      # Checking upon initialization that the class 
        if not Constants.__instance:                                                        # hasn't already been initialized
            Constants.__instance = object.__new__(cls)                                      # if so returning the already
        return Constants.__instance                                                         # initialized instance..

    def __init__(self):
        # ---- SERVER ADDRESSES ----

        # GUI Server
        self.GUI_SERVER_PORT = 5000
        self.GUI_SERVER_ADDR = "localhost"
        self.GUI_SERVER_ADDR_FULL = f"{self.GUI_SERVER_ADDR}:{int(self.GUI_SERVER_PORT)}"

        # WebLogger Server
        self.WEBLOGGER_SERVER_PORT = 5002
        self.WEBLOGGER_SERVER_ADDR = "localhost"
        self.WEBLOGGER_SERVER_ADDR_FULL = f"{self.WEBLOGGER_SERVER_ADDR}:{int(self.WEBLOGGER_SERVER_PORT)}"

        # ---- MAIN ----
        self.DATA_FOLDER_PATH = os.path.abspath("../data/")
        self.ENV_DEBUG = True


        # ---- VISION ----

        # Default device to fall back if settingHandler fails.
        self.DEFAULT_DEVICE_ID = 0


        # ---- WEBLOGGER ----
        self.LOG_STORE_PATH = os.path.abspath("../data/logs/")