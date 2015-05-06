import random
import maya.cmds as cmds

maxleaves = 7836
rangeInt = int(maxleaves/2)


for i in xrange (0, 3643):
    
    rndName = random.randint(0,maxleaves)
    cmds.select( 'BBB'+ str(rndName), add=True )
    