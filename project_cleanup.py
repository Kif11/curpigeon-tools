import shutil
import re
import os
import time

def project_cleanup():

	cwd = os.getcwd()

	# Grab curent time and date to create a dolder with unique name
	curDate = time.strftime("%d-%m-%Y")
	curTime = time.strftime("%H-%M-%S")

	subfolder_name = curDate + '_' + curTime

	print subfolder_name

	deleted_dir = os.path.normpath(os.path.join(cwd, 'Deleted', subfolder_name)) + '\\'

	# Files to recycle
	name_list = ['startup', 
				 'renderData', 
				 'export', 
				 'clip', 
				 'xgen', 
				 'slim', 
				 'renderman', 
				 'backup', 
				 'autosave', 
				 'particles',
				 'tmp',
				 'images',
				 'qubetmpfile',
				 'sound']

	file_list = []

	for f in os.listdir(cwd):
		file_list.append(os.path.join(cwd, f))

	# Create tresh directory if dosn't exist
	if not os.path.exists(deleted_dir):
		os.makedirs(deleted_dir)

	# Iterate trough file in directory and move matches into deleted_dir
	for name in name_list:
		for path in file_list:
			if re.search(name, path):
				new_path = path.replace(cwd, deleted_dir)
				shutil.move(path, new_path)
				print path, 'moved to %s' %new_path

project_cleanup()