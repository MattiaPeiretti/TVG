# ---------------------------------------------------------------------
# AGENTS HANDLER
# Manages the different agents (like the websocket servers
# or rest servers), starting them in order, to make sure that the
# app can run correctcly.
#
# Written by Mattia Peiretti on 05/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

# Libs
import threading
import logging
import os
import asyncio
import time
import websockets
import json
import io

# Modules
from project.constants import Constants

# Setting up the constants
constants = Constants()


class AgentsHanlder(object):
    __instance = None  # Instance shared varaible

    # Singleton
    def __new__(cls, *args, **kwargs):  # Checking upon initialization that the class
        if not AgentsHanlder.__instance:  # hasn't already been initialized
            AgentsHanlder.__instance = object.__new__(
                cls
            )  # if so returning the already
        return AgentsHanlder.__instance  # initialized instance..

    def __init__(self):
        self.agents = []  # List of all of the agents running with agent data
        self.threads = list()  # List of all of the threads running
        self.connected_clients = set()

    # ===== SERVER RELATED =====
    def __serve_forever(self):
        # Setting the event loop, so that the websockets framework can work properly.
        asyncio.set_event_loop(asyncio.new_event_loop())

        # Launching the server.
        start_server = websockets.serve(
            self.__server_handler,
            constants.AGENTSCHECKUP_SERVER_ADDR,
            constants.AGENTSCHECKUP_SERVER_PORT,
        )

        # Launching the server asyncronously.
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def __server_handler(self, websocket, path):
        # Register client.
        self.connected_clients.add(websocket)

        try:
            while True:
                fake_file = io.StringIO()
                json.dump(self.get_status(), fake_file)

                try:
                    data = fake_file.getvalue()
                except Exception as e:
                    data = ""
                    print(e)

                for conn in self.connected_clients:
                    await conn.send(data)
                    await asyncio.sleep(1)
        finally:
            # Closing the fake_file
            fake_file.close()
            # Unregister the client.
            self.connected_clients.remove(websocket)

    def __check_threads_life(self):
        while True:
            time.sleep(1)
            for agent in self.agents:
                if agent["thread"] and agent["thread"].is_alive():
                    if not agent["is_running"]:
                        logging.debug(
                            f'Agent {agent["name"]} has been detected online.'
                        )
                    agent["is_running"] = True
                else:
                    if agent["is_running"]:
                        logging.debug(
                            f'Agent {agent["name"]} has been detected offline.'
                        )
                    agent["is_running"] = False

    def __create_agent_checker(self):
        self.__launch_agent(
            agent_name="agentsChecker",
            agent_init_function=self.__check_threads_life,
            args=[],
        )

        self.__launch_agent(
            agent_name="agentsCheckerWSServer",
            agent_init_function=self.__serve_forever,
            args=[],
        )

    def __launch_agent(
        self,
        agent_name,
        agent_init_function,
        agent_term_function=None,
        args=None,
        agent_thread=None,
    ):
        # Killing already running threads if any
        if agent_thread and agent_thread.is_alive():
            if agent_term_function:
                agent_term_function()
            agent_thread.join()

        # Creating the new thread
        if args:
            agent_thread = threading.Thread(
                target=agent_init_function, args=args, daemon=True, name=agent_name
            )
        else:
            agent_thread = threading.Thread(
                target=agent_init_function, daemon=True, name=agent_name
            )

        logging.debug(f"Created agent's {agent_name} thread ")
        # Adding it to our threads list
        self.threads.append(agent_thread)

        # Starting and registering the run of the thread,
        # if the thread is not running in the first place
        if not agent_thread.is_alive():
            agent_thread.start()
        else:
            print("bobop")
        return agent_thread

    def push_agent(self, agentFunc, agentName, TerminateFunc=None):
        # Data Validation..
        if not callable(agentFunc):
            raise Exception("Provide a valid callable function for start func")

        if not callable(TerminateFunc) and TerminateFunc != None:
            raise Exception("Provide a valid callable function for terminate func")

        # Adding new agent object to the list
        self.agents.append(
            {
                "name": agentName,
                "func": agentFunc,
                "termFunc": TerminateFunc,
                "is_running": False,
                "thread": None,
            }
        )

        logging.debug(f"Registered new {agentName} agent to the agent list.")

    def get_status(self, agent_name=None):
        """
        Returns the current state of all of the agents registered in the handler.
        To mean that it provides an list of object, one per agent, which tells whether
        an agent is running or not.
        """
        safe_list = []
        for agent in self.agents:
            safe_list.append(
                {
                    "name": agent["name"],
                    "is_running": agent["is_running"],
                }
            )
            if agent["name"] == agent_name:
                return {
                    "name": agent["name"],
                    "is_running": agent["is_running"],
                }
        return safe_list

    def run_all(self):
        # Making sure that flask is not auto reloading. If it is, then wait for the werkzeug app to fully load.
        # If so, returning without doing anything.
        # Otherwise all of the threads would be instanced twice creating hell on earth...
        if not (constants.ENV_DEBUG and os.environ.get("WERKZEUG_RUN_MAIN") == "true"):
            return

        for agent in self.agents:
            agent["thread"] = self.__launch_agent(
                agent_name=agent["name"],
                agent_init_function=agent["func"],
                agent_term_function=agent["termFunc"],
                agent_thread=agent["thread"],
            )
            logging.debug(f"Started agent: {agent['name']}")
        logging.debug("All agents initialized succesfully.")

        # Calling the agentchecket to have constant feedback on the status of the agents
        self.__create_agent_checker()

    def terminate_all(self):
        for agent in self.agents:
            if agent["termFunc"]:
                agent["termFunc"]()
            agent["thread"].join()
            agent["is_running"] = True
        logging.debug("All agents terminated succesfully.")
