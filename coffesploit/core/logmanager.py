# -*- coding: utf-8 -*-
from Queue import Queue


class LogManager(object):
    def __init__(self):
        self.log = Queue()

    def puttolog(self,message):
        self.log.put_nowait(message)

    def getlog(self):
		log_obj = None
		if not self.log.empty():
			try:
				log_obj = self.log.get_nowait()
			except Queue.Empty:
				pass
		return log_obj

#instance
logmanager = LogManager()

if __name__ == "__main__":
	logmanager.puttolog("message1")
	logmanager.puttolog("msg2")
	logmanager.puttolog("msg3")
	for i in range(3):
		print logmanager.getlog()
	print "********* That's all ok! ********"
