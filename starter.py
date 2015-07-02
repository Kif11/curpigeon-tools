# from engines import maya
# import sys
# import os

# cwd = os.getcwd()
# sys.path.append(cwd)

# os.environ['STARTER'] = cwd

# maya = maya.Maya()

# maya.run()

import subprocess


class Environment(object):

	def env (self, **kwargs):

		self.vars = kwargs

	def set_env (self):

		for key, value in self.vars.items():
			print 'Setting', key, 'to', value
		


class Application(Environment):

	def __init__(self, name=None, exe=None):

		self.name = name
		self.exe = exe

	def start(self):

		# subprocess.Popen(cmd)
		print "Executing", self.exe


class Maya(Application):

	def __init__(self, project=None):

		self.name = 'Maya'
		self._project = project

	@property
	def project(self):
		return self._project

	@project.setter
	def project(self, value):

		self.env(PROJECT="D:/MayaProject")
		self.set_env()

		self._project = value


maya = Maya()

maya.env(APPDIR='F:/SomeDir', FRAMEBUFFER=1)
maya.set_env()

maya.exe = 'C:/Maya.exe'
maya.project = 'D:/MyProject'

maya.start()