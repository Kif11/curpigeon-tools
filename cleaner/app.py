import re
import os
import time
import shutil
import win32con
import win32api
from lib.pathlib import Path


class Cleaner(object):

	def __init__(self, template):

		self.template = template

		self.project_path = template.project_path
		self.deleted_dir = Path('Deleted')

	def walklevel(self, some_dir, level=1):
		
		some_dir = str(some_dir)
		some_dir = some_dir.rstrip(os.path.sep)
		assert os.path.isdir(some_dir)
		num_sep = some_dir.count(os.path.sep)
		for root, dirs, files in os.walk(some_dir):
			yield root, dirs, files
			num_sep_this = root.count(os.path.sep)
			if num_sep + level <= num_sep_this:
				del dirs[:]

	def project_cleanup(self):

		# Grab curent time and date to create a dolder with unique name
		curDate = time.strftime("%d-%m-%Y")
		curTime = time.strftime("%H-%M-%S")

		subfolder_name = Path(curDate + '_' + curTime)

		# Files to recycle
		files_to_recycle = {'Curpigeon_Project': ['startup', 
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
												 'sound',
												 'Keyboard',
												 '.DS',
												 'SQ'],

							'Render': ['FG',
									   'BG', 
									   'defaultRenderLayer', 
									   'SHD',
									   'Leaves', 
									   'tmp', 
									   'zDepth', 
									   '.DS_Store',
									   '.iff'],

							'Scenes': ['.mb', '.DS'],
							'Cache': ['bifrost', 'particles', '.DS']
							}


		for root, dirs, files in self.walklevel(self.project_path, level=1):

			root = Path(root)
			stem = root.stem

			# For every root folder name in the files_to_recycle dictonary
			# check if there is a folder with coresponding name.
			# If so look fo forbidden files and move them to Deleted directory
			# under the coresponding root
			for key, value in files_to_recycle.items():

				if key == stem:

					# Create Deleted directory and current time/date directory
					deleted_path = root / self.deleted_dir / subfolder_name
					deleted_path.mkdir(parents=True)

					win32api.SetFileAttributes(str(root / self.deleted_dir), win32con.FILE_ATTRIBUTE_HIDDEN)

					for name in value:
						for file_name in dirs + files:
							if file_name.startswith(name) or file_name.endswith(name):

								old_path = root / Path(file_name)
								new_path = deleted_path / Path(file_name)

								try:
									shutil.move(str(old_path), str(new_path))

									print '%s moved to %s' % (old_path, new_path)
								except:
									print old_path, 'can not be moved'
									pass
		print 'Project', self.project_path, 'has been cleaned'

if __name__ == '__main__':
	project_cleanup()