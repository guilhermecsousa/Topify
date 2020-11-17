import os
import xmltodict

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from lxml import etree
from projecto.settings import BASE_DIR
from io import StringIO, BytesIO
from urllib.request import urlopen , Request
import feedparser
from django.template.defaulttags import register
from BaseXClient import BaseXClient
import os


def index(request):

    return render(request, 'index.html')


def artistglobal(request):
    os.chdir("app/xml/scripts/")
    os.system(" python3 validate_top_artists.py")
    os.chdir("../../../")
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:giveTopGlobal()" #.format("'BTS'")
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    tparams = {
        "info": xmltodict.parse(res)['artistas']['artist'],
    }
    return render(request, 'artistglobal.html', tparams)


def artistport(request):
    os.chdir("app/xml/scripts/")
    os.system(" python3 validate_top_artistsPT.py")
    os.chdir("../../../")
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:giveTopPortugal()" 
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    tparams = {
        "info": xmltodict.parse(res)['artistas']['artist'],
    }
    return render(request, 'artistport.html', tparams)


def trackglobal(request):
    os.chdir("app/xml/scripts/")
    os.system(" python3 validate_top_songs.py")
    os.chdir("../../../")
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:giveTopSongsGlobal()"
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    tparams = {
        "info": xmltodict.parse(res)['songs']['song'],
    }
    return render(request, 'trackglobal.html', tparams)


def trackport(request):
    os.chdir("app/xml/scripts/")
    os.system(" python3 validate_top_songsPT.py")
    os.chdir("../../../")
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:giveTopSongsPT()" 
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    tparams = {
        "info": xmltodict.parse(res)['songs']['song'],
    }
    return render(request, 'trackport.html', tparams)


def artist(request):

    return render(request, 'artist.html')


def favorites(request):
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    
    return render(request, 'favorites.html')


def news(request):
    response_billboard = urlopen(Request('https://www.billboard.com/feed/', headers={'User-Agent' : 'Mozilla/5.0'})).read().decode('utf-8')
    tree = etree.fromstring(response_billboard.encode('utf-8'))
    link = tree.xpath("/rss/channel/link")
    elem = tree.xpath("/rss/channel/title")
    language = tree.xpath("/rss/channel/language")
    noticias = tree.xpath("/rss/channel/item")
    news_array = [[] ]
    # the namespaces contained in this document
    ns = {'dc': 'http://purl.org/dc/elements/1.1/',
          'content': 'http://purl.org/rss/1.0/modules/content/',
          'media' : 'http://search.yahoo.com/mrss/'}
    #array of news. each article is an array with title, link to the article, publication date, content and image of the article
    for noticia in noticias:
        news_array.append([noticia.find('title').text ,
                           noticia.find('link').text ,
                           noticia.find('pubDate').text ,
                           noticia.find('description', ns).text,
                           noticia.find('media:thumbnail', ns).xpath("@url")[0]])
    tparams = {
        'news': news_array,
    }
    return render(request, 'news.html', tparams) 



