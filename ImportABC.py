#Import needed commands
import maya.cmds as cmds
import maya.mel
import os.path

import logging
logger = logging.getLogger('ftpuploader')

try:
    maya.mel.eval('setProject "//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/";')
    projectPathTxt = cmds.workspace(q=True, rd=True)
except:
    projectPathTxt = 'Curpigeon project not found, connect to the AAU network>>>>>' 
    
    
#Set Project Variables


#Set Cache Variables
cacheStr = 'Cache/Anm/CHAR/'

#Set Pigeon Variables
rockyPath = 'Assets/Char/Geo/Pigeons/Rocky/GEO_Rocky.ma'
rockyFull = projectPathTxt + rockyPath

boxyPath = 'Assets/Char/Geo/Pigeons/Boxy/GEO_Boxy.ma'
boxyFull = projectPathTxt + boxyPath  

heavyPath = 'Assets/Char/Geo/Pigeons/Heavy/GEO_Heavy.ma'
heavyFull = projectPathTxt + heavyPath  

longBeakPath = 'Assets/Char/Geo/Pigeons/Longbeak/GEO_Longbeak.ma'
longBeakFull = projectPathTxt + longBeakPath  

raggedyPath = 'Assets/Char/Geo/Pigeons/Raggedy/GEO_Raggedy.ma'
raggedyFull = projectPathTxt + raggedyPath  

scrawnyPath = 'Assets/Char/Geo/Pigeons/Scrawny/GEO_Scrawny.ma'
scrawnyFull = projectPathTxt + scrawnyPath


#Set Humans Variables
georgePath = 'Assets/Char/Geo/Humans/George/GEO_George.ma'
georgeFull = projectPathTxt + georgePath

ernestPath = 'Assets/Char/Geo/Humans/Ernest/GEO_Ernest.ma'
ernestFull = projectPathTxt + ernestPath

vincentPath = 'Assets/Char/Geo/Humans/Vincent/GEO_Vincent.ma'
vincentFull = projectPathTxt + vincentPath

joePath = 'Assets/Char/Geo/Humans/Joe/GEO_Joe.ma'
joeFull = projectPathTxt + joePath

tomPath = 'Assets/Char/Geo/Humans/Tom/GEO_Tom.ma'
tomFull = projectPathTxt + tomPath

bobPath = 'Assets/Char/Geo/Humans/Bob/GEO_Bob.ma'
bobFull = projectPathTxt + bobPath



####
def openENV():
    #Set Variables
    projectPath = cmds.workspace(q=True, rd=True)
    envStr = 'Assets/Env/_Master_Scene/ENV_Master.ma'
    envScenePath = projectPath + envStr
    cmds.file( envScenePath, f=True, o=True ) #Opens the ENV file


#Import ABC funtions
def importABC ():
    
    #Set Variables
    projectPath = cmds.workspace(q=True, rd=True)
    cacheStr = 'Cache/Anm/CHAR/'
    
    seqValue = cmds.textField(stringSQ, q=True, text=True )
    shotValue = cmds.textField(stringSH, q=True, text=True )
    abcPath = projectPath + cacheStr + 'SQ' + seqValue + '/' + 'SH' + shotValue + '/' + 'SQ' + seqValue + '_' + 'SH' + shotValue
    
    
    #Get Values for the Pigeons
    rockyValue = cmds.checkBox(importRocky,q=True,value=True )
    boxyValue = cmds.checkBox(importBoxy,q=True,value=True )
    scrawnyyValue = cmds.checkBox(importScrawny,q=True,value=True )
    raggedyValue = cmds.checkBox(importRaggedy,q=True,value=True )
    heavyValue = cmds.checkBox(importHeavy,q=True,value=True )
    longBeakValue = cmds.checkBox(importLBeak,q=True,value=True )
    
    #Get Values for the Humans
    georgeValue = cmds.checkBox(importGeaorge,q=True,value=True )
    ernestValue = cmds.checkBox(importEarnest,q=True,value=True )
    vincentValue = cmds.checkBox(importVincent,q=True,value=True )
    joeValue = cmds.checkBox(importJoe,q=True,value=True )
    tomValue = cmds.checkBox(importTom,q=True,value=True )
    bobValue = cmds.checkBox(importBob,q=True,value=True )
          
    if (rockyValue): #Rocky ABC
        #Establish Rocky's ABC path
        abcPathRocky = abcPath + '_Rocky.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathRocky + '";')       
        
    if (boxyValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathBoxy = abcPath + '_Boxy.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathBoxy + '";')   
        
    if (scrawnyyValue): #Scrawny ABC
        #Establish Boxy's ABC path
        abcPathScrawny = abcPath + '_Scrawny.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathScrawny + '";')

    if (raggedyValue): #Raggedy ABC
        #Establish Boxy's ABC path
        abcPathRaggedy = abcPath + '_Raggedy.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathRaggedy + '";')

    if (heavyValue): #heavy ABC
        #Establish Boxy's ABC path
        abcPathHeavy = abcPath + '_Heavy.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathHeavy + '";')
        
    if (longBeakValue): #Longbeak ABC
        #Establish Boxy's ABC path
        abcPathLongbeak = abcPath + '_Longbeak.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathLongbeak + '";')     
        
        ################
    if (georgeValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathGeorge = abcPath + '_George.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathGeorge + '";')    
        
    if (ernestValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathErnest = abcPath + '_Ernest.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathErnest + '";')    
        
    if (vincentValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathVincent = abcPath + '_Vincent.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathVincent + '";')    
        
    if (joeValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathJoe = abcPath + '_Joe.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathJoe + '";')    
        
    if (tomValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathTom = abcPath + '_Tom.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathTom + '";')    
        
    if (bobValue): #Boxy ABC
        #Establish Boxy's ABC path
        abcPathBob = abcPath + '_Bob.abc'
        #Import the cache with a MEL command
        maya.mel.eval('AbcImport -mode import -connect "/"' + '"' + abcPathBob + '";')       

####
#Import GEO funtions
def importGEO():
    
    #Get Values for the Pigeons
    rockyValue = cmds.checkBox(importRocky,q=True,value=True )
    boxyValue = cmds.checkBox(importBoxy,q=True,value=True )
    scrawnyyValue = cmds.checkBox(importScrawny,q=True,value=True )
    raggedyValue = cmds.checkBox(importRaggedy,q=True,value=True )
    heavyValue = cmds.checkBox(importHeavy,q=True,value=True )
    longBeakValue = cmds.checkBox(importLBeak,q=True,value=True )
    
    #Get Values for the Humans
    georgeValue = cmds.checkBox(importGeaorge,q=True,value=True )
    ernestValue = cmds.checkBox(importEarnest,q=True,value=True )
    vincentValue = cmds.checkBox(importVincent,q=True,value=True )
    joeValue = cmds.checkBox(importJoe,q=True,value=True )
    tomValue = cmds.checkBox(importTom,q=True,value=True )
    bobValue = cmds.checkBox(importBob,q=True,value=True )
    
     #Import Maya Scene (PIGEONS)
    if (rockyValue): #Rocky ABC
        cmds.file( rockyFull, i=True )
        
    if (boxyValue): #Rocky ABC
        cmds.file( boxyFull, i=True )
        
    if (scrawnyyValue): #Rocky ABC
        cmds.file( scrawnyFull, i=True )
        
    if (raggedyValue): #Rocky ABC
        cmds.file( raggedyFull, i=True )
        
    if (heavyValue): #Rocky ABC
        cmds.file( heavyFull, i=True )
        
    if (longBeakValue): #Rocky ABC
        cmds.file( longBeakFull, i=True )           
        
     #Import Maya Scene (HUMANS)
    if (georgeValue): #Rocky ABC
        cmds.file( georgeFull, i=True )
        
    if (ernestValue): #Rocky ABC
        cmds.file( ernestFull, i=True )
        
    if (vincentValue): #Rocky ABC
        cmds.file( vincentFull, i=True )
        
    if (joeValue): #Rocky ABC
        cmds.file( joeFull, i=True )
        
    if (tomValue): #Rocky ABC
        cmds.file( tomFull, i=True )
        
    if (bobValue): #Rocky ABC
        cmds.file( bobFull, i=True )
        
#ESTABLISHES THE UI
flWin = cmds.window(title="Curpigeon Scene Setup", wh=(378,156), maximizeButton=False, minimizeButton=False, resizeToFitChildren=True)
cmds.columnLayout(adjustableColumn = True)

#Characters Imports

cmds.text(label='')
cmds.text(label='Project Path' , align = 'left')
projectPath = cmds.textField(w=100, tx= projectPathTxt, editable= False) #Creates the projectPath Variable

cmds.rowColumnLayout( numberOfColumns=6 )

cmds.text(label='')
cmds.text(label='')

#cmds.rowColumnLayout( numberOfRows=1 )

cmds.text( label='SQ', align='right')
stringSQ = cmds.textField(w=20)

cmds.text( label='SH', align='right' )
stringSH = cmds.textField(w=20)

cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

importRocky = cmds.checkBox(label='Rocky',value=False)
importScrawny = cmds.checkBox(label='Scrawny',value=False)
importRaggedy = cmds.checkBox(label='Raggedy',value=False)
importHeavy = cmds.checkBox(label='Heavy',value=False)
importBoxy = cmds.checkBox(label='Boxy',value=False)
importLBeak = cmds.checkBox(label='L.Beak',value=False)

importGeaorge = cmds.checkBox(label='George',value=False, en= True)
importEarnest = cmds.checkBox(label='Earnest',value=False, en= True)
importVincent = cmds.checkBox(label='Vincent',value=False, en= True)
importJoe = cmds.checkBox(label='Joe',value=False, en= True)
importTom = cmds.checkBox(label='Tom',value=False, en= True)
importBob = cmds.checkBox(label='Bob',value=False, en= True)

cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')
cmds.text(label='')

cmds.button(label='ENV', w=40, command='openENV()')
cmds.text(label='')
cmds.text(label='')

cmds.text(label='')
cmds.button(label='GEO', w=60, command='importGEO()')
cmds.button(label='ABC', w=60, command='importABC()')

cmds.showWindow(flWin) 