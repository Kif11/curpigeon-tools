from string import Template


class Template(object):

	def __init__(self):

		# Template settings
		self.sequence_prefix = 'SQ'
		self.shot_prefix = 'SH'
		self.separator = '_'
		self.padding = r'02d'

		# Shot code template constructor
		self.shot_code_template = '{sq_pref}{{sq:{pad}}}{sep}{sh_pref}{{sh:{pad}}}'.format(sq_pref=self.sequence_prefix,
																						   sh_pref=self.shot_prefix,
																						   sep=self.separator,
																						   pad=self.padding)

	# Construct shot code givent sequence and shot integers
	def shot_code(self, sequence, shot):
		
		shot_code = self.shot_code_template.format(sq=sequence, sh=shot)

		return shot_code


t = Template()

# t2 = Template()

print t.sequence_prefix = 'Sa'

print t.shot_code(3, 12)


# print t2.sequence_prefix = 'KK'

# print t2.shot_code(32, 414)