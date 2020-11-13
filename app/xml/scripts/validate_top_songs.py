from lxml import etree
schemadoc = etree.parse("../xsd/top_songs.xsd")
schema = etree.XMLSchema(schemadoc)
parser = etree.XMLParser(schema=schema)
tree = etree.parse("../top_songs.xml")
schema.assertValid(tree)
