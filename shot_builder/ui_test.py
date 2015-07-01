from PySide.QtCore import *
from PySide.QtGui import *
import sys
import aau_site
import context

import ui.main as showUI

class MainDialog(QDialog, showUI.Ui_SB_Form):
	
	def __init__ (self, parent=None):

		super(MainDialog, self).__init__(parent) 
		self.setupUi(self)

		shots = aau_site.list_shots(147)

		sh_model = self.shotBOX.model()

		for shot in shots:
			item = QStandardItem(str(shot['code']))
			sh_model.appendRow(item)

		self.connect(self.newSceneBTN, SIGNAL('clicked()'), self.create_new_scene)
		# self.connect(self.envBTN, SIGNAL('clicked()'), self.get_ui_context)


	def context(self):

		sh_index = self.shotBOX.currentIndex()
		shot_code = self.shotBOX.itemText(sh_index)

		c = context.Context()
		c.scene_path = shot_code

		return c.get

	def create_new_scene(self):
		print 'Creating new maya scene', self.context()
		


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()