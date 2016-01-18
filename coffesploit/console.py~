# -*- coding: utf-8 -*-
import os
import sys
from coffesploit.core.coffesplot import Coffesploit


class Console(object):
    def __init__(self):
        self.main = Coffesploit()
        self.cmd = None
        self.cmd_list = ('use', 'set', 'run', 'tools', 'exit', 'help', 'update', 'banner', 'version')

    def get_input(self):
        sys.stdout.write(self.main.pluginmanager.current_plugin_type + "/" +
                         self.main.pluginmanager.current_plugin_name + '>')
        self.cmd = sys.stdin.readline().strip()

    def start(self):
        self.banner()
        while 1:
            try:
                # show plugin name in shell
                if self.main.pluginmanager.current_plugin_name:
                    self.cmd = raw_input(self.main.pluginmanager.current_plugin_type + "/" +
                                         self.main.pluginmanager.current_plugin_name + '>')
                else:
                    self.cmd = raw_input('>')
                self.parsecmd(self.cmd.strip())
            except EOFError:
                print("There have something wrong.")
            except KeyboardInterrupt:
                print "\nKeyboardInterrupt"
                self.exit()

    def banner(self):
        print ("""

            Welcome to CoffeSploit :)


                   .:::::..        ..
             :jtii;;;,,,,::::::::.........
             ... :ii;,,,,,:::::::::::::,it
             ..................::::,,;ittf
             :................::::,,,;ittf
             :................::::,,,;ittfL;,::
             ::...............::::,,,;iitfiL  j:
              :.............::::::,,,;iitf.    i,
              :..............::::,,,;;iitL     j:
              ::.............::::,,,;;ittL     .:
              ::............:::::,,,;;itf      t:
              :.............:::::,,,;;itf      :;
               ::...........::::,,,;;;ijL     ,:
               ::...........:::::,,,;itj.    ,:j
            ,,,,::.........::::::,,;;itftttt::j
         ,,,,,;;:::........:::::,,,;itjGjf, :ftt
       ,;;;;;;;;,::::....::::::,,,;;ijLi,,,ijjti;;
       ;;;;;;;;;;,::::::::::::,,,;;itfDiiGfjjti;;,....
        i;;;;;;;ii,::::::::::,,,;;itfDDGLffjti;;;;:...
         ,i;;iiiiti,,,:::::,,,,;;itfGDDGLfjtii;:,,::::
         j   iiittjfi;,,,,,,;;;itjfGEDGLftti..tti;,,::
        ..:iji,     tEGfjtttjjfLGE#E;   .:jLGDGfji;,,:
       ..:,;tjGfjtiii;,,:::..::,,;iitjffLGKEEDGLfti;,:
       ..:,;itjfGDGGLffjjjjjjjjjffLLGDEWKKEEDGLfjti;,:
       ...:,,;itjfLDEfijGEKKKKKKDLLEWKEEEDGGLfftti;,::
         ..::,,;iitjffLGGDDDEEEDDDDDGGGLLLffjtii;,,::.
           ...::,,,;;iittjjjjjfffjjjjjjttii;;,,:::....



                                              """)

    def exit(self):
        print("\n good bye! \n")
        exit(0)

    def parsecmd(self, cmd):
    	if cmd in ('exit','banner'):
    		self.banner() if cmd=="banner" else self.exit()
    	else:
    		if not cmd:
    			return
    		cmd = cmd.split()
    		if cmd[0] in self.cmd_list:
    			print self.main.exec_cmd(cmd)
    		else:
    			print("No such command!\n")
