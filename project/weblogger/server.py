# ---------------------------------------------------------------------
# WEBLOGGER SERVER
# Websocket server, which broadcasts the log data, real-time, to the 
# web-client interface. 
#
# Written by Mattia Peiretti on 05/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------
import logging
import asyncio
import websockets
import os
from project.constants import Constants

constants = Constants()

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    
    try:
        while True:
            with open(f"{constants.LOG_STORE_PATH}/consoleOut.log") as log_info:
                data = log_info.read().splitlines() 
            data = ''.join(data).replace('\n','')
            #data = "a"
            for conn in connected:
                await conn.send(data)
            await asyncio.sleep(1)
    finally:
        # Unregister.
        connected.remove(websocket)

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

    
def run_server(address=constants.WEBLOGGER_SERVER_ADDR, port=constants.WEBLOGGER_SERVER_PORT):
    get_or_create_eventloop()
    start_server = websockets.serve(server, address, port)
    
    get_or_create_eventloop().run_until_complete(start_server)
    get_or_create_eventloop().run_forever()

if __name__ == "__main__":
    run_server()

    