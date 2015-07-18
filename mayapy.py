# import os
# import sys

# os.environ["MAYA_LOCATION"] = "C:/Program Files/Autodesk/Maya2015"
# os.environ["PATH"] += os.pathsep + "C:/Program Files/Autodesk/Maya2015/bin"
# sys.path.append("C:\Program Files\Autodesk\Maya2015\Python\lib\site-packages")

# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\setuptools-0.6c9-py2.6.egg")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\pymel-1.0.0-py2.6.egg")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\ipython-0.10.1-py2.6.egg")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages\ply-3.3-py2.6.egg")                         
# sys.path.append("C:\Program Files\Autodesk\Maya2014\\bin\python26.zip")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\DLLs")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\plat-win")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\lib-tk")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\\bin")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python")
# sys.path.append("C:\Program Files\Autodesk\Maya2014\Python\lib\site-packages")

# # print "Content-Type: text/plain\n\n"
# # for key in os.environ.keys():
# #     print "%30s %s \n" % (key,os.environ[key])

# os.environ["TEMP"] = "D:/"


import maya.standalone

maya.standalone.initialize()

# import maya.cmds as cmds

import pymel.core as pm



# os._exit(0)

pm.openFile('D:/test.ma')

print pm.ls()

# import maya.cmds as cmds

# cmds.file('D:/test.ma', open=1)

# print cmds.ls()
