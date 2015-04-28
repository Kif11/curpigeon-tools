import maya.cmds as cmds
import shutil
import time

now=time

start_time = time.time()
filename = "test5.ma"
path = 'd:/'
cmds.file( rename = path + filename)
cmds.file(s=True, f=True, typ="mayaAscii")


shutil.copy(path+filename,"Z:/Test")
print("--- %s seconds ---for file copy " % (time.time() - start_time))



start_time = time.time()
filename = "test5.ma"
path = 'Z:/Test'
cmds.file( rename = path + filename)
cmds.file(s=True, f=True, typ="mayaAscii")
print("--- %s seconds --- for local save" % (time.time() - start_time))