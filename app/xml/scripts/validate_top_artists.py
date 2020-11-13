from lxml import etree
schemadoc = etree.parse("../xsd/top_artists.xsd")
schema = etree.XMLSchema(schemadoc)
parser = etree.XMLParser(schema=schema)
tree = etree.parse("../top_artists.xml")
schema.assertValid(tree)


