import os
import subprocess

class Maya(object):

	def __init__(self, template):

		self.template = template
		self.project_path = str(template.project_path)
		self.scripts_path = str(template.script_path)
		self.qube_path = os.path.join(self.scripts_path, 'qube')

		# Path to maya executable
		self.maya_exec = 'C:/Program Files/Autodesk/Maya2015/bin/maya.exe'

		self.cmd = self.maya_exec

	def run(self):

		# Path to qube submission script files
		

		# List of paths where maya are going to look for user preferences
		maya_user_prefs = ['H:/Code/Python/kk-maya-launcher/config/user_prefs/maya', 
						   'F:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
						   'G:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
						   'J:/Code/Python/kk-maya-launcher/config/user_prefs/maya',
						   'G:/maya',
						   '//180net1/Collab/tbertino_Curpigeon/Curpigeon_Project/Scripts/prefs/maya']

		# Set up environmental variables
		os.environ['MAYA_PROJECT'] = self.project_path
		os.environ['PYTHONPATH'] = self.scripts_path
		os.environ['MAYA_SCRIPT_PATH'] = os.pathsep.join([self.scripts_path, self.qube_path])

		# Iterate trough the list of user preferences directory
		for path in maya_user_prefs:
			# Check if directory is exist use it
			if os.path.exists(path):
				os.environ['MAYA_APP_DIR'] = path
				break

		# Print environment for debug
		print 'Project:', os.environ['MAYA_PROJECT']
		print 'User prefs:', os.environ['MAYA_APP_DIR']
		print 'Python scripts:', os.environ['PYTHONPATH']
		print 'Mel scripts:', os.environ['MAYA_SCRIPT_PATH']


		# Run application
		print 'Running command:', self.cmd
		subprocess.Popen(self.cmd)