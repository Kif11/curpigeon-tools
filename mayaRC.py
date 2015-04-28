import maya.cmds as cmds
import os
import shutil

# Define an empty list to store all external paths
path_list = []

# Given list of texture pathes will find the uvtiled one 
# and replace them wiht expanded version
def expand_uv_tiles(path_list):

	for path in path_list:

		mary_tile = '<UVTILE>'

		# For mary uvtiled textures
		if mary_tile in path:

			# Remove path from the list
			path_list.remove(path)

			utile = 1
			vtile = 1
			root, fila_name = os.path.split(path)
			name, ext = os.path.splitext(fila_name)

			name = name.replace(mary_tile, '')

			files = os.listdir(root)

			for f in files:
				if f.startswith(name):
					path_list.append(os.path.join(root, f))

			return path_list

# Return a list of all absolute texture path in the scene
def texture_paths():

	textureFileNodes = cmds.ls(typ='file')

	for node in textureFileNodes:
		path = cmds.getAttr(node + ".fileTextureName")

		# Expand path
		path = cmds.workspace(en=path)

		path_list.append(path)

	return path_list

def geo_paths():

	# VRayMesh
	VRayCacheFiles = cmds.ls(type = "VRayMesh")

	for node in VRayCacheFiles:
		path_list.append(cmds.getAttr(node + ".fileName"))

	# Alembic Cache
	alembicCache = cmds.ls(type = "AlembicNode")

	for node in alembicCache:
		path_list.append(cmds.getAttr(node + ".abc_File"))

	return path_list

def copy_external_assets(path_list):

	cur_project_dir = cmds.workspace(q=True, rd=True)
	new_project_dir = 'G:/SQ05/SH16'

	# Create new project dir if doesn't exist
	if not os.path.exists(new_project_dir):
		os.makedirs(new_project_dir)

	for path in path_list:
		# Validate that the file exist
		if os.path.exists(path):
			new_path = path.replace(cur_project_dir, new_project_dir)
			new_path = new_path.replace('\\', '/')

			# Create folders for current file
			if not os.path.isdir(os.path.split(new_path)[0]):
				os.makedirs(os.path.split(new_path)[0])

			# Copy file if doesnt exist
			if not os.path.isfile(new_path):
				shutil.copyfile(path, new_path)
				print new_path, "- File has been created"
			else:
				print new_path, "- File already exist"

def scene_path():
	scene_path = cmds.file(q=True, expandName=True)
	path_list.append(scene_path)


def main():

	# Add all the texture to path_list
	expand_uv_tiles(texture_paths())
	# Add all the geo in the list
	geo_paths()
	# Add scene
	scene_path()

	# Copy to a new location
	copy_external_assets(path_list)

	print 'DONE!'

main()


'''
# retrieve a string array of all files referenced in the scene
#
cmds.file( q=True, l=True )
# Result: C:/maya/projects/default/scenes/fred.ma C:/mystuff/wilma.mb C:/maya/projects/default/scenes/barney.ma
'''