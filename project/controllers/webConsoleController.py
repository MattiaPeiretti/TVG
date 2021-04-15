# Libs
import flask
import subprocess
import time
import logging
import json

# adjusted flask_logger
def flask_logger():
    """creates logging information"""
    with open("log.log") as log_info:
        # for i in range(25):
        #     data = log_info.read()
        #     yield data.encode()
        #     time.sleep(0.1)

        data = log_info.read().splitlines() 
           
    return ''.join(data).replace('\n','')
    #return str(data).replace('", "', "<br>").replace(`)
        # Create empty job.log, old logging will be deleted
        #open("log.log", 'w').close()

def get_HTML_logstream():
    """returns logging information"""
    #return flask.Response(flask_logger())
    logs = "<style>body {background-color: black;}</style>"
    logs = logs + flask_logger()
    flask_logger()
    dataDict = {"data":logs} 
    return flask.Response(json.dumps(dataDict))