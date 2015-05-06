import maya.cmds as cmds

def prepNameSpace():
    global nameSpaceArray
    nameSpaceArray = cmds.namespaceInfo(  ":" , listOnlyNamespaces = True)

    #remove internal namespaces from array
    nameSpaceArray.remove('UI')
    nameSpaceArray.remove('shared')
    
    global countNS
    countNS = len(nameSpaceArray)

def nameSpaceRemover():
    
    prepNameSpace()
    
    if (countNS == 0):
        maya.mel.eval('updateNamespaceEditor;')
        print 'Namespaces Clean'
        pass
    else:
        start = 0
        for x in range(0, countNS):
        
            cmds.namespace( removeNamespace = ':'+ nameSpaceArray[start], mergeNamespaceWithRoot = True)
            start += 1
        nameSpaceRemover()
        
nameSpaceRemover()

