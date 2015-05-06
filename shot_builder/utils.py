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


# Debug
# file_name = '//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/Scenes/SQ05/SH16/maya/SQ05_SH16_02_KIR.ma'
# print extract_context(file_name)