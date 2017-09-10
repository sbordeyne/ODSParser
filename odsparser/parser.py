class ODSParser():
	def __init__(self, ods_name):
		self.ods_name = ods_name
		self.open()
		pass
	#WITH SHENANIGANS
	def __enter__(self):
		self.open(self)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()
		pass
	#OPEN and CLOSE methods
	def open(self):
		self.odscontent = zipfile.ZipFile(self.ods_name, "r")
		self.content = self.odscontent.open("content.xml")
		self.tree= etree.parse(self.content)
		self.root = self.tree.getroot()
		self.body = ods.root[3]
		self.spreadsheet = body[0]
		self.tables = [t for t in spreadsheet if "}table" in t.tag]
		pass

	def close(self):
		self.content.close()
		self.odscontent.close()
		pass
	#parser for the content.xml in the ods file.
	def parse(self):
		for table in self.tables:
			for column in table:
				print(column.tag, column.attrib)
		pass

	#turns the data into a pandas dataframe
	def to_dataframe(self):
		pass

	#turns the data into a numpy array
	def to_array(self):
		pass
	pass
