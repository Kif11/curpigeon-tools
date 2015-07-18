import os
import sys
from cleaner.app import *
from config.curpigeon_template import *
from maya_engine.app import *




args = sys.argv


if args[1] == 'cleaner':
	
	c = Cleaner(cpTemplate)
	c.project_cleanup()


elif args[1] == 'maya':
	
	m = Maya(cpTemplate)
	m.run()

else:
	print 'Unknown command'
