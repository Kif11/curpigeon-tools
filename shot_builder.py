#Import needed commands
import maya.cmds as cmds
import maya.mel
import os.path

class App(object):

    def __init__(self):

        # Try to retrive the current sequence and shot from the filename
        try:
            import env
            scene_path = cmds.file(q=True, sceneName=True)
            self.sequence, self.shot = env.extract_context(scene_name)
        except:
            print 'Failed to retrive sequence and shot number'
            self.sequence, self.shot = '', ''
            pass

        # Project path
        self.projectPathTxt = '//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/'

        self.envStr = 'Assets/Env/Master/env.ma'

        self.camStr = 'Assets/Cam/'

        #Set Cache Variables
        self.charCacheStr = 'Cache/Anm/CHAR/'

        #Set Pigeon Variables
        rockyPath = 'Assets/Char/Geo/Pigeons/Rocky/GEO_Rocky.ma'
        self.rockyFull = self.projectPathTxt + rockyPath

        boxyPath = 'Assets/Char/Geo/Pigeons/Boxy/GEO_Boxy.ma'
        boxyFull = self.projectPathTxt + boxyPath  

        heavyPath = 'Assets/Char/Geo/Pigeons/Heavy/GEO_Heavy.ma'
        self.heavyFull = self.projectPathTxt + heavyPath  

        longBeakPath = 'Assets/Char/Geo/Pigeons/Longbeak/GEO_Longbeak.ma'
        self.longBeakFull = self.projectPathTxt + longBeakPath  

        raggedyPath = 'Assets/Char/Geo/Pigeons/Raggedy/GEO_Raggedy.ma'
        self.raggedyFull = self.projectPathTxt + raggedyPath  

        scrawnyPath = 'Assets/Char/Geo/Pigeons/Scrawny/GEO_Scrawny.ma'
        scrawnyFull = self.projectPathTxt + scrawnyPath

        #Set Humans Variables
        georgePath = 'Assets/Char/Geo/Humans/George/GEO_George.ma'
        self.georgeFull = self.projectPathTxt + georgePath

        ernestPath = 'Assets/Char/Geo/Humans/Ernest/GEO_Ernest.ma'
        self.ernestFull = self.projectPathTxt + ernestPath

        vincentPath = 'Assets/Char/Geo/Humans/Vincent/GEO_Vincent.ma'
        self.vincentFull = self.projectPathTxt + vincentPath

        joePath = 'Assets/Char/Geo/Humans/Joe/GEO_Joe.ma'
        self.joeFull = self.projectPathTxt + joePath

        tomPath = 'Assets/Char/Geo/Humans/Tom/GEO_Tom.ma'
        self.tomFull = self.projectPathTxt + tomPath

        bobPath = 'Assets/Char/Geo/Humans/Bob/GEO_Bob.ma'
        self.bobFull = self.projectPathTxt + bobPath

        self.ui()

    def ui(self):

        #ESTABLISHES THE UI
        flWin = cmds.window(title="Curpigeon Scene Setup", wh=(378,156), maximizeButton=False, minimizeButton=False, resizeToFitChildren=True)
        cmds.columnLayout(adjustableColumn = True)

        #Characters Imports

        cmds.text(label='')
        cmds.text(label='Project Path' , align = 'left')
        projectPath = cmds.textField(w=100, tx= self.projectPathTxt, editable= False) #Creates the projectPath Variable

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

        self.importRocky = cmds.checkBox(label='Rocky',value=False)
        self.importScrawny = cmds.checkBox(label='Scrawny',value=False)
        self.importRaggedy = cmds.checkBox(label='Raggedy',value=False)
        self.importHeavy = cmds.checkBox(label='Heavy',value=False)
        self.importBoxy = cmds.checkBox(label='Boxy',value=False)
        self.importLBeak = cmds.checkBox(label='L.Beak',value=False)

        self.importGeaorge = cmds.checkBox(label='George',value=False, en= True)
        self.importEarnest = cmds.checkBox(label='Earnest',value=False, en= True)
        self.importVincent = cmds.checkBox(label='Vincent',value=False, en= True)
        self.importJoe = cmds.checkBox(label='Joe',value=False, en= True)
        self.importTom = cmds.checkBox(label='Tom',value=False, en= True)
        self.importBob = cmds.checkBox(label='Bob',value=False, en= True)

        cmds.text(label='')
        cmds.text(label='')
        cmds.text(label='')
        cmds.text(label='')
        cmds.text(label='')
        cmds.text(label='')

        cmds.button(label='ENV', w=40, command=self.importENV)
        cmds.button(label='CAM', w=60, command=self.importCAM)

        cmds.text(label='')
        cmds.text(label='')

        cmds.button(label='GEO', w=60, h=40, command=self.importGEO)
        cmds.button(label='ABC', w=60, command=self.importABC)

        cmds.showWindow(flWin)


    def importCAM(self, *args):
        print 'Importing CAM'
        seqValue = cmds.textField(self.stringSQ, q=True, text=True )
        shotValue = cmds.textField(self.stringSH, q=True, text=True )
        camPath = self.projectPathTxt + self.camStr + 'SQ' + seqValue + '/' + 'SH' + shotValue + '/' + 'SQ' + seqValue + '_' + 'SH' + shotValue + '_CAM.fbx'
        print camPath

        # TODO(Kirill): Need to figure out how to get rid of namespaces.

        melCmd = 'FBXImport -file "%s"' %camPath

        print melCmd

        maya.mel.eval(melCmd)

    def importENV(self, *args):

        envScenePath = self.projectPathTxt + self.envStr

        # Import the ENV file
        cmds.file( envScenePath, i=True, f=True )

    # Import ABC funtions
    def importABC (self, *args):

        seqValue = cmds.textField(self.stringSQ, q=True, text=True )
        shotValue = cmds.textField(self.stringSH, q=True, text=True )
        
        # Set Variables
        projectPath = cmds.workspace(q=True, rd=True)
        abcPath = self.projectPathTxt + self.charCacheStr + 'SQ' + seqValue + '/' + 'SH' + shotValue + '/' + 'SQ' + seqValue + '_' + 'SH' + shotValue
        
        
        # Get Values for the Pigeons
        rockyValue = cmds.checkBox(self.importRocky,q=True,value=True )
        boxyValue = cmds.checkBox(self.importBoxy,q=True,value=True )
        scrawnyyValue = cmds.checkBox(self.importScrawny,q=True,value=True )
        raggedyValue = cmds.checkBox(self.importRaggedy,q=True,value=True )
        heavyValue = cmds.checkBox(self.importHeavy,q=True,value=True )
        longBeakValue = cmds.checkBox(self.importLBeak,q=True,value=True )
        
        # Get Values for the Humans
        georgeValue = cmds.checkBox(self.importGeaorge,q=True,value=True )
        ernestValue = cmds.checkBox(self.importEarnest,q=True,value=True )
        vincentValue = cmds.checkBox(self.importVincent,q=True,value=True )
        joeValue = cmds.checkBox(self.importJoe,q=True,value=True )
        tomValue = cmds.checkBox(self.importTom,q=True,value=True )
        bobValue = cmds.checkBox(self.importBob,q=True,value=True )
              
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

    #Import GEO funtions
    def importGEO(self, *args):
        
        #Get Values for the Pigeons
        rockyValue = cmds.checkBox(self.importRocky,q=True,value=True )
        boxyValue = cmds.checkBox(self.importBoxy,q=True,value=True )
        scrawnyyValue = cmds.checkBox(self.importScrawny,q=True,value=True )
        raggedyValue = cmds.checkBox(self.importRaggedy,q=True,value=True )
        heavyValue = cmds.checkBox(self.importHeavy,q=True,value=True )
        longBeakValue = cmds.checkBox(self.importLBeak,q=True,value=True )
        
        #Get Values for the Humans
        georgeValue = cmds.checkBox(self.importGeaorge,q=True,value=True )
        ernestValue = cmds.checkBox(self.importEarnest,q=True,value=True )
        vincentValue = cmds.checkBox(self.importVincent,q=True,value=True )
        joeValue = cmds.checkBox(self.importJoe,q=True,value=True )
        tomValue = cmds.checkBox(self.importTom,q=True,value=True )
        bobValue = cmds.checkBox(self.importBob,q=True,value=True )
        
         #Import Maya Scene (PIGEONS)
        if (rockyValue): #Rocky ABC
            cmds.file( self.rockyFull, i=True )
            
        if (boxyValue): #Rocky ABC
            cmds.file( boxyFull, i=True )
            
        if (scrawnyyValue): #Rocky ABC
            cmds.file( scrawnyFull, i=True )
            
        if (raggedyValue): #Rocky ABC
            cmds.file( self.raggedyFull, i=True )
            
        if (heavyValue): #Rocky ABC
            cmds.file( self.heavyFull, i=True )
            
        if (longBeakValue): #Rocky ABC
            cmds.file( self.longBeakFull, i=True )           
            
         #Import Maya Scene (HUMANS)
        if (georgeValue): #Rocky ABC
            cmds.file( self.georgeFull, i=True )
            
        if (ernestValue): #Rocky ABC
            cmds.file( self.ernestFull, i=True )
            
        if (vincentValue): #Rocky ABC
            cmds.file( self.vincentFull, i=True )
            
        if (joeValue): #Rocky ABC
            cmds.file( self.joeFull, i=True )
            
        if (tomValue): #Rocky ABC
            cmds.file( self.tomFull, i=True )
            
        if (bobValue): #Rocky ABC
            cmds.file( self.bobFull, i=True )

# Will run the  app on import
application = App()