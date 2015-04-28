import os
import subprocess

cwd = os.getcwd()
maya_exec = 'C:/Program Files/Autodesk/Maya2015/bin/maya.exe'

# List of paths where maya are going to look for user preferences
maya_user_prefs = ['H:/Code/Python/kk-maya-launcher/config/user_prefs/maya', 
				   'F:/Code/Python/kk-maya-launcher/config/user_prefs/maya'
				   'G:/Code/Python/kk-maya-launcher/config/user_prefs/maya']

cmd = maya_exec

# Set up environmental variables
os.environ['MAYA_PROJECT'] = cwd
os.environ['PYTHONPATH'] = os.path.join(cwd, 'scripts')
os.environ['MAYA_SCRIPT_PATH'] = os.path.join(cwd, 'Scripts')

for path in maya_user_prefs:
	if os.path.exists(path):
		os.environ['MAYA_APP_DIR'] = path

subprocess.Popen(cmd)