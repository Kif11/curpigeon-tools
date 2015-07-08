import maya.cmds as cmds
import maya.mel
import shutil
import re
import os

# Extract sequence and shot number from maya scene name
# Assuming that the scene has folowing naming convention SQ01_SH01_KIR.ma
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

# Remove all namespaces in current scene
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


# Set tag attribute for given list of nodes
def set_tag(nodes, tag):

	for node in nodes:
		try:
			cmds.addAttr(node, longName='tag', dt='string')
			cmds.setAttr(node + '.tag', tag, type='string')
		except:
			print 'Can not set tag for', node
			pass

	return nodes


# Return a list of objects that have matching tag attribute
def list_by_tag(tag, **kwargs):
	
	selection = cmds.ls(**kwargs)
	
	nodes = []
	
	for node in selection:
		try:
			object_tag = cmds.getAttr(node + '.tag')
		except:
			object_tag = ''
			pass
		if tag == object_tag:
			nodes.append(node)
			
	return nodes


# Take a list of object and return root parent for each one
def get_roots(nodes):
	roots = []
	for node in nodes:
		try:
			root = '|' + cmds.listRelatives(node, allParents=True, fullPath=True)[0].split('|')[1]
			roots.append(root)
		except:
			pass
	
	# Return list with removed dublicates
	return list(set(roots))


# Return true if reference file already referenced in the scene
def reference_in_scene(scene):

	scene_references = cmds.ls(references=True)

	for node in scene_references:
		
		reference_file = cmds.referenceQuery(node, filename=True)
	
		if os.path.normpath(scene) == os.path.normpath(reference_file):
			
			print node, 'Already exists in the scene'
			
			return True
			
	return False


# Export given maya file as a reference.
def reference(scene):

	if not reference_in_scene(scene):
		objects = cmds.file(scene, reference=True, 
								   defaultNamespace=True, 
								   returnNewNodes=True)

		return objects


def create_render_layers(names):

	scene_render_layers = cmds.ls(type='renderLayer')

	for layer in names:
		if layer not in scene_render_layers:
			cmds.createRenderLayer(name=layer)


def set_layer_attr(node_type, attr_name, attr_value, layer):

	# Set currendt layer
	cmds.editRenderLayerGlobals(currentRenderLayer=layer)

	nodes = cmds.ls(type=node_type)

	for node in nodes:
		cmds.editRenderLayerAdjustment(node + '.' + attr_name, layer=layer)
		cmds.setAttr(node + '.' + attr_name, attr_value)