from PySide import QtCore, QtGui
import maya.cmds as cmds
import maya.mel as mel
import sys
import smtplib
from datetime import datetime

try:
    cmds.loadPlugin ('vrayformaya', quiet=True)
    cmds.pluginInfo ('vrayformaya', edit=True, autoload=False)
    maya.mel.eval('setAttr -type "string" defaultRenderGlobals.currentRenderer "vray";')
except:
    print 'vRay not installed'



class Ui_Dialog(QtGui.QDialog):

    #CREATE THE VARIABLES
    
    global carrier
    carrier = '@txt.att.net','@vtext.com','@messaging.sprintpcs.com','@tmomail.net', \
              '@mymetropcs.com','@email.uscc.net','@vmobl.com','@mmst5.tracfone.com', \
              '@tmomail.net','@sms.mycricket.com','@messaging.nextel.com', \
              '@message.alltel.com','@ptel.com','@tms.suncom.com','@qwestmp.com', \
              '@pcs.rogers.com', '@fido.ca', '@msg.telus.com' , '@txt.bell.ca' , '@msg.koodomobile.com' , \
              '@text.mtsmobility.com' , '@sms.sasktel.com' , '@txt.bell.ca' , '@vmobile.ca'
    
    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.Tool) #Makes the for a Maya Tool Windows
        Dialog.setEnabled(True)
        Dialog.setFixedSize(230, 473) #Makes the windows with a fixed W/H
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(False)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #Makes windows tool stays on top
        Dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.toolNotificatorFrame = QtGui.QToolBox(Dialog)
        self.toolNotificatorFrame.setGeometry(QtCore.QRect(10, 120, 211, 141))
        self.toolNotificatorFrame.setFrameShape(QtGui.QFrame.Box)
        self.toolNotificatorFrame.setObjectName("toolNotificatorFrame")
        self.notificatorPage = QtGui.QWidget()
        self.notificatorPage.setGeometry(QtCore.QRect(0, 0, 209, 85))
        self.notificatorPage.setObjectName("notificatorPage")
        self.carrierListBox = QtGui.QComboBox(self.notificatorPage)
        self.carrierListBox.setGeometry(QtCore.QRect(110, 0, 91, 20))
        self.carrierListBox.setObjectName("carrierListBox")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")   
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.carrierListBox.addItem("")
        self.phoneCheckbox = QtGui.QCheckBox(self.notificatorPage)
        self.phoneCheckbox.setGeometry(QtCore.QRect(10, 0, 51, 17))
        self.phoneCheckbox.setChecked(False)
        self.phoneCheckbox.setText("")
        self.phoneCheckbox.setObjectName("phoneCheckbox")
        self.emailCheckbox = QtGui.QCheckBox(self.notificatorPage)
        self.emailCheckbox.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.emailCheckbox.setText("")
        self.emailCheckbox.setObjectName("emailCheckbox")
        self.phoneTextBox = QtGui.QLineEdit(self.notificatorPage)
        self.phoneTextBox.setGeometry(QtCore.QRect(30, 0, 81, 20))
        self.phoneTextBox.setObjectName("phoneTextBox")
        self.emailTextBox = QtGui.QLineEdit(self.notificatorPage)
        self.emailTextBox.setGeometry(QtCore.QRect(30, 30, 171, 20))
        self.emailTextBox.setObjectName("emailTextBox")
        self.toolNotificatorFrame.addItem(self.notificatorPage, "")
        self.settingsPage = QtGui.QWidget()
        self.settingsPage.setGeometry(QtCore.QRect(0, 0, 209, 85))
        self.settingsPage.setObjectName("settingsPage")
        self.smtp_label = QtGui.QLabel(self.settingsPage)
        self.smtp_label.setGeometry(QtCore.QRect(-20, 0, 51, 20))
        self.smtp_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.smtp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.smtp_label.setObjectName("smtp_label")
        self.user_label = QtGui.QLabel(self.settingsPage)
        self.user_label.setGeometry(QtCore.QRect(-20, 30, 51, 20))
        self.user_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_label.setObjectName("user_label")
        self.pass_label = QtGui.QLabel(self.settingsPage)
        self.pass_label.setGeometry(QtCore.QRect(-20, 60, 51, 20))
        self.pass_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pass_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pass_label.setObjectName("pass_label")
        self.smtpTextBox = QtGui.QLineEdit(self.settingsPage)
        self.smtpTextBox.setGeometry(QtCore.QRect(40, 0, 121, 20))
        self.smtpTextBox.setObjectName("smtpTextBox")
        self.smtp_portTextBox = QtGui.QLineEdit(self.settingsPage)
        self.smtp_portTextBox.setGeometry(QtCore.QRect(170, 0, 31, 20))
        self.smtp_portTextBox.setObjectName("smtp_portTextBox")
        self.smtp_userTextBox = QtGui.QLineEdit(self.settingsPage)
        self.smtp_userTextBox.setGeometry(QtCore.QRect(40, 30, 161, 20))
        self.smtp_userTextBox.setObjectName("smtp_userTextBox")
        self.smtp_passTextBox = QtGui.QLineEdit(self.settingsPage)
        self.smtp_passTextBox.setGeometry(QtCore.QRect(40, 60, 161, 20))
        self.smtp_passTextBox.setEchoMode(QtGui.QLineEdit.Password)
        self.smtp_passTextBox.setObjectName("smtp_passTextBox")
        self.toolNotificatorFrame.addItem(self.settingsPage, "")
        self.frameMode = QtGui.QFrame(Dialog)
        self.frameMode.setGeometry(QtCore.QRect(10, 30, 211, 71))
        self.frameMode.setFrameShape(QtGui.QFrame.Box)
        self.frameMode.setFrameShadow(QtGui.QFrame.Plain)
        self.frameMode.setObjectName("frameMode")
        self.frameRangeStart = QtGui.QSpinBox(self.frameMode)
        self.frameRangeStart.setGeometry(QtCore.QRect(10, 40, 51, 22))
        self.frameRangeStart.setMinimum(-500)
        self.frameRangeStart.setMaximum(9999)
        self.frameRangeStart.setProperty("value", 0)
        self.frameRangeStart.setObjectName("frameRangeStart")
        self.frameRangeEnd = QtGui.QSpinBox(self.frameMode)
        self.frameRangeEnd.setGeometry(QtCore.QRect(150, 40, 51, 22))
        self.frameRangeEnd.setReadOnly(False)
        self.frameRangeEnd.setMaximum(9999)
        self.frameRangeEnd.setProperty("value", 100)
        self.frameRangeEnd.setObjectName("frameRangeEnd")
        self.methodBatch = QtGui.QRadioButton(self.frameMode)
        self.methodBatch.setGeometry(QtCore.QRect(120, 10, 82, 17))
        self.methodBatch.setChecked(False)
        self.methodBatch.setObjectName("methodBatch")
        self.rangeLabel = QtGui.QLabel(self.frameMode)
        self.rangeLabel.setGeometry(QtCore.QRect(65, 40, 81, 20))
        self.rangeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rangeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rangeLabel.setObjectName("rangeLabel")
        self.methodFrame = QtGui.QRadioButton(self.frameMode)
        self.methodFrame.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.methodFrame.setObjectName("methodFrame")
        self.methodFrame.setChecked(True)
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(120, 440, 101, 23))
        self.startButton.setObjectName("startButton")
        self.outputFrame = QtGui.QFrame(Dialog)
        self.outputFrame.setGeometry(QtCore.QRect(10, 280, 211, 151))
        self.outputFrame.setFrameShape(QtGui.QFrame.Panel)
        self.outputFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.outputFrame.setObjectName("outputFrame")
        self.startTimeLabel = QtGui.QLabel(self.outputFrame)
        self.startTimeLabel.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.startTimeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.startTimeTextBox = QtGui.QLineEdit(self.outputFrame)
        self.startTimeTextBox.setGeometry(QtCore.QRect(130, 10, 71, 20))
        self.startTimeTextBox.setEchoMode(QtGui.QLineEdit.Normal)
        self.startTimeTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.startTimeTextBox.setReadOnly(True)
        self.startTimeTextBox.setObjectName("startTimeTextBox")
        self.endTimeTextBox = QtGui.QLineEdit(self.outputFrame)
        self.endTimeTextBox.setGeometry(QtCore.QRect(130, 40, 71, 20))
        self.endTimeTextBox.setEchoMode(QtGui.QLineEdit.Normal)
        self.endTimeTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.endTimeTextBox.setReadOnly(True)
        self.endTimeTextBox.setObjectName("endTimeTextBox")
        self.endTimeLabel = QtGui.QLabel(self.outputFrame)
        self.endTimeLabel.setGeometry(QtCore.QRect(10, 40, 111, 20))
        self.endTimeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.endTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.endTimeLabel.setObjectName("endTimeLabel")
        self.totalRenderTimeTextBox = QtGui.QLineEdit(self.outputFrame)
        self.totalRenderTimeTextBox.setGeometry(QtCore.QRect(130, 70, 71, 20))
        self.totalRenderTimeTextBox.setEchoMode(QtGui.QLineEdit.Normal)
        self.totalRenderTimeTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.totalRenderTimeTextBox.setReadOnly(True)
        self.totalRenderTimeTextBox.setObjectName("totalRenderTimeTextBox")
        self.totalTimeLabel = QtGui.QLabel(self.outputFrame)
        self.totalTimeLabel.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.totalTimeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.currentTimeLabel = QtGui.QLabel(self.outputFrame)
        self.currentTimeLabel.setGeometry(QtCore.QRect(10, 100, 111, 20))
        self.currentTimeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.currentTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.progressBar = QtGui.QProgressBar(self.outputFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 130, 191, 10))
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.currentFrameTextBox = QtGui.QLineEdit(self.outputFrame)
        self.currentFrameTextBox.setGeometry(QtCore.QRect(130, 100, 41, 20))
        self.currentFrameTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.currentFrameTextBox.setReadOnly(True)
        self.currentFrameTextBox.setObjectName("currentFrameTextBox")
        self.stopButton = QtGui.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(10, 440, 101, 23))
        self.stopButton.setObjectName("stopButton")
        self.frameLabelOne = QtGui.QLabel(Dialog)
        self.frameLabelOne.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.frameLabelOne.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameLabelOne.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frameLabelOne.setObjectName("frameLabelOne")

        self.retranslateUi(Dialog)
        self.toolNotificatorFrame.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.methodFrame, self.methodBatch)
        Dialog.setTabOrder(self.methodBatch, self.phoneCheckbox)
        Dialog.setTabOrder(self.phoneCheckbox, self.emailCheckbox)
        Dialog.setTabOrder(self.emailCheckbox, self.carrierListBox)
        Dialog.setTabOrder(self.carrierListBox, self.startButton)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Render Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(0, QtGui.QApplication.translate("Dialog", "AT&T", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Verizon", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Sprint", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(3, QtGui.QApplication.translate("Dialog", "T-Mobile", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(4, QtGui.QApplication.translate("Dialog", "Metro PCS", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(5, QtGui.QApplication.translate("Dialog", "US Cellular", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Virgin Mobile", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(7, QtGui.QApplication.translate("Dialog", "Trackfone", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(8, QtGui.QApplication.translate("Dialog", "Boost Mobile", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(9, QtGui.QApplication.translate("Dialog", "Cricket", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(10, QtGui.QApplication.translate("Dialog", "Nextel", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(11, QtGui.QApplication.translate("Dialog", "Alltel", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(12, QtGui.QApplication.translate("Dialog", "Ptel", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(13, QtGui.QApplication.translate("Dialog", "Suncom", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(14, QtGui.QApplication.translate("Dialog", "Qwest", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(15, QtGui.QApplication.translate("Dialog", "Rogers", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(16, QtGui.QApplication.translate("Dialog", "Fido", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(17, QtGui.QApplication.translate("Dialog", "Telus", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(18, QtGui.QApplication.translate("Dialog", "Bell", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(19, QtGui.QApplication.translate("Dialog", "Kudi", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(20, QtGui.QApplication.translate("Dialog", "MTS", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(21, QtGui.QApplication.translate("Dialog", "Sasktel", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(22, QtGui.QApplication.translate("Dialog", "Solo", None, QtGui.QApplication.UnicodeUTF8))
        self.carrierListBox.setItemText(23, QtGui.QApplication.translate("Dialog", "Virgin (CA)", None, QtGui.QApplication.UnicodeUTF8))
        self.phoneTextBox.setText(QtGui.QApplication.translate("Dialog", "4155428212", None, QtGui.QApplication.UnicodeUTF8))
        self.emailTextBox.setText(QtGui.QApplication.translate("Dialog", "contact@yasopisso.com", None, QtGui.QApplication.UnicodeUTF8))
        self.toolNotificatorFrame.setItemText(self.toolNotificatorFrame.indexOf(self.notificatorPage), QtGui.QApplication.translate("Dialog", "Notificator", None, QtGui.QApplication.UnicodeUTF8))
        self.smtp_label.setText(QtGui.QApplication.translate("Dialog", "SMTP", None, QtGui.QApplication.UnicodeUTF8))
        self.user_label.setText(QtGui.QApplication.translate("Dialog", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.pass_label.setText(QtGui.QApplication.translate("Dialog", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.smtpTextBox.setText(QtGui.QApplication.translate("Dialog", "smtp.gmail.com", None, QtGui.QApplication.UnicodeUTF8))
        self.smtp_portTextBox.setText(QtGui.QApplication.translate("Dialog", "587", None, QtGui.QApplication.UnicodeUTF8))
        self.smtp_userTextBox.setText(QtGui.QApplication.translate("Dialog", "rendernotificator@gmail.com", None, QtGui.QApplication.UnicodeUTF8))
        self.smtp_passTextBox.setText(QtGui.QApplication.translate("Dialog", "rendermaster00", None, QtGui.QApplication.UnicodeUTF8))
        self.toolNotificatorFrame.setItemText(self.toolNotificatorFrame.indexOf(self.settingsPage), QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.methodBatch.setText(QtGui.QApplication.translate("Dialog", "Single Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeLabel.setText(QtGui.QApplication.translate("Dialog", "<<Start  End>>", None, QtGui.QApplication.UnicodeUTF8))
        self.methodFrame.setText(QtGui.QApplication.translate("Dialog", "Batch Render", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.startTimeLabel.setText(QtGui.QApplication.translate("Dialog", "Start time", None, QtGui.QApplication.UnicodeUTF8))
        self.startTimeTextBox.setText(QtGui.QApplication.translate("Dialog", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.endTimeTextBox.setText(QtGui.QApplication.translate("Dialog", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.endTimeLabel.setText(QtGui.QApplication.translate("Dialog", "End time", None, QtGui.QApplication.UnicodeUTF8))
        self.totalRenderTimeTextBox.setText(QtGui.QApplication.translate("Dialog", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.totalTimeLabel.setText(QtGui.QApplication.translate("Dialog", "Total Render Time", None, QtGui.QApplication.UnicodeUTF8))
        self.currentTimeLabel.setText(QtGui.QApplication.translate("Dialog", "Frames Completed", None, QtGui.QApplication.UnicodeUTF8))
        self.currentFrameTextBox.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.frameLabelOne.setText(QtGui.QApplication.translate("Dialog", "Select render method and frame range", None, QtGui.QApplication.UnicodeUTF8))
        self.createConnections()
      
       
    #Create the connections between buttons and methods
    def createConnections(self):
        
        self.stopButton.clicked.connect(self.stopRender) 
        self.startButton.clicked.connect(self.startRender)
        self.phoneTextBox.textChanged.connect(self.phoneBoxChanged)
        self.phoneCheckbox.clicked.connect(self.prepNotif)
        self.emailCheckbox.clicked.connect(self.prepNotif)
        self.methodFrame.clicked.connect(self.frameBufferMode)
        self.frameRangeStart.valueChanged.connect(self.setFrames)
        self.frameRangeEnd.valueChanged.connect(self.setFrames)
        self.methodBatch.clicked.connect(self.singleMode)
    
    #Method for the Render Button        
    def startRender(self):
        self.prepNotif() #Prepare notifications
        self.createCallBack() #Creates After render Callback
        
        global currentFrame
        currentFrame = self.frameRangeStart.value()
        cmds.currentTime(currentFrame)
  
        
        mel.eval('renderWindowRender redoPreviousRender renderView;')

    #Method for the Stop Button
    def stopRender(self):
        pass
        
    #Method for Phone Text Box changed
    def phoneBoxChanged(self):
        self.prepNotif()
   
    #After Render Callback Method
    def createCallBack(self):       
        
        #Creates the MEL callbacks
        
        global melPostRenderFrame
        melPostRenderFrame = 'python "ui.afterFrameCallBack()";'
    
        global melPreRender
        melPreRender = 'python "ui.preRenderCallBack()";'
          
        global melCall
        melCall = 'python "ui.renderNotif()";'   
       
       
        #Creates the Post Render Callback          
        maya.mel.eval('string $pythonToMel = `python "melCall"`;') #Converts the python String to a Mel one
        maya.mel.eval('setAttr -type "string" defaultRenderGlobals.postMel $pythonToMel;') #Put's the string in the MelCallBack
        
        maya.mel.eval('string $framePost = `python "melPostRenderFrame"`;')
        maya.mel.eval('setAttr -type "string" defaultRenderGlobals.postRenderMel $framePost;')
        
        maya.mel.eval('string $framePre = `python "melPreRender"`;')
        maya.mel.eval('setAttr -type "string" defaultRenderGlobals.preMel $framePre;')
        
        

     
    def prepNotif(self):
        #Prepare variables for notifications (if any)
        global email
        email = self.emailTextBox.text()
        
        global fromaddr
        fromaddr = self.smtp_userTextBox.text()
        
        global username
        username = self.smtp_userTextBox.text()
        
        global SMTP
        SMTP = self.smtpTextBox.text() + ':' + self.smtp_portTextBox.text()
        
        global password
        password = self.smtp_passTextBox.text()
        
        global msg
        msg = 'This is a render test'
        
        
        if (self.phoneCheckbox.isChecked()):
            carrierList = self.carrierListBox.currentIndex()
            phoneSMS = self.phoneTextBox.text() + str(carrier[carrierList])
        else:
            phoneSMS = ''
        
        if (self.emailCheckbox.isChecked()):
            email = self.emailTextBox.text()
        else:
            email = ''
        
        global toaddrs
        toaddrs = [email , phoneSMS]

        global notifStatus
        notifStatus = True
        
        #Check weather notification is needed or not
        if (self.phoneCheckbox.isChecked() or self.emailCheckbox.isChecked()):
            notifStatus = True
        else:
            notifStatus = False 
    
    #Establishes the frame buffer to Render Animation Only
    def frameBufferMode(self):
        self.frameRangeEnd.setEnabled(True)
        maya.mel.eval('setAttr "vraySettings.animBatchOnly" 0;')#Disable Render ani,ation only
        maya.mel.eval('setAttr "defaultRenderGlobals.animation" 1;')#Enable animation in render settings
        maya.mel.eval('setAttr "vraySettings.dontSaveImage" 0;')#Disable don't save images
        self.setFrames()#Establish the frame range
    
    def singleMode(self):
        self.frameRangeEnd.setEnabled(False)
        maya.mel.eval('setAttr "vraySettings.animBatchOnly" 1;')
        
        
   
    #Set start and end frames
    def setFrames(self):
        global startFrame
        startFrame = self.frameRangeStart.value()
        
        global endFrame
        endFrame = self.frameRangeEnd.value()
        
        maya.mel.eval('setAttr "defaultRenderGlobals.startFrame"'+ str(startFrame) +';')
        maya.mel.eval('setAttr "defaultRenderGlobals.endFrame"'+ str(endFrame) +';')

            
    def afterFrameCallBack(self):
        global currentFrame
        #Progress Bar properties  
        self.progressBar.setProperty('minimum',startFrame)
        self.progressBar.setProperty('maximum',endFrame)        
        self.progressBar.setProperty('value',currentFrame)        
        
        #Current Frame property
        self.currentFrameTextBox.setText(str(currentFrame-startFrame))
        
        #global currentFrame
        currentFrame += 1 
        
        
        
    def preRenderCallBack(self):
        cTime = datetime.now().strftime('%I:%M:%S %p')
        self.startTimeTextBox.setText(cTime)
        
        global timeStartAll
        timeStartAll = datetime.now().replace(microsecond=0)

            
    def endTimeValue(self):
        eTime = datetime.now().strftime('%I:%M:%S %p')
        self.endTimeTextBox.setText(eTime)
        
        timeEndAll = datetime.now().replace(microsecond=0)
        renderTimeAll = str (timeEndAll - timeStartAll)
        self.totalRenderTimeTextBox.setText(renderTimeAll)
        
    def renderNotif(self):
        self.endTimeValue()
        
        
        
        
        if (notifStatus):       
            # This does the magic
            server = smtplib.SMTP(SMTP)
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
        else:
            pass   
        
    
try:
    Dialog.close() #Unloads the app if it was already open
except:
    pass
    
    
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show() #Shows the UI
ui.frameBufferMode()


    
