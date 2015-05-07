import maya.cmds as cmds
import os

# Align two objects
def align():
	obj1, obj2 = cmds.ls(selection=True, o=True)
	objPos = cmds.xform(obj2, q=1, ws=1, rp=1)
	objRot = cmds.xform(obj2, q=1, ro=True)
	cmds.move(objPos[0], objPos[1], objPos[2], obj1, rpr=True)
	cmds.rotate(objRot[0], objRot[1], objRot[2], obj1, r=True)
	cmds.select(obj1)

# Delete history, Freeze transform etc.
def clean_up():
	selection = cmds.ls(selection=True)
	for node in selection:
		cmds.makeIdentity(node, apply=True, t=1, r=1, s=1, n=0)
		cmds.delete(node, ch=True)

# Bunch rename tool	
def rename():
	selection = cmds.ls(selection=True)
	
	msg = cmds.promptDialog(
		title='Rename Object',
		message='Enter Name:',
		button=['OK', 'Cancel'],
		defaultButton='OK',
		cancelButton='Cancel',
		dismissString='Cancel')
		
	if msg == 'OK':
		msgText = cmds.promptDialog(query=True, text=True)

	count = 1
	for node in selection:
		cmds.rename(node, "%s_%03d" %(msgText, count))
		count += 1

# Export to Alembic
def exportToAbc():			
	
	selection = cmds.ls(selection=True, o=True)

	# Build correct path for alembic export
	forExport = ""
	for node in selection:
		root = " -root |%s" %node
		forExport = forExport + root

	# Export Alembic
	cmds.AbcExport(j="-frameRange 1 1 -uvWrite %s -file %s.abc" % (forExport, selection[0]))

# Move pivot to lowest point of geometry
def pivot_to_min():
	selection = cmds.ls(selection=True, o=True)

	for node in selection:
		bbox = cmds.xform(node, q=True, ws=True, bb=True)
		cmds.xform(node, ws=False, piv=((bbox[0]+bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2))

# Extract geometry from hierarchy		
def unparent_all():

	selection = cmds.ls(selection=True, o=True)

	shapesInSelection = cmds.listRelatives(selection, typ="mesh", ad=True, f=True)
	
	for shape in shapesInSelection:
		try:
			ioAttr = cmds.getAttr(shape + ".io")
			if not(ioAttr):
				transformOfShape = cmds.listRelatives(shape, p=True, f=True)
				cmds.parent(transformOfShape, w=True)
		except: pass

# Import Alembic as VRMesh
def importABCasVRMesh():		
	pathPick = cmds.fileDialog()
	path = os.path.split(pathPick)[1]
	name = path.split(".")[0]

	# Export alembic as VRMesh   
	mel.eval('vrayCreateProxyExisting("%s", "geo/%s")' % (name, path))

def distribute(i=True, r=False):
	# i - instance
	# r - replace
	selection = cmds.ls(selection=True, o=True)
	for node in selection[1:]:
		if i:
			inst = cmds.instance(selection[0])
		else:
			inst = cmds.duplicate(selection[0])

		objPos = cmds.xform(node, q=1, ws=1, rp=1)
		objRot = cmds.xform(node, q=1, ro=True)
		cmds.move(objPos[0], objPos[1], objPos[2], inst, rpr=True)
		cmds.rotate(objRot[0], objRot[1], objRot[2], inst, r=True)
		cmds.select(inst)

		if r:
			cmds.delete(node)