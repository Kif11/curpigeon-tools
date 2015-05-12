import maya.cmds as cmds
import maya.mel
import os.path
import utils

# Reload for debug purposes
reload(utils)

class App(object):


	def __init__(self):

		self.characters = {
			'Humans' : ['Tom', 'Vincent', 'Joe', 'Bob', 'George', 'Ernest'], 
			'Pigeons': ['Rocky', 'Raggedy', 'Scrawny', 'Longbeak', 'Heavy', 'Boxy']
			 }

		scene_path = cmds.file(q=True, sceneName=True)
		self.sequence, self.shot = utils.extract_context(scene_path)

		# Try to retrive the current sequence and shot from the filename
		scene_path = cmds.file(q=True, sceneName=True)

		# Populate sequence and shot field base on file name
		self.sequence, self.shot = utils.extract_context(scene_path)

		# If utils.extract_context failed set fields empty
		if self.sequence <= 0:
			self.sequence, self.shot = '', ''

		# Project path
		self.cwd = os.getcwd().replace('\\', '/')
		self.project_path = self.cwd.replace('\\', '/')

		self.envStr = 'Assets/Env/Master/env.ma'

		self.lightStr = 'Assets/Env/Light/light.ma'

		# Initilize UI
		self.ui()


	def ui(self):

		#ESTABLISHES THE UI
		flWin = cmds.window(title="Curpigeon Scene Setup", wh=(378,156), maximizeButton=False, minimizeButton=False, resizeToFitChildren=True)
		cmds.columnLayout(adjustableColumn = True)

		#Characters Imports

		cmds.text(label='')
		cmds.text(label='Project Path' , align = 'left')
		projectPath = cmds.textField(w=100, tx= self.project_path, editable= False) #Creates the projectPath Variable

		cmds.rowColumnLayout( numberOfColumns=6 )

		cmds.text(label='')
		cmds.text(label='')

		#cmds.rowColumnLayout( numberOfRows=1 )

		cmds.text( label='SQ', align='right')
		self.stringSQ = cmds.textField(w=20, tx=self.sequence)

		cmds.text( label='SH', align='right' )
		self.stringSH = cmds.textField(w=20, tx=self.shot)

		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')

		self.char_checkboxes = {}
		for kind in self.characters:
			for char in self.characters[kind]:
				self.char_checkboxes[char] = cmds.checkBox(label=char, value=False)

		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')
		cmds.text(label='')

		cmds.button(label='FRANGE', w=40, command=self.set_frame_range)
		cmds.button(label='GOTO SG', w=40, command=self.goto_sg)

		cmds.button(label='ENV', w=40, command=self.import_env)
		cmds.button(label='CAM', w=60, command=self.import_cam)
		cmds.button(label='LIGHT', w=60, command=self.import_light)

		cmds.button(label='GEO', w=60, h=40, command=self.import_geo)
		cmds.button(label='ABC', w=60, command=self.import_abc)

		cmds.button(label='LAYERS', w=40, command=self.configure_layers)
		
		cmds.showWindow(flWin)

	# Return curent sequnce and shot number specified in corespondin fields
	def context(self):
		sequence = cmds.textField(self.stringSQ, q=True, text=True )
		shot = cmds.textField(self.stringSH, q=True, text=True )


		if shot == '' or sequence == '':
			print 'Specify your shot and sequence first'

			# TODO:(kirill) Need to breake here somehow???
			return 0

		shot_code = 'SQ' + sequence + '_' + 'SH' + shot

		return {'sequence': int(sequence),
				'shot': int(shot), 
				'shot_code': shot_code}

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
			utils.create_render_layers()

			# Set render layer
			cmds.editRenderLayerMembers('BG', objects)


	def import_abc (self, *args):

		print self.cache_paths(self.context()['sequence'], self.context()['shot'])

		for char, value in self.char_values().items():
			if value:
				maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + self.cache_paths(self.context()['sequence'], self.context()['shot'])[char] + '";')


	def import_geo(self, *args):

		# Configure render settings
		self.configure_render()

		# Create render layers if do not exists
		utils.create_render_layers()

		for char, value in self.char_values().items():
			if value:
				objects = utils.reference(self.geo_paths()[char])

				# Assign tag
				if objects:
					utils.set_tag(objects, 'char')
					cmds.editRenderLayerMembers('FG', objects)


	def configure_layers(self, *args):

		mate_shaders = self.cwd + '/Scripts/shot_builder/lib/shadow_layer_mtl.ma'

		scene_references = cmds.ls(references=True)

		# Reference shader file
		utils.reference(mate_shaders)

		# Create render layers if do not exists
		utils.create_render_layers()

		##### FG Layer #####
		self.enable_element('FG', {'char': True, 'env': False})

		##### FG Layer #####
		self.enable_element('BG', {'char': False, 'env': True})

		##### SHD Layer #####

		# List of all objects on FG layer
		fg_objects = cmds.editRenderLayerMembers('FG', fullNames=True, query=True)
		# Move to SHD layer
		cmds.editRenderLayerMembers('SHD', fg_objects)

		# Set currendt layer to SHD
		cmds.editRenderLayerGlobals(currentRenderLayer='SHD')

		for node in fg_objects:
			cmds.select(node)
			cmds.hyperShade(a='matte')

		# List of all objects on BG layer
		bg_objects = cmds.editRenderLayerMembers('BG', fullNames=True, query=True)
		# Move to SHD layer
		cmds.editRenderLayerMembers('SHD', bg_objects)
		# Set currendt layer to SHD
		cmds.editRenderLayerGlobals(currentRenderLayer='SHD')

		if bg_objects:
			for node in bg_objects:
				cmds.select(node)
				cmds.hyperShade(a='vray_wrapper')

		self.enable_element('SHD', {'char': False, 'env': False})


		##### zDepth Layer #####

		# List of all objects on master layer
		all_objects = cmds.ls(type='transform')

		# Move to SHD layer
		cmds.editRenderLayerMembers('zDepth', all_objects)

		# Set currendt layer to zDepth
		cmds.editRenderLayerGlobals(currentRenderLayer='zDepth')

		# Assign matte shader for all objects
		for node in all_objects:
			cmds.select(node)
			cmds.hyperShade(a='matte')

		self.enable_element('zDepth', {'char': False, 'env': False})


		# Create zDepth render element
		zdepth_name = 'vrayRE_Z_depth'
		if not cmds.objExists(zdepth_name):
			maya.mel.eval('vrayAddRenderElement zdepthChannel;')
			cmds.editRenderLayerAdjustment(zdepth_name + ".enabled", layer='zDepth')
			cmds.setAttr(zdepth_name + ".enabled", True)
		else:
			print '%s render element already exists' % zdepth_name

		# This is different aproach base on tags
		#
		# all_objects = cmds.ls(type='transform')

		# chars = []
		# for node in all_objects:
		#     if cmds.attributeQuery('tag', node=node, exists=True):
		#         if cmds.getAttr(node + '.tag') == 'char':
		#         	chars.append(node)

		            #cmds.hyperShade(a='test_mat')

	def configure_render(self):

		preset_path = self.cwd + '/Scripts/shot_builder/lib/vray_settings.mel'

		cmds.nodePreset(load=True)

		# http://mayafail.blogspot.com/2010/02/mayapresetpath-is-abortion-of-shame.html

		# vr_settings_node = 'vraySettings'
		# settings = {'width': 1920,
		# 			'height':1080,
		# 			'relements_usereferenced': 1,
		# 			'ddisplac_maxSubdivs': 3
		# 			'giOn': 0
		# 			'dmcMaxSubdivs': 8
		# 			'cam_mbOn': 1
		# 			'imageFormatStr': 6
		# 			'ddisplac_maxSubdivs':
		# 			}

		# for field, value in settings.items():
		# 	cmds.setAttr(vr_settings_node + '.' + field, value)

		# # Set render output path
		# render_output = '%02d_%02d' % (sequence, shot)
		# cmds.setAttr(vr_settings_node + '.fileNamePrefix', render_output, type='string')

	def enable_element(self, layer, args):

		# List all rendet elements
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
