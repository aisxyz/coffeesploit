# -*- coding: utf-8 -*-
from coffesploit.core.helpmanager import HelpManager
from coffesploit.core.pluginmanager import PluginManager
from coffesploit.core.logmanager import logmanager
from coffesploit.core.pluginmanage.resultplugin import run_result
from config import UPDATE_URL
import os

__Version__ = "0.2test"


class Coffesploit(object):
    """Main Class"""

    def __init__(self):
        self.pluginmanager = PluginManager()
        self.helper = HelpManager()
        self.plugin_list = self.get_plugin_list()
        self.cmd_list = {'use': self.use, 'set': self.set, 'run': self.run,
        				 'tools': self.tools, 'help': self.help, 'version': self.version,
        				 'update': self.update
        				 }

    def version(self):
        return(__Version__ + '\n')

    #def config_from(self, basedir, db_uri):
    #    self.basedir = basedir
    #    self.db_uri = db_uri

    def exec_cmd(self, cmd=['help']):
    	if cmd[0] in self.cmd_list:
    		return self.cmd_list[cmd[0]](*cmd[1:])
    		
				
    def set(self, arg1, arg2):
        self.pluginmanager.set_args(arg1, arg2)
        return ''
		
    def tools(self, tool=None, help='help'):
    	if tool in self.plugin_list and help=='help':
    		return self.pluginmanager.plugin_help()
    	elif not tool:
    		intermediateInfo = "All available tools are as follows:\n"
    		for plugin in self.plugin_list:
    			intermediateInfo += plugin + '\n'
    		return intermediateInfo
    	else:
    		raise TypeError
			
    def use(self, arg):
        if arg in self.plugin_list:
            return self.pluginmanager.load_plugin(arg)
        else:
            return("tool %s is not existed\n" %arg)	
	
    def help(self, arg='help'):
        """show help info of arg"""
        return self.helper.gethelp(arg)
	
    def run(self, method='text'):
        result = self.pluginmanager.plugin_run()
        if method == 'text':
            return(self.get_result_for_text() if result is True else result)
        elif method == 'visual':					# Visualization works only in web.
            return(self.get_result_for_visual() if result is True else result)
				
    def update(self):
		from config import UPDATE_URL
		import os
		try:
			with open(UPDATE_URL + "config.ini", 'w', 1) as plugin_config_file:
				for item in os.listdir(UPDATE_URL):
					if os.path.isdir(UPDATE_URL + item):
						for obj in os.listdir(UPDATE_URL + item):
							if os.path.isfile(os.path.join(UPDATE_URL + item, obj)) and obj[-3:] == ".py":
								if obj != "__init__.py":
									plugin_info = "%s,%s,%s,%s%s" %(item, obj[:-3].lower(), obj, obj[:-3], os.linesep)
									plugin_config_file.write(plugin_info)
							elif os.path.isdir(os.path.join(UPDATE_URL + item, obj)):		# indicate it is a package
								plugin_info = "%s,%s,%s,%s%s" %(item, obj.lower(), obj + '.' + obj + '.py', obj, os.linesep)
								plugin_config_file.write(plugin_info)
				return("Update succeed, restart the program to load them.\n")
		except:
			return self.helper.gethelp('update')
			
    def get_result_for_text(self):
        result = ("*"*40 + " Run results of %s " + "*"*40 +"\n") %(self.current_plugin_name())
        result += run_result.get_result_for_text(self.get_run_result())
        #while (not logmanager.log.empty()):
        #    result += '\n'+ str(logmanager.getlog())
        return result
    
    def get_result_for_visual(self):
    	result = run_result.get_result_for_visual(self.get_run_result(), self.current_plugin_name())
    	#f = open('test.txt', 'w')
    	#f.write(str(result))
    	#f.close()
    	return result
        
    def get_run_result(self):
        return self.pluginmanager.plugin_result()
		
    def get_plugin_list(self):
        return self.pluginmanager.get_plugins_list()

    def get_tool_categories(self):
        return self.pluginmanager.get_tool_categories()
			
    def get_tools_by_category(self):
        return self.pluginmanager.get_tools_by_category()
		
    def current_plugin_name(self):
        return self.pluginmanager.current_plugin_name

    def current_plugin_status(self):
        return self.pluginmanager.plugin_status()

