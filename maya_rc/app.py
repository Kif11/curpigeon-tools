import maya.cmds as cmds
import os
import shutil


# Given list of texture pathes will find the uvtiled one 
# and replace them wiht expanded versions
def expand_uv_tiles(path_list):

	for path in path_list:

		mary_tile = '<UVTILE>'

		# For mary uvtiled textures
		if mary_tile in path:

			# Remove original unexpanded path from the list
			path_list.remove(path)

			# Split path into name components
			root, fila_name = os.path.split(path)
			name, ext = os.path.splitext(fila_name)

			# Remove uvtile expresion from name
			name = name.replace(mary_tile, '')

			# List all files in this directory
			files = os.listdir(root)

			# If file name match to original uvtile name
			# append it to path  
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

	vray_meshes = [cmds.getAttr(node + ".fileName") for node in cmds.ls(type = "VRayMesh")]
	alembic_caches = [cmds.getAttr(node + ".abc_File") for node in cmds.ls(type = "AlembicNode")]

	return vray_meshes + alembic_caches

# Return a list of file path from all referenc node in the scene
def references_paths():
	
	# Using python list comprehension to construct a list
	return [cmds.referenceQuery(node, filename=True) for node in cmds.ls(references=True)]
    	

def copy_external_assets(new_project, path_list):

	cur_project_dir = cmds.workspace(q=True, rd=True)

	# Create new project dir if doesn't exist
	if not os.path.exists(new_project):
		os.makedirs(new_project)

	for path in path_list:
		# Validate that the file exist
		if os.path.exists(path):
			new_path = path.replace(cur_project_dir, new_project)
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


def main():

	scene_path = cmds.file(q=True, expandName=True)

	path_list = expand_uv_tiles(texture_paths() + geo_paths() + references_paths() + scene_path)

	# Copy to a new location
	copy_external_assets('G:/SQ05/SH16', path_list)

	print 'DONE!'

main()