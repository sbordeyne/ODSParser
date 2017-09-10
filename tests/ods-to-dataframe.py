import zipfile
import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd

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

with ODSParser("extract.ods") as ods:
	for child in ods.root:
		if "body" in child.tag:
			spreadsheet = child[0][1]
			print(spreadsheet.attrib)
			for subchild in spreadsheet:
				print(subchild.tag)
	pass

"""
def indent(elem, level=0):
	i = "\n" + level*"  "
	j = "\n" + (level-1)*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for subelem in elem:
			indent(subelem, level+1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = j
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = j
	return elem

ods_name = "extract.ods"
with zipfile.ZipFile(ods_name, "r") as z:
	with z.open("content.xml", "r") as content:
		tree = ET.fromstringlist(content.readlines())

print(tree)
"""
test = ET.fromstring("""<?xml version="1.0"?>
<data>
	<country name="Liechtenstein">
		<rank>1</rank>
		<year>2008</year>
		<gdppc>141100</gdppc>
		<neighbor name="Austria" direction="E"/>
		<neighbor name="Switzerland" direction="W"/>
	</country>
	<country name="Singapore">
		<rank>4</rank>
		<year>2011</year>
		<gdppc>59900</gdppc>
		<neighbor name="Malaysia" direction="N"/>
	</country>
	<country name="Panama">
		<rank>68</rank>
		<year>2011</year>
		<gdppc>13600</gdppc>
		<neighbor name="Costa Rica" direction="W"/>
		<neighbor name="Colombia" direction="E"/>
	</country>
</data>""")
"""
#for child in test:
#	print(child.tag, child.attrib)
#for child in tree:
#	print(child.tag, child.attrib)

#for cell in tree.findall("text:p"):
#	print(cell.tag, cell.attrib)
indent(tree)
ET.dump(tree)
print(ET)"""
