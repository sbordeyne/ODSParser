from odsparser import ODSParser

with ODSParser("extract.ods") as ods:
	for child in ods.root:
		if "body" in child.tag:
			spreadsheet = child[0][1]
			print(spreadsheet.attrib)
			for subchild in spreadsheet:
				print(subchild.tag)
	pass
