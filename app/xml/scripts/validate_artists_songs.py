from lxml import etree
import pickle

schemadoc = etree.parse("../xsd/artist_tracks_.xsd")
schema = etree.XMLSchema(schemadoc)
parser = etree.XMLParser(schema=schema)

my_list = []

with open('array_artists', 'rb') as f:
    my_list = pickle.load(f)

for aname in my_list:
    print("validating" + aname +"...")  
    tree = etree.parse("../xml_artists_songs/artist_tracks_" + aname + ".xml")
    schema.assertValid(tree)
