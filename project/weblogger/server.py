# ---------------------------------------------------------------------
# WEBLOGGER SERVER
# Websocket server, which broadcasts the log data, real-time, to the 
# web-client interface. 
#
# Written by Mattia Peiretti on 05/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

import asyncio
import websockets
import project.constants as constants

connected = set()
# adjusted flask_logger
def flask_logger():
    """creates logging information"""
    with open(f"../../data/logs/consoleOut.log") as log_info:
        # for i in range(25):
        #     data = log_info.read()
        #     yield data.encode()
        #     time.sleep(0.1)

        data = log_info.read().splitlines() 
           
    return ''.join(data).replace('\n','')
    #return str(data).replace('", "', "<br>").replace(`)
        # Create empty job.log, old logging will be deleted
        #open("log.log", 'w').close()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    
    try:
        while True:
            for conn in connected:
                await conn.send(flask_logger())
            await asyncio.sleep(1)
    finally:
        # Unregister.
        connected.remove(websocket)

    
def run_server(address=constants.WEBLOGGER_SERVER_ADDR, port=constants.WEBLOGGER_SERVER_PORT):
    start_server = websockets.serve(server, address, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever() 


if __name__ == "__main__":
    run_server()

    