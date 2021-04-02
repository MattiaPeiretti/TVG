# ---------------------------------------------------------------------
# AGENT STACK
# Takes care of distributing agents among the files.
#
# Written by Mattia Peiretti on 03/2021, https://mattiapeiretti.com
# ---------------------------------------------------------------------


class DependencyDistributor(object):
    __instance = None                                                       #Instance shared varaible

    #Singleton
    def __new__(cls, *args, **kwargs):                                      # Checking upon initialization that the class 
        if not DependencyDistributor.__instance:                            # hasn't already been initialized
            DependencyDistributor.__instance = object.__new__(cls)          # if so returning the already
        return DependencyDistributor.__instance                             # inirialized instance..

    def __init__(self):
        self.stack = {}                                                     # Declare agents dict
        self.is_initialized = False
        
    def add_dependency(self, dependency, dependency_name):
        self.stack[dependency_name] = dependency

    def get_dependency_instance(self, dependency_name):
        if self.stack[dependency_name]:
            return self.stack[dependency_name]
        raise ValueError("Agent not found")
    
    def initialize(self):
        self.is_initialized = True