import maya.cmds as cmds

def create_render_layers():
	cmds.createRenderLayer(name='FG', number=1)
	cmds.createRenderLayer(name='BG', number=2)
	cmds.createRenderLayer(name='SHD', number=3)
	cmds.createRenderLayer(name='zDepth', number=4)

def set_bg_layer():
	layer_objects = ['pSphere1', 'pCone1']
	cmds.editRenderLayerMembers('BG', layer_objects)

def set_shd_layer():
	layer_objects = ['pSphere1', 'pCone1', 'pPlane1', 'directionalLight1']

	cmds.editRenderLayerMembers('SHD', layer_objects)

	# Assign material to selected
	cmds.hyperShade(a='test_mat')