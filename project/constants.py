# Libs
import os

# ---- SERVER ADDRESSES ----

# GUI Server
GUI_SERVER_PORT = 5000
GUI_SERVER_ADDR = "localhost"
GUI_SERVER_ADDR_FULL = f"{GUI_SERVER_ADDR}:{int(GUI_SERVER_PORT)}"

# WebLogger Server
WEBLOGGER_SERVER_PORT = 5002
WEBLOGGER_SERVER_ADDR = "localhost"
WEBLOGGER_SERVER_ADDR_FULL = f"{WEBLOGGER_SERVER_ADDR}:{int(WEBLOGGER_SERVER_PORT)}"

# ---- MAIN ----
DATA_FOLDER_PATH = os.path.abspath("../data/")

# ---- VISION ----

# Default device to fall back if settingHandler fails.
DEFAULT_DEVICE_ID = 0


# ---- WEBLOGGER ----
LOG_STORE_PATH = os.path.abspath("../data/logs/")