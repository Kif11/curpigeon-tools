import shutil
import os

nuke_master_path = os.getcwd() + '/Scenes/Master/nuke/CP_Master.nk'

invalid = True

# Ask user for file destination until his path is valid
while invalid:

	# Grab copy destination from user
	destination_path = raw_input('Select where you would like to copy your nuke scene: ')
	
	if os.path.exists(destination_path):
		shutil.copy(nuke_master_path, destination_path)
		print 'Nuke scene copied to', destination_path
		invalid = False
	else:
		print 'Path is not valid'
		invalid = True


# End of the program
raw_input('Press any key to finish.')

g:
        
        
