# ---------------------------------------------------------------------
# CUSTOM LOGGER
# The code in this file takes care of setting up the logger 
# that the system uses to log globally...
#
# Written by Mattia Peiretti on 04/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

import logging

class ConsoleFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    # Terminal Color codes
    green = "\u001b[32m"
    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    # Format strings
    format = "%(asctime)s - %(levelname)s at [%(module)s] → %(message)s"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class WebConsoleFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    #Terminal Color codes
    green =     "<span style='color: green;'>"
    grey =      "<span style='color: white;'>"
    yellow =    "<span style='color: yellow;'>"
    red =       "<span style='color: red;'>"
    bold_red =  "<span style='color: red; font-weight: 800;'>"
    reset = "</span><br />"

    # Format strings
    format = "%(asctime)s - %(levelname)s at [%(module)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)