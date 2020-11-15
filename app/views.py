import os

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from lxml import etree
from projecto.settings import BASE_DIR
from io import StringIO, BytesIO
from urllib.request import urlopen , Request
import feedparser
from django.template.defaulttags import register
#schemadoc = etree.parse("top_artists.xsd")
#schema = etree.XMLSchema(schemadoc)
#parser = etree.XMLParser(schema=schema)
#tree = etree.parse("top_artists.xml")
#schema.assertValid(tree)

def index(request):

    return render(request, 'index.html')

def topglobal(request):

    return render(request, 'topglobal.html')

def topport(request):

    return render(request, 'topport.html')

def artist(request):

    return render(request, 'artist.html')

def favorites(request):

    return render(request, 'favorites.html')

def news(request):
    feed = feedparser.parse('https://www.billboard.com/feed/')
    tparams = {
        'news': feed,
    }
    return render(request, 'news.html', tparams) 

# tree = etree.fromstring(response_billboard.encode('utf-8'))
#     link = tree.xpath("/rss/channel/link")
#     elem = tree.xpath("/rss/channel/title")
#     language = tree.xpath("/rss/channel/language")
#     noticias = tree.xpath("/rss/channel/item")
#     news_array = [[]]
#     i = 0
#     # the namespaces contained in this document
#     ns = {'dc': 'http://purl.org/dc/elements/1.1/',
#           'content': 'http://purl.org/rss/1.0/modules/content/',
#           'media' : 'http://search.yahoo.com/mrss/'}
#     # array of news. each article is an array with title, link, publication date, content and image of the article
#     for noticia in noticias:
#         news_array.append([noticia.find('title').text ,
#                            noticia.find('link').text ,
#                            noticia.find('pubDate').text ,
#                            noticia.find('content:encoded', ns).text,
#                            noticia.find('media:thumbnail', ns).xpath("@url")[0]])
#         i = i + 1
#     print(news_array)
#
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)