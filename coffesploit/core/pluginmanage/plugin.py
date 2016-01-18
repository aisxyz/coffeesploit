# -*- coding: utf-8 -*-
#from coffesploit.core.logmanager import logmanager

class Plugin(object):
    """
    This is the base class for aLL plugins, all plugins should inherit from it
    with '__init__()' parameter-free, and implement the following methods at least:
    status() --> Dict-like, used to do some setting.
    result() --> Dict-like, used to return executive outcomes.
    run()    --> None, used to run the current plugin.
    help()   --> String, used to show help information.
    """

    def run(self, status):
        pass

    def status(self):
        return {}
    
    def help(self):
		return("Use help command to get help information.\n")
		
    def result(self):
        """ reslut should return a dict-like  """
        return {}
