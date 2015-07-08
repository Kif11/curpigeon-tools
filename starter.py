import os
import sys
from cleaner.app import *
from config.curpigeon_template import *
from maya.app import *

user_input = ''

while user_input != 'q':

	user_input = raw_input("->")


	if user_input == 'cleaner':
		
		c = Cleaner(cpTemplate)
		c.project_cleanup()


	elif user_input == 'maya':
		
		m = Maya(cpTemplate)
		m.run()

# Debug
# m = Maya(cpTemplate).run()