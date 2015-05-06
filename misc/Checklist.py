import maya.cmds as mc

flWin = mc.window(title="Checklist", wh=(210,300))
mc.columnLayout()

mc.text(label='')
mc.text(label='  PLEASE, MAKE SURE YOU COMPLETE')
mc.text(label='  ALL THE STEPS BELOW')
mc.text(label='')
SetProject = mc.checkBox(label='Set your project',value=False)
SetProject = mc.checkBox(label='Import your Maya ENV_Scene',value=False)
SetProject = mc.checkBox(label='Import your Characters',value=False)
SetProject = mc.checkBox(label='Apply your geo cache',value=False)
SetProject = mc.checkBox(label='Add interacting geomerty to FG, SHD',value=False)
SetProject = mc.checkBox(label='Apply Wrap_SHD_ENV to SHD R Layer',value=False)
SetProject = mc.checkBox(label='Apply Wrap_FG_ENV to FG R Layer',value=False)

mc.text(label='')
mc.text(label='  NOW YOUR RENDER SETTINGS')
mc.text(label='')

SetProject = mc.checkBox(label='Set render frames',value=False)
SetProject = mc.checkBox(label='Select your camera',value=False)
SetProject = mc.checkBox(label='Set BG and Master Layer to one frame',value=False)
mc.text(label='      if no moving camera')

mc.showWindow(flWin)