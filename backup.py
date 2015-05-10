import os
import shutil
import re

characters = {
				'Humans' : ['Tom', 'Vincent', 'Joe', 'Bob', 'George', 'Ernest'], 
				'Pigeons': ['Rocky', 'Raggedy', 'Scrawny', 'Longbeak', 'Heavy', 'Boxy']
			 }

def backup_char(char_type, char_name):

	project_path = '//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project'
	human_path = '/Assets/Char/Geo/%s' % char_type
	file_name = 'GEO_%s.ma' % char_name
	name, ext = os.path.splitext(file_name)
	char_root = '%s/%s/%s' % (project_path, human_path, char_name)
	char_master = '%s/%s' % (char_root, file_name)
	wip_path = '%s/wip' % char_root

	if not os.path.exists(wip_path):
		os.mkdir(wip_path)

	wip_files = os.listdir(wip_path)

	# If files in directory
	if len(wip_files) == 0:
		version = 1
	# If there are files find the last version
	else:
		version_list = []
		for f in wip_files:
			search = re.search(r'\d+', f)
			if search:
				version_list.append(int(search.group()))
		version = sorted(version_list)[-1:][0] + 1

	print char_name, 'version', version, 'createed'

	new_name = '%s_%02d%s' % (name, version, ext)
	new_version_path = '%s/%s' % (wip_path, new_name)
	shutil.copy(char_master, new_version_path)

def backup_all_characters():
	for char_type in characters.keys():
		for char in characters[char_type]:
			backup_char(char_type, char)

backup_all_characters()