import os

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from lxml import etree
from projecto.settings import BASE_DIR
from io import StringIO, BytesIO
from urllib.request import urlopen , Request

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

def rss(request):
    response_billboard = urlopen(Request('https://www.billboard.com/feed/', headers={'User-Agent' : 'Mozilla/5.0'})).read().decode('utf-8')
    tree = etree.fromstring(response_billboard.encode('utf-8'))
    link = tree.xpath("/rss/channel/link")
    elem = tree.xpath("/rss/channel/title")
    language = tree.xpath("/rss/channel/language") 
    noticias = tree.xpath("/rss/channel/item")
    news_array = [[] ]
    i = 0
    # the namespaces contained in this document
    ns = {'dc': 'http://purl.org/dc/elements/1.1/',
          'content': 'http://purl.org/rss/1.0/modules/content/', 
          'media' : 'http://search.yahoo.com/mrss/'}
    #array of news. each article is an array with title, link to the article, publication date, content and image of the article
    for noticia in noticias:
        news_array.append([noticia.find('title').text ,
                           noticia.find('link').text ,
                            noticia.find('pubDate').text ,
                           noticia.find('content:encoded', ns).text, 
                           noticia.find('media:thumbnail', ns).xpath("@url")[0]])                     
        i = i + 1
    tparams = {
        'news' : news_array,     
    }
    return render(request, 'newsfeed.html', tparams) 

