import maya.cmds as cmds
import maya.mel
import os.path
import utils
import re
import shutil
import context

# Reload for debug purposes
reload(utils)
reload(context)

class App(object):


	def __init__(self):

		self.characters = {
			'Humans' : ['Tom', 'Vincent', 'Joe', 'Bob', 'George', 'Ernest'], 
			'Pigeons': ['Rocky', 'Raggedy', 'Scrawny', 'Longbeak', 'Heavy', 'Boxy']
			 }

		# Path to current scene file
		scene_path = cmds.file(q=True, sceneName=True)
		
		my_context = context.Context()

		if scene_path:

			my_context.scene_path = scene_path
		
			self.sequence = my_context.get['sequence']
			self.shot = my_context.get['shot']

		else:

			self.sequence = '' 
			self.shot = ''

		# Run directory
		self.cwd = os.getcwd().replace('\\', '/')

		# Script directory
		self.app_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

		# Project directory
		self.project_path = cmds.workspace(q=True, rootDirectory=True)


		# Initilize UI
		self.ui()

		


	def ui(self):

		# ESTABLISHES THE UI
		flWin = cmds.window(title="Curpigeon Scene Setup", wh=(378,156), maximizeButton=True, minimizeButton=False, resizeToFitChildren=True)
		cmds.columnLayout(adjustableColumn = True)

		# Characters Imports

		cmds.text(label='Project Path' , align = 'left')
		project_path = cmds.textField(w=100, tx= self.project_path, editable= False) #Creates the projectPath Variable

		cmds.rowColumnLayout( numberOfColumns=6 )


		# cmds.rowColumnLayout( numberOfRows=1 )

		cmds.text( label='SQ', align='right')
		self.stringSQ = cmds.textField(w=20, tx=self.sequence)

		cmds.text( label='SH', align='right' )
		self.stringSH = cmds.textField(w=20, tx=self.shot)


		self.char_checkboxes = {}
		for kind in self.characters:
			for char in self.characters[kind]:
				self.char_checkboxes[char] = cmds.checkBox(label=char, value=False)


		cmds.button(label='FRANGE', w=40, command=self.set_frame_range)
		cmds.button(label='GOTO SG', w=40, command=self.goto_sg)

		cmds.button(label='ENV', w=40, command=self.import_env)
		cmds.button(label='CAM', w=60, command=self.import_cam)
		cmds.button(label='LIGHT', w=60, command=self.import_light)

		cmds.button(label='GEO', w=60, h=40, command=self.import_geo)
		cmds.button(label='ABC', w=60, command=self.import_abc)

		cmds.button(label='LAYERS', w=100, command=self.configure_layers)
		cmds.button(label='VRAY SETTINGS', w=100, command=self.configure_render)
		cmds.button(label='OPEN FOR EDIT', w=100, command=self.open_for_edit)
		
		
		cmds.showWindow(flWin)

	# # Return curent sequnce and shot number specified in corespondin fields
	# def context(self):

	# 	sequence = cmds.textField(self.stringSQ, q=True, text=True )
	# 	shot = cmds.textField(self.stringSH, q=True, text=True )


	# 	if shot == '' or sequence == '':
	# 		print 'Specify your shot and sequence first'

	# 		# TODO:(kirill) Need to breake here somehow???
	# 		return 0

	# 	shot_code = 'SQ' + sequence + '_' + 'SH' + shot

	# 	return {'sequence': int(sequence),
	# 			'shot': int(shot), 
	# 			'shot_code': shot_code}

	# Return dictionary of char name : path to character geo file
	def geo_paths(self):

		char_geo_dir = 'Assets/Char/Geo'

		paths = {}
		for kind in self.characters:
			for char in self.characters[kind]:

				paths[char] = '%s/%s/%s/%s/GEO_%s.ma' % (self.project_path, 
																		char_geo_dir, 
																		kind, 
																		char, 
																		char)
		return paths

	# Return dictionary of char name : path to character cache file
	def cache_paths(self, sequence, shot):

		# Reference path
		# //netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/Cache/Anm/CHAR/SQ05/SH16/SQ05_SH16_Bob.abc'

		char_cache_dir = 'Cache/Anm/CHAR'

		paths = {}
		for kind in self.characters:
			for char in self.characters[kind]:

				paths[char] = '%s/%s/SQ%02d/SH%02d/SQ%02d_SH%02d_%s.abc' % (self.project_path, 
																			char_cache_dir, 
																			sequence,
																			shot,
																			sequence,
																			shot,
																			char)
		return paths

	# Return dictionary of boolean values of character checkboxes
	def char_values(self):

		char_values = {}
		for char, check_box in self.char_checkboxes.items():
			char_values[char] = cmds.checkBox(check_box, q=True,value=True )

		return char_values

	# Open Shotgun shot page
	def goto_sg(self, *args):

		shot = self.find_shot(147, self.context()['shot_code'])

		curpigeon_url = 'https://aau.shotgunstudio.com/page/6503'

		shot_url = '%s#Shot_%s_%s' %(curpigeon_url, 
									shot['id'],
									shot['code'])

		cmd = 'start chrome %s' %shot_url

		os.system(cmd)

	# Find sot on SH and return it
	def find_shot(self, project_id, shot_code):

		from aau_site import sg

		# project_id = 147
		# shot_code = 'SQ05_SH16'

		shot = sg.find('Shot', [
					['project','is',{'type':'Project','id': project_id}],
					['code', 'is', shot_code]],
					['code', 'assets', 'sg_no__of_frames'])[0]

		characters = [asset['name'] for asset in shot['assets']]
		

		return shot

	# Set maya timeline corespondin with Duration value specified on SG
	def set_frame_range(self, *args):

		shot = self.find_shot(147, self.context()['shot_code'])

		frame_number = shot['sg_no__of_frames']

		cmds.playbackOptions(minTime='0', maxTime=frame_number)

		return frame_number

	# Importa main light rig
	def import_light(self, *args):

		lightScenePath = '%s/%s' % (self.project_path, 
									self.lightStr)

		objects = utils.reference(lightScenePath)

		if objects:
			# Assign tag
			utils.set_tag(objects, 'light')

		 
	def import_cam(self, *args):

		sequence = self.context()['sequence']
		shot = self.context()['shot']

		cam_dir = '%s/Assets/Cam/SQ%02d/SH%02d' % (self.project_path,
													sequence,
													shot)

		files = os.listdir(cam_dir)

		for f in files:
			if os.path.splitext(f)[1] == '.fbx':
				cam_path = '%s/%s' % (cam_dir, f)
			else:
				print 'No FBX files found'

		cmd = 'FBXImport -file "%s"' % cam_path

		print 'Executing ', cmd

		maya.mel.eval(cmd)

		# Remove namespaces
		utils.remove_namespaces()


	def import_env(self, *args):

		env_path = '%s/%s' % (self.project_path, self.envStr)

		# Reference the environment file
		objects = utils.reference(env_path)
		
		if objects:
			# Assign tag
			utils.set_tag(objects, 'env')

			# Create render layers
			# utils.create_render_layers()

			# Create render layer and assign imported objects to it
			utils.create_render_layers(['BG'])
			cmds.editRenderLayerMembers('BG', objects)


	def import_abc (self, *args):

		for char, value in self.char_values().items():
			if value:
				maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + self.cache_paths(self.context()['sequence'], self.context()['shot'])[char] + '";')


	def import_geo(self, *args):

		# Create render layers if do not exists
		# utils.create_render_layers()

		for char, value in self.char_values().items():
			if value:
				objects = utils.reference(self.geo_paths()[char])

				# Assign tag
				if objects:
					utils.set_tag(objects, 'char')

					# Create render layer and assign imported objects to it
					utils.create_render_layers(['FG'])
					cmds.editRenderLayerMembers('FG', objects)


	def open_for_edit(self, *args):

		for char, value in self.char_values().items():
			if value:

				char_path = self.geo_paths()[char]

				self.backup_asset(char_path)

				# Open selected maya asset file
				cmds.file(self.geo_paths()[char], open=True, force=True)

	def backup_asset(self, asset_path):

		char_root, char_file_name = os.path.split(asset_path)
		name, ext = os.path.splitext(char_file_name)
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

		print name, 'version', version, 'created in', wip_path

		new_name = '%s_%02d%s' % (name, version, ext)
		new_version_path = '%s/%s' % (wip_path, new_name)
		shutil.copy(asset_path, new_version_path)


	def clean_up_scene ():

		delete_names = ['ikSystem', 'Turtle', 'xgen', 'xgm']
		delete_types = ['mentalray', 'container']

		delete_list = []
		all_nodes = cmds.ls()

		# Append all the nodes that specified in deletion_names
		for node in all_nodes:
			for node_name in delete_names:
				if node.startswith(node_name):
					delete_list.append(node)

			for node_type in delete_types:
				if cmds.nodeType(node).startswith(node_type):
					delete_list.append(node)

		for node in delete_list:
			print node
		do_delete = raw_input("Delete?")

		if do_delete:
			# Delete node tha in delete_list
			for node in delete_list:
				try:
					cmds.lockNode(node, lock=False)
					cmds.delete(node)
					print node, 'Deleted'
				except:
					print node, 'Can not be deleted'
					pass


	def configure_layers(self, *args):

		mate_shaders = self.cwd + '/Scripts/shot_builder/lib/shadow_layer_mtl.ma'

		scene_references = cmds.ls(references=True)

		# Reference shader file
		utils.reference(mate_shaders)

		# Create render layers if not exist
		utils.create_render_layers(['FG', 'BG', 'SHD', 'zDepth'])

		##### FG START #####
		fg_layer_name = 'FG'
		# Configure vray render elements
		self.enable_element(fg_layer_name, {'char': True, 'env': False})
		# List all object with 'char' tag attribute
		fg_objects = utils.list_by_tag('char', type='transform')
		# Move to FG layer
		cmds.editRenderLayerMembers(fg_layer_name, utils.get_roots(fg_objects), noRecurse=True)
		##### FG END #####


		##### BG START #####
		bg_layer_name = 'BG'
		self.enable_element(bg_layer_name, {'char': False, 'env': True})
		bg_objects = utils.list_by_tag('env', type='transform')
		cmds.editRenderLayerMembers(bg_layer_name, utils.get_roots(bg_objects), noRecurse=True)
		##### BG END #####
		

		##### SHD START #####
		shadow_layer_name = 'SHD'
		# Move to foreground and background objects to SHD layer
		cmds.editRenderLayerMembers(shadow_layer_name, utils.get_roots(fg_objects), noRecurse=True)
		cmds.editRenderLayerMembers(shadow_layer_name, utils.get_roots(bg_objects), noRecurse=True)

		# Set currendt layer to SHD
		cmds.editRenderLayerGlobals(currentRenderLayer=shadow_layer_name)

		# Assign matte material to foreground objects
		for node in fg_objects:
			cmds.select(node)
			cmds.hyperShade(a='matte')
		# Assign vray_wrapper material to background objects
		for node in bg_objects:
			cmds.select(node)
			cmds.hyperShade(a='vray_wrapper')

		# Configure vray render elements
		self.enable_element(shadow_layer_name, {'char': False, 'env': False})
		# Disable all dome lights
		utils.set_layer_attr('VRayLightDomeShape', 'enabled', False, shadow_layer_name)
		##### SHD END #####


		##### zDepth START #####
		zdepth_layer_name = 'zDepth'

 		# Move to foreground and background objects to zDepth layer
		cmds.editRenderLayerMembers(zdepth_layer_name, utils.get_roots(fg_objects), noRecurse=True)
		cmds.editRenderLayerMembers(zdepth_layer_name, utils.get_roots(bg_objects), noRecurse=True)

		# Set currendt layer to zDepth
		cmds.editRenderLayerGlobals(currentRenderLayer='zDepth')

		# Assign matte shader for FG and BG objects
		for node in fg_objects + bg_objects:
			cmds.select(node)
			cmds.hyperShade(a='matte')

		# Configure vray render elements
		self.enable_element(zdepth_layer_name, {'char': False, 'env': False})

		# Create zDepth render element
		zdepth_name = 'vrayRE_Z_depth'
		if not cmds.objExists(zdepth_name):
			maya.mel.eval('vrayAddRenderElement zdepthChannel;')
			cmds.editRenderLayerAdjustment(zdepth_name + ".enabled", layer=zdepth_layer_name)
			cmds.setAttr(zdepth_name + ".enabled", True)
		else:
			print '%s render element already exists' % zdepth_name
		# Disable all dome lights
		utils.set_layer_attr('VRayLightDomeShape', 'enabled', False, zdepth_layer_name)
		##### zDepth END #####


	def configure_render(self, *args):

		sequence = self.context()['sequence']
		shot = self.context()['shot']

		start_frame = cmds.playbackOptions(q=True, minTime=True)
		end_frame = cmds.playbackOptions(q=True, maxTime=True)

		render_output = 'SQ%02d/SH%02d/maya/%%s/<Layer>/%%s' % (sequence, shot)

		## Setting vray settings

		vr_setings_node = 'vraySettings'
		deffailt_settings_node = 'defaultRenderGlobals'
		
		# Render output path
		cmds.setAttr(vr_setings_node + '.fileNamePrefix', render_output, type='string')

		# Output format
		cmds.setAttr(vr_setings_node + '.imageFormatStr', 'exr (multichannel)', type='string')

		# Animation
		cmds.setAttr(deffailt_settings_node + '.animation', True)
		cmds.setAttr(vr_setings_node + '.animBatchOnly', True)

		# Frame range
		cmds.setAttr(deffailt_settings_node + '.startFrame', start_frame)
		cmds.setAttr(deffailt_settings_node + '.endFrame', end_frame)

		# Resolution
		cmds.setAttr(vr_setings_node + ".width", 1920)
		cmds.setAttr(vr_setings_node + ".height", 1080)

		# Global
		cmds.setAttr(vr_setings_node + '.globopt_mtl_limitDepth', True)
		cmds.setAttr(vr_setings_node + '.globopt_mtl_maxDepth', 3)
		cmds.setAttr(vr_setings_node + '.globopt_render_viewport_subdivision', True)

		# DMC Sampler
		cmds.setAttr(vr_setings_node + '.dmcThreshold', 0.01)
		cmds.setAttr(vr_setings_node + '.dmcMaxSubdivs', 6)

		# Camera
		cmds.setAttr(vr_setings_node + '.cam_mbOn', True)

		# VRay UI
		cmds.setAttr(vr_setings_node + '.ui_render_swatches', False)

		# GI
		cmds.setAttr(vr_setings_node + '.giOn', True)
		cmds.setAttr(vr_setings_node + '.primaryEngine', 2)
		cmds.setAttr(vr_setings_node + '.dmc_depth', 1)


		cmds.setAttr(vr_setings_node + '.sys_regsgen_xc', 64)
		cmds.setAttr(vr_setings_node + '.sys_rayc_dynMemLimit', 24000)
		cmds.setAttr(vr_setings_node + '.ddisplac_maxSubdivs', 3)

		# Render elements
		cmds.setAttr(vr_setings_node + '.relements_usereferenced', True)


	def enable_element(self, layer, args):

		# List all render elements
		elements = cmds.ls(type="VRayRenderElement")

		for element in elements:
			for tag, enabled in args.items():
				if cmds.attributeQuery('tag', node=element, exists=True):
					if cmds.getAttr(element + ".tag") == tag:
						print layer, tag, enabled, element
						# Create render layer adjustments 
						# You still need to be on the layer in order to make an ajusment
						cmds.editRenderLayerGlobals(currentRenderLayer=layer)
						cmds.editRenderLayerAdjustment(element + ".enabled", layer=layer)
						cmds.setAttr(element + ".enabled", enabled)
