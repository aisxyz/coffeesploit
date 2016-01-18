#/usr/bin/python
import ftplib
from coffesploit.core.pluginmanage.plugin import Plugin

class FtpAnonymousLogin(Plugin):
    def __init__(self):
        self.tool_name = "FtpAnonymousLogin"
        super(FtpAnonymousLogin, self).__init__(self.tool_name)
        self.host = None
        self.isvulnerable = False
        self.login_result = {}

    def status(self):
        super(FtpAnonymousLogin,self).status()
        return  {'host': self.host}

    def anonlogin(self, hostname):
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login('anonymous', 'me@your.com')
            ftp.quit()
            return True
        except Exception, e:
            return False

    def run(self,status):
        self.host = status['host']
        super(FtpAnonymousLogin, self).run(status)
        if self.anonlogin(self.host):
            self.isvulnerable = True

    def result(self):
        if self.isvulnerable is True:
            self.login_result['[+]' + str(self.host)] = 'FTP Anonymous Login Succeeded.'
        else:
			self.login_result['[-]' + str(self.host)] = 'FTP Anonymous Login Failed. '
        return self.login_result
			
	def help(self):
		"""Description: help information about ftpnmonymouslogin"""
