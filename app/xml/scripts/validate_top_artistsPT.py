from lxml import etree
schemadoc = etree.parse("../xsd/top_artistsPT.xsd")
schema = etree.XMLSchema(schemadoc)
parser = etree.XMLParser(schema=schema)
tree = etree.parse("../top_artistsPT.xml")
schema.assertValid(tree)
