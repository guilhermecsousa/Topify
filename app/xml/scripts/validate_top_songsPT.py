from lxml import etree
schemadoc = etree.parse("../xsd/top_songsPT.xsd")
schema = etree.XMLSchema(schemadoc)
parser = etree.XMLParser(schema=schema)
tree = etree.parse("../top_songsPT.xml")
schema.assertValid(tree)
