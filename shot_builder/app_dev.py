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
		self.camStr = 'Assets/Cam/'
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

		cmds.button(label='SHD', w=40, command=self.shadow_layer)
		
		cmds.showWindow(flWin)

	# Return curent sequnce and shot number specified in corespondin fields
	def context(self):
		sequence = cmds.textField(self.stringSQ, q=True, text=True )
		shot = cmds.textField(self.stringSH, q=True, text=True )
		shot_code = 'SQ' + sequence + '_' + 'SH' + shot
		return {'sequence': sequence,
				'shot': shot, 
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

				paths[char] = '%s/%s/SQ%s/SH%s/SQ%s_SH%s_%s.abc' % (self.project_path, 
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

		lightScenePath = self.project_path + self.lightStr

		objects = utils.reference(lightScenePath)

		# Assign tag
		utils.set_tag(objects, 'light')

		 
	def import_cam(self, *args):

		camPath = self.project_path + '/' + self.camStr + 'SQ' + self.context()['sequence'] + '/' + 'SH' + self.context()['shot'] + '/' + 'SQ' + self.context()['sequence'] + '_' + 'SH' + self.context()['shot'] + '_CAM.fbx'

		print camPath

		melCmd = 'FBXImport -file "%s"' % camPath

		maya.mel.eval(melCmd)

		# Remove namespaces
		utils.remove_namespaces()


	def import_env(self, *args):

		env_path = '%s/%s' % (self.project_path, self.envStr)

		# Reference the environment file
		objects = utils.reference(env_path)
		
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

		for char, value in self.char_values().items():
			if value:
				objects = utils.reference(self.geo_paths()[char])
				cmds.editRenderLayerMembers('FG', objects)

				# Assign tag
				utils.set_tag(objects, 'char')


	def shadow_layer(self, *args):

		mate_shaders = self.cwd + '/Scripts/shot_builder/lib/shadow_layer_mtl.ma'

		scene_references = cmds.ls(references=True)

		# Import reference if not already exist
		# TODO(kirill): Make it global for all reference import
		ref_in_scene = False
		for node in scene_references:
		    if mate_shaders == cmds.referenceQuery(node, filename=True):
		    	ref_in_scene = True
		
		if not ref_in_scene:
			utils.reference(mate_shaders)

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

		for node in bg_objects:
			cmds.select(node)
			cmds.hyperShade(a='vray_wrapper')


		# all_objects = cmds.ls(type='transform')

		# chars = []
		# for node in all_objects:
		#     if cmds.attributeQuery('tag', node=node, exists=True):
		#         if cmds.getAttr(node + '.tag') == 'char':
		#         	chars.append(node)

		            #cmds.hyperShade(a='test_mat')
