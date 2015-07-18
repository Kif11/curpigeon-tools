from config.curpigeon_template import *
import os


class NukeCheckout(object):
	
	def __init__(self, template, sequence, shot, user, version=1):


		cpTemplate.sequence = sequence
		cpTemplate.shot = shot
		cpTemplate.user = user
		cpTemplate.version = version


		self.context = cpTemplate.context()


	def nuke_scene_path(self):

		print self.context['shot']

if __name__ == '__main__':

	nc = NukeCheckout(cpTemplate, 1, 2, 'kkirill2')

	nc.nuke_scene_path()