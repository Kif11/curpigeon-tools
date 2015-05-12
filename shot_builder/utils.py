import maya.cmds as cmds
import maya.mel
import shutil
import re
import os


def extract_context(file_path):

	file_name = os.path.split(file_path)[1]

	# Non capturing group to skip special char and spaces (?:)
	# http://stackoverflow.com/questions/13964986/regex-and-the-or-operator-without-grouping-in-python

	p = re.compile(r'(?:/S|\s)*sq(\d*)_sh(\d*)', re.IGNORECASE)
	s = re.match(p, file_name)

	if s:
		sequence = s.group(1)
		shot = s.group(2)
	else:
		sequence, shot = '', ''

	return sequence, shot


def remove_namespaces():

	nameSpaceArray = cmds.namespaceInfo(  ":" , listOnlyNamespaces = True)

	# Remove maya internal namespaces from array
	nameSpaceArray.remove('UI')
	nameSpaceArray.remove('shared')

	countNS = len(nameSpaceArray)

	for i in range(0, countNS):
	    cmds.namespace( removeNamespace = ':'+ nameSpaceArray[i], mergeNamespaceWithRoot = True)

	if (countNS):
		remove_namespaces()

	return 0


def set_tag(nodes, tag):

	for node in nodes:
		try:
			cmds.addAttr(node, longName='tag', dt='string')
			cmds.setAttr(node + '.tag', tag, type='string')
		except:
			print 'Can not set tag for', node
			pass

	return nodes


def reference(scene):

	scene_references = cmds.ls(references=True)

	exists = False
	for node in scene_references:
	    if scene == cmds.referenceQuery(node, filename=True):
	    	exists = True
	    	print node, 'Already exists in the scene'
	    	return 0

	if not exists:
		objects = cmds.file(scene, reference=True, defaultNamespace=True, returnNewNodes=True)
		return objects




def create_render_layers():

	render_layers = ['FG', 'BG', 'SHD', 'zDepth']
	scene_render_layers = cmds.ls(type='renderLayer')

	for layer in render_layers:
		if layer not in scene_render_layers:
			cmds.createRenderLayer(name=layer)


# Debug
# file_name = '//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/Scenes/SQ05/SH16/maya/SQ05_SH16_02_KIR.ma'
# print extract_context(file_name)