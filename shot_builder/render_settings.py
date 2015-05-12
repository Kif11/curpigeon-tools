import maya.cmds as cmds
import maya.mel
import os.path
import utils

def configure_render():

	cwd = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

	vr_setings_node = 'vraySettings'

	# Delete vray settings node if alredy exist
	if cmds.objExists(vr_setings_node):
		cmds.delete(vr_setings_node)

	vr_settings_file = '%s/lib/vray_settings.ma' % cwd

	# Impor a new vray settings node
	cmds.file(vr_settings_file, i=True)


configure_render()