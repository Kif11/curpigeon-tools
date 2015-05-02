import shutil
import re
import os

## Test string
# file_name = 'E:/Projects/Curpigeon bld/shot/SQ05/SH16/scenes/SQ05_SH16_03_KIR.ma'

def extract_context(file_name):

	# Non capturing group to skip special char and spaces (?:)
	# http://stackoverflow.com/questions/13964986/regex-and-the-or-operator-without-grouping-in-python

	p = re.compile(r'(?:/S|\s)*sq(\d*)_sh(\d*)', re.IGNORECASE)
	s = re.match(p, file_name)

	# print s

	sequence = s.group(1)
	shot = s.group(2)

	return sequence, shot

