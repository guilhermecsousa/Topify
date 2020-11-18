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
import re
from django.shortcuts import redirect

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

    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input2 = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:trackFromPlaylist()"
        query2 = session.query(input2)
        res2 = query2.execute()
        query2.close()
    finally:
        if session:
            session.close()

    song = dict()
    song2 = dict()

    song = xmltodict.parse(res)['songs']['song']
    if res2 != None and res2 != '' and res2 != "<tracks/>":
        song2 = xmltodict.parse(res2)['tracks']['track']
        print(song2)
        for s in song:
            try:
                for s2 in song2:
                    print(song2)
                    if s['name']== s2['name'] and s['artist']==s2['artist']['name']:
                        s['in_fav'] = True
                        break
                    else:
                        s['in_fav'] = False
            except:
                if s['name']== song2['name'] and s['artist']==song2['artist']['name']:
                    s['in_fav'] = True
                    break
                else:
                    s['in_fav'] = False
    else:
        for s in song:
            s['in_fav'] = False

    tparams = {
        "info": song,
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
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input2 = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:trackFromPlaylist()"
        query2 = session.query(input2)
        res2 = query2.execute()
        query2.close()
    finally:
        if session:
            session.close()

    song = dict()
    song2 = dict()
    song = xmltodict.parse(res)['songs']['song']
    if res2 != None and res2 != '' and res2 != "<tracks/>":
        song2 = xmltodict.parse(res2)['tracks']['track']
        for s in song:
            try:
                for s2 in song2:
                    print(song2)
                    if s['name']== s2['name'] and s['artist']==s2['artist']['name']:
                        s['in_fav'] = True
                        break
                    else:
                        s['in_fav'] = False
            except:
                if s['name']== song2['name'] and s['artist']==song2['artist']['name']:
                    s['in_fav'] = True
                    break
                else:
                    s['in_fav'] = False

    else:
        for s in song:
            s['in_fav'] = False
    tparams = {
        "info": song,
    }

    return render(request, 'trackport.html', tparams)


def artist(request):

    return render(request, 'artist.html')


def favorites(request):
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = "import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:trackFromPlaylist()"
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    dictionary = dict()
    boolwean = False 
    is_only_one = False
    if res != None and res != '' and res != "<tracks/>":
        dictionary = xmltodict.parse(res)['tracks']['track']
        try:
            for s in dictionary:
                print(s['name'])
                print("ola")
        except:
            print(dictionary)            
            print("Adeus, ola2")
            is_only_one = True
        boolwean = True
    tparams = {
            "info" : dictionary,
            "is_info" : boolwean,
            "is_only_one" : is_only_one
    } 
    return render (request, 'favorites.html',tparams)


def fav_add(request):
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin') 
    artist = request.GET['artist']
    song = request.GET['song']
    print(artist)
    print(song)
    try:
        input = """import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:insertTrack("{}", "{}")""".format(artist, song) 
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    if request.GET['type'] == 'trackpt':
        return redirect('/trackport')
    if request.GET['type'] == 'favorites':
        return redirect('/favorites')
    return redirect('/trackglobal') 

def fav_remove(request): 
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    try:
        input = """import module namespace funcs='com.funcs.music' at 'music.xqm'; funcs:deleteTrack("{}", "{}")""".format(request.GET['song'], request.GET['artist']) 
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    if request.GET['type'] == 'trackpt':
        return redirect('/trackport')
    if request.GET['type'] == 'favorites':
        return redirect('/favorites')
    return redirect('/trackglobal')

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
                           re.compile(r'<[^>]+>').sub('', noticia.find('description', ns).text),
                           noticia.find('media:thumbnail', ns).xpath("@url")[0]])
    tparams = {
        'news': news_array,
    }
    return render(request, 'news.html', tparams) 
