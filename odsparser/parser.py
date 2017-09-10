class ODSParser():
	def __init__(self, ods_name):
		self.ods_name = ods_name
		pass
#WITH SHENANIGANS
	def __enter__(self):
		self.odscontent = zipfile.ZipFile(self.ods_name, "r")
		self.content = self.odscontent.open("content.xml")
		self.tree= etree.parse(self.content)
		self.root = self.tree.getroot()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.content.close()
		self.odscontent.close()
		pass
