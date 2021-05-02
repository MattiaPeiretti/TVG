# ---------------------------------------------------------------------
# AGENTS HANDLER
# Manages the different agents (like the websocket servers 
# or rest servers), starting them in order, to make sure that the
# app can run correctcly.
#
# Written by Mattia Peiretti on 05/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------

#import threading
import threading
import logging
import os
from project.constants import Constants

# Setting up the constants
constants = Constants()

class AgentsHanlder():
    def __init__(self):
        self.agents_startups = [] # List of all of the agents running with agent data
        self.threads = list()     # List of all of the threads running

    def push_agent(self, agentFunc, agentName, TerminateFunc=None):

        # Data Validation..
        if not callable(agentFunc):
            raise Exception("Provide a valid callable function for start func")

        if (not callable(TerminateFunc) and TerminateFunc != None):
            raise Exception("Provide a valid callable function for terminate func")

        # Adding new agent object to the list
        self.agents_startups.append({
            "name": agentName,
            "func": agentFunc, 
            "termFunc": TerminateFunc,
            "is_running": False, 
            "thread": None
        })

        logging.debug(f"Registered new {agentName} agent to the agent list.")

    def get_status(self, agent=False):
        '''
        Returns the current state of all of the agents registered in the handler.
        To mean that it provides an list of object, one per agent, which tells whether 
        an agent is running or not.
        '''
        safe_list = []
        for agent in self.agents_startups:
            safe_list.append({
                "name": agent["name"],
                "is_running": agent["is_running"], 
            })
        return safe_list

    def run_all(self):
        # Making sure that flask is not auto reloading. If it is, then wait for the werkzeug app to fully load.
        # If so, returning without doing anything.
        # Otherwise all of the threads would be instanced twice creating hell on earth...
        if not (constants.ENV_DEBUG and os.environ.get("WERKZEUG_RUN_MAIN") == "true"):
            return

        for agent in self.agents_startups:
            # Killing already running threads if any
            if agent["thread"]:
                if agent["termFunc"]:
                    agent["termFunc"]()
                agent["thread"].join()
            
            # Creating the new thread
            agent["thread"] = threading.Thread(target=agent["func"], daemon=True)

            # Adding it to our threads list
            self.threads.append(agent["thread"])

            # Starting and registering the run of the thread,
            # if the thread is not running in the first place
            if not agent["thread"].is_alive():
                agent["thread"].start()
                agent["is_running"] = True
                logging.debug(f"Started agent: {agent['name']}")
        logging.debug("All agents initialized succesfully.")

    def terminate_all(self):
        for agent in self.agents_startups:
            if agent["termFunc"]:
                agent["termFunc"]()
            agent["thread"].join()
            agent["is_running"] = True
        logging.debug("All agents terminated succesfully.")
            