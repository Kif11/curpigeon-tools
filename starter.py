# from engines import maya
# import sys


# cwd = os.getcwd()
# sys.path.append(cwd)

# os.environ['STARTER'] = cwd

# maya = maya.Maya()

# maya.run()

import os
import subprocess


class Environment(object):

	def env (self, **kwargs):

		self.vars = kwargs

	def set_env (self):

		for key, value in self.vars.items():
			os.environ[key] = value
			print 'Setting', key, 'to', value



class Application(Environment):

	def __init__(self, name=None, exe=None):

		self.name = name
		self.exe = exe

	def start(self):

		subprocess.Popen(self.exe)
		print "Executing", self.exe


class Maya(Application):

	def __init__(self, project=None, script=None, user_pref=None):

		self.name = 'Maya'

		self._project = project
		self._script = script
		self._user_prefs = user_pref

	@property
	def project(self):
		return self._project

	@project.setter
	def project(self, value):

		self._project = value

		self.env(MAYA_PROJECT=self._project)
		self.set_env()

	@property
	def script(self):
	    return self._script

	@script.setter
	def script (self, value):

		self._script = value

		self.env(PYTHONPATH=self._script,
				 MAYA_SCRIPT_PATH=self._script)
		self.set_env()

	@property
	def user_prefs(self):
	    return self._user_prefs

	@user_prefs.setter
	def user_prefs(self, paths):

		for path in paths:
			# Check if directory is exist use it
			if os.path.exists(path):
				self.env(MAYA_APP_DIR=path)
				self.set_env()

				self._user_prefs = path

				break

	# Git-plus is suck but git controll is awesome!!!


if __name__ == '__main__':

	maya = Maya()

	maya.exe = '/Applications/Autodesk/maya2015/Maya.app/Contents/bin/maya'
	maya.project = '/Users/admin/Desktop/maya_test_project'
	maya.script = '/test/scrip/directory'
	maya.user_prefs = ['/Users/admin/Desktop/maya']

	maya.start()
