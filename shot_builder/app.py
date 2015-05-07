import maya.cmds as cmds
import maya.mel
import os.path
import utils

# Reload for debug purposes
# reload(utils)

class App(object):

    def __init__(self):


        scene_path = cmds.file(q=True, sceneName=True)
        self.sequence, self.shot = utils.extract_context(scene_path)

        # Try to retrive the current sequence and shot from the filename
        scene_path = cmds.file(q=True, sceneName=True)
        self.sequence, self.shot = utils.extract_context(scene_path)

        if self.sequence <= 0:
            self.sequence, self.shot = '', ''

        # Project path
        #self.projectPathTxt = '//netapp/collab/tbertino_Curpigeon_/Curpigeon_Project/'
        cwd = os.getcwd()
        self.projectPathTxt = cwd.replace('\\', '/') + '/'

        self.envStr = 'Assets/Env/Master/env.ma'
        self.camStr = 'Assets/Cam/'
        self.lightStr = 'Assets/Env/Light/light.ma'



        #Set Cache Variables
        self.charCacheStr = 'Cache/Anm/CHAR/'

        #Set Pigeon Variables
        rockyPath = 'Assets/Char/Geo/Pigeons/Rocky/GEO_Rocky.ma'
        self.rockyFull = self.projectPathTxt + rockyPath

        boxyPath = 'Assets/Char/Geo/Pigeons/Boxy/GEO_Boxy.ma'
        self.boxyFull = self.projectPathTxt + boxyPath  

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

        # Initilize UI
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

        cmds.button(label='FRANGE', w=40, command=self.set_frame_range)
        cmds.button(label='GOTO SG', w=40, command=self.goto_sg)

        cmds.button(label='ENV', w=40, command=self.import_env)
        cmds.button(label='CAM', w=60, command=self.import_cam)
        cmds.button(label='LIGHT', w=60, command=self.import_light)



        cmds.button(label='GEO', w=60, h=40, command=self.import_geo)
        cmds.button(label='ABC', w=60, command=self.import_abc)

        cmds.showWindow(flWin)

    def context(self):
        sequence = cmds.textField(self.stringSQ, q=True, text=True )
        shot = cmds.textField(self.stringSH, q=True, text=True )
        shot_code = 'SQ' + sequence + '_' + 'SH' + shot
        return {'sequence': sequence,
                'shot': shot, 
                'shot_code': shot_code}

    def goto_sg(self, *args):

        shot = self.find_shot(147, self.context()['shot_code'])

        curpigeon_url = 'https://aau.shotgunstudio.com/page/6503'

        shot_url = '%s#Shot_%s_%s' %(curpigeon_url, 
                                    shot['id'],
                                    shot['code'])

        cmd = 'start chrome %s' %shot_url

        os.system(cmd)


    def find_shot(self, project_id, shot_code):

        from aau_site import sg

        # project_id = 147
        # shot_code = 'SQ05_SH16'

        shot = sg.find('Shot', [
                    ['project','is',{'type':'Project','id': project_id}],
                    ['code', 'is', shot_code]],
                    ['code', 'assets', 'sg_no__of_frames'])[0]

        characters = [asset['name'] for asset in shot['assets']]
        

        return shot

    def set_frame_range(self, *args):

        shot = self.find_shot(147, self.context()['shot_code'])

        frame_number = shot['sg_no__of_frames']

        cmds.playbackOptions(minTime='0', maxTime=frame_number)

        return frame_number

    def import_light(self, *args):
        lightScenePath = self.projectPathTxt + self.lightStr
        cmds.file(lightScenePath, reference=True, defaultNamespace=True)

         
    def import_cam(self, *args):
        camPath = self.projectPathTxt + self.camStr + 'SQ' + self.context()['sequence'] + '/' + 'SH' + self.context()['shot'] + '/' + 'SQ' + self.context()['sequence'] + '_' + 'SH' + self.context()['shot'] + '_CAM.fbx'

        melCmd = 'FBXImport -file "%s"' %camPath

        maya.mel.eval(melCmd)

        # Remove namespaces
        utils.remove_namespaces()

    def import_env(self, *args):

        envScenePath = self.projectPathTxt + self.envStr

        # # Import the ENV file ABSOLETE
        # cmds.file( envScenePath, i=True, f=True )

        # Reference the environment file
        cmds.file(envScenePath, reference=True, defaultNamespace=True)

    # Import ABC funtions
    def import_abc (self, *args):

        seqValue = cmds.textField(self.stringSQ, q=True, text=True )
        shotValue = cmds.textField(self.stringSH, q=True, text=True )
        
        # Set Variables
        projectPath = cmds.workspace(q=True, rd=True)
        abcPath = self.projectPathTxt + self.charCacheStr + 'SQ' + seqValue + '/' + 'SH' + self.context()['shot'] + '/' + 'SQ' + seqValue + '_' + 'SH' + self.context()['shot']
        
        
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
    def import_geo(self, *args):
        
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
        
        # PIGEONS
        if (rockyValue):
            # cmds.file( self.rockyFull, i=True )
            cmds.file(self.rockyFull, reference=True, defaultNamespace=True)
            
        if (boxyValue):
            # cmds.file( boxyFull, i=True )
            cmds.file(self.boxyFull, reference=True, defaultNamespace=True)
            
        if (scrawnyyValue):
            # cmds.file( scrawnyFull, i=True )
            cmds.file(self.scrawnyFull, reference=True, defaultNamespace=True)
            
        if (raggedyValue):
            # cmds.file( self.raggedyFull, i=True )
            cmds.file(self.raggedyFull, reference=True, defaultNamespace=True)
            
        if (heavyValue):
            # cmds.file( self.heavyFull, i=True )
            cmds.file(self.heavyFull, reference=True, defaultNamespace=True)
            
        if (longBeakValue):
            # cmds.file( self.longBeakFull, i=True )
            cmds.file(self.longBeakFull, reference=True, defaultNamespace=True)           
            
        # HUMANS
        if (georgeValue):
            # cmds.file( self.georgeFull, i=True )
            cmds.file(self.georgeFull, reference=True, defaultNamespace=True)
            
        if (ernestValue): #Rocky ABC
            # cmds.file( self.ernestFull, i=True )
            cmds.file(self.ernestFull, reference=True, defaultNamespace=True)
            
        if (vincentValue): #Rocky ABC
            # cmds.file( self.vincentFull, i=True )
            cmds.file(self.vincentFull, reference=True, defaultNamespace=True)
            
        if (joeValue): #Rocky ABC
            # cmds.file( self.joeFull, i=True )
            cmds.file(self.joeFull, reference=True, defaultNamespace=True)
            
        if (tomValue): #Rocky ABC
            # cmds.file( self.tomFull, i=True )
            cmds.file(self.tomFull, reference=True, defaultNamespace=True)
            
        if (bobValue): #Rocky ABC
            # cmds.file( self.bobFull, i=True )
            cmds.file(self.bobFull, reference=True, defaultNamespace=True)