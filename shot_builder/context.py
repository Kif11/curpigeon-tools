import os
import re
import sys
from lib.pathlib import *

class UI():

	def __init__(self):
		self.sequence = 33
		self.shot = 44
		self.user = 'DMK'


class Context(object):


	def __init__(self, ui=None):

		self.platform_name = {"linux2": "linux", "darwin": "mac", "win32": "windows"}[sys.platform]
		
		self._project_root = None
		self._scene_path = None
		self.file_name = None

		self.shot_code_temlate = r'SQ(?P<sequence>\d*)_SH(?P<shot>\d*)'

		self.ui = ui

	@property
	def project_root(self):

		return self._project_root

	@project_root.setter
	def project_root(self, path):

		if self.platform_name == 'windows':
			self._project_root = PureWindowsPath(path)
		elif self.platform_name == 'mac':
			self._project_root = PureMacPath(path)

	@property
	def scene_path(self):
		return self._scene_path


	@scene_path.setter
	def scene_path(self, path):

		if self.platform_name == 'windows':
			self._scene_path = PureWindowsPath(path)
			self.file_name = self._scene_path.stem

		elif self.platform_name == 'mac':
			self._scene_path = PureMacPath(path)
			self.file_name = self._scene_path.stem


	@property
	def get(self):

		self.update_context()

		return self.context


	def update_context(self):

		# First try to extract context from UI
		if self.ui:
			self.context_from_ui()

		# Then try to extract context from file name
		elif self.scene_path:
			self.context_from_filename()

		elif self.file_name:
			self.context_from_filename()


	# Use regex to extract context from filename base on shot_code_temlate
	def context_from_filename(self):

		print 'Extracting context from filename', self.file_name

		s = re.match(self.shot_code_temlate, self.file_name)

		if s:
			self.context = s.groupdict()
		else:
			print 'Faile to match %s file name to %s template' % (self.file_name, self.shot_code_temlate)
			self.context = {}


	def context_from_ui(self):

		sequence = self.ui.sequence
		shot = self.ui.shot
		user = self.ui.user

		self.context = {'sequence': sequence,
					   	'shot': shot, 
					   	'shot_code': user}



# myUI = UI()

# my_context = Context()

# my_context.ui = myUI

# my_context.project_root = 'C:/project'

# print my_context.project_root

# my_context.scene_path = 'C:/project/sequence/shot/SQ11_SH99_KIR_something_01.ma'

# print my_context.get
