from PySide.QtCore import *
from PySide.QtGui import *

import sys

import maya_engine as me
import aau_site
import context
import ui.main


from maya import OpenMayaUI as omui 
from shiboken import wrapInstance 
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


reload(ui.main)
reload(me)

class MainDialog(MayaQWidgetDockableMixin, QDialog, ui.main.Ui_SB_Form):
	
	def __init__ (self, rootWidget=None, maya_engine=None, *args, **kwargs):

		super(MainDialog, self).__init__(*args, **kwargs) 

		self.maya_engine = maya_engine

		# Destroy this widget when closed.  Otherwise it will stay around
		self.setAttribute(Qt.WA_DeleteOnClose, True)


		# Determine root widget to scan
		if rootWidget != None:
			self.rootWidget = rootWidget
		else:
			mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
			self.rootWidget = wrapInstance(long(mayaMainWindowPtr), QWidget)


		self.setupUi(self)

		shots = aau_site.list_shots(147)

		sh_model = self.shotBOX.model()

		for shot in shots:
			item = QStandardItem(str(shot['code']))
			sh_model.appendRow(item)

		self.connect(self.newSceneBTN, SIGNAL('clicked()'), self.maya_engine.new_scene)
 

	def context(self):

		sh_index = self.shotBOX.currentIndex()
		shot_code = self.shotBOX.itemText(sh_index)

		c = context.Context()
		c.scene_path = shot_code

		return c.get

		
def main():

	ui = MainDialog()
	ui.show()

	return ui

if __name__ == "__main__":
	main()


