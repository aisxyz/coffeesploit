# -*- coding: utf-8 -*-
import urllib2
import re
import threading
import os
import sys
import socket
import signal
#from coffesploit.core.pluginmanage.plugin import Plugin

g_stop = False
g_lock = threading.Lock()

class Cmsshibie:
	def __init__(self):
		#super(Cmsshibie, self).__init__("cmsshibie")
		self.run_result = {}
		
	def status(self):
		return {'url': None}
		
	def run(self, status):
		if status and type(status) == dict:
			threads = []
			files = os.listdir("Bin")
			#print u"cms识别中....\n"
			#stop = False
			for f in files:  
				cms = Cms(status['url'], f)
				threads.append(cms)
			for t in threads:
				t.start()
			while True:
				if g_stop:
					break
		
	def result(self):
		pass
		
	def help(self):
		pass
	
class Cms(threading.Thread):
	def __init__(self, url, name):
		threading.Thread.__init__(self)
		self.url = url
		self.name = name

	def run(self):		
		filepath = "./Bin/" + self.name 
		i = 0
		for line in open(filepath): 
			global g_stop
			i = i + 1
			if i <= 2:
				continue
			texts = line.split("------")
			response = self.curl(texts[0])
			if re.search(texts[1], str(response)):
				print "识别结果\r\n"
				print self.url + " is: " + texts[2] + "\r\n"
				g_lock.acquire()
				g_stop = True
				g_lock.release()
				break
				
	def curl(self, path):
		url = self.url + path
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request, timeout=10)
			res = response.read()
			response.close()
		except urllib2.URLError,e:
			return e
		except socket.timeout as e:
			return e
		return res
		
if __name__ == '__main__':
    cmssh = Cmsshibie()
    cmssh.run({'url':'http://www.dedecms.com'})
