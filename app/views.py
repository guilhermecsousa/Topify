import os

from django.http import Http404
from django.shortcuts import render
from lxml import etree

from projecto.settings import BASE_DIR

#schemadoc = etree.parse("top_artists.xsd")
#schema = etree.XMLSchema(schemadoc)
#parser = etree.XMLParser(schema=schema)
#tree = etree.parse("top_artists.xml")
#schema.assertValid(tree)

def index(request):

    return render(request, 'asd.html')

#    fname = 'top_artists.xml'
#    pname = os.path.join(BASE_DIR, 'app/' + fname)
#    xml = etree.parse(pname)
#    info = dict()
#    artists = xml.xpath('//artista')
#    for a in artists:

#        info['artist'] = a.find('artist')
#        print(info)

#    tparams = {
#        'info' : info,
#    }

 #   return render(request, 'index/#topg.html', tparams)