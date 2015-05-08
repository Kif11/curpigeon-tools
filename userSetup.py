import maya.utils as utils
import maya.cmds as cmds
import maya.mel
import shot_builder.app as sb
import kk_tools.app as kk

reload(sb)

# Create custome main menu
def create_menu():

	gMainWindow = maya.mel.eval('$temp1=$gMainWindow')
	oMenu= cmds.menu(parent=gMainWindow, tearOff = True, label = 'Curpigeon')

	# Populate menu with elements
	cmds.menuItem(parent=oMenu, label='Shot Builder', command='sb.App()')

	cmds.menuItem(parent=oMenu, label='TOOLS', divider=True)

	cmds.menuItem(parent=oMenu, label='Align', annotation='Align first selection to second', command='kk.align()')
	cmds.menuItem(parent=oMenu, label='Clean Object', annotation='Delete history and reset transform', command='kk.clean_up()')
	cmds.menuItem(parent=oMenu, label='Rename', annotation='Rename selected objects', command='kk.rename()')
	cmds.menuItem(parent=oMenu, label='Base Pivot', annotation='Set pivot point to the bottom point of selected object', command='kk.pivot_to_min()')
	cmds.menuItem(parent=oMenu, label='Unparent', annotation='Unparet all nested geometry', command='kk.unparent_all()')
	cmds.menuItem(parent=oMenu, label='Distribute', annotation='Distribute first selection on other selected objects', command='kk.distribute()')

# Wait until maya idle when execute create_meny command
utils.executeDeferred(create_menu)