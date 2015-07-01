class Template(object):

	def __init__(self):

		# Default instance template settings
		self.sequence_prefix = 'SQ'
		self.shot_prefix = 'SH'
		self.separator = '_'
		self.padding = r'02d'

	# Shot code template constructor
	def get_shot_code_template(self):

		self.shot_code_template = '{sq_pref}{{sq:{pad}}}{sep}{sh_pref}{{sh:{pad}}}'.format(sq_pref=self.sequence_prefix,
																						   sh_pref=self.shot_prefix,
																						   sep=self.separator,
																						   pad=self.padding)

		return self.shot_code_template

	# Construct shot code givent sequence and shot integers
	def shot_code(self, sequence, shot):

		self.get_shot_code_template()
		
		shot_code = self.shot_code_template.format(sq=sequence, sh=shot)

		return shot_code


class Context(Template):

	def __init__(self):

		Template.__init__(self)

	def set_shot_code_template(self, template):
		
		self.shot_code_template = template

	def test(self):
		return self.get_shot_code_template()


# Examples
# t = Template()
# t.sequence_prefix = 'Seq'
# t.shot_prefix = 'Shot'
# t.padding = r'03'

# print t.shot_code(14, 22)
# print t.shot_code_template

c = Context()

print c.test()
