#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unidecode
from lxml import etree
from urllib.request import urlopen 

import pickle
tree_top_artists = etree.parse("../top_artists.xml")
tree_top_tracks = etree.parse("../top_songs.xml")
tree_top_artistsPT = etree.parse("../top_artistsPT.xml")
tree_top_songsPT = etree.parse("../top_songsPT.xml")

r1 = tree_top_artists.xpath('/lfm/artists/artist/name')
r2 = tree_top_tracks.xpath('/lfm/tracks/track/artist/name')
r3 = tree_top_artistsPT.xpath('/lfm/topartists/artist/name')
r4 = tree_top_songsPT.xpath("/lfm/tracks/track/artist/name")

a1 = [a.text for a in r1]
a2 = [a.text for a in r2]
a3 = [a.text for a in r3]
a4 = [a.text for a in r4]

a_total = list(set(a1 + a2 + a3 + a4))

for i in range(0, len(a_total)-1):
    a_total[i] = unidecode.unidecode(a_total[i].replace(' ', '_'))

with open('array_artists', 'wb') as f:
    pickle.dump(a_total, f)

for n in a_total:
    name_url = unidecode.unidecode(n.replace("_", "+") )   
    name_file =n + ".xml"

    URL_artist_albums = "http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist=" + name_url + "&api_key=46d61d429e1fcddb75d6b42038a671f5"
    URL_artist_tracks = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + name_url + "&api_key=46d61d429e1fcddb75d6b42038a671f5"
    URL_artist_info = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=" + name_url + "&api_key=46d61d429e1fcddb75d6b42038a671f5"
    URL_artist_similar = "http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=" + name_url + "&api_key=46d61d429e1fcddb75d6b42038a671f5"

    print("Fetching artists albums...")
    with open('../xml_artists_albums/artist_albums_' + name_file, 'w', encoding='utf-8') as f:
        f.write(urlopen(URL_artist_albums).read().decode('utf-8'))
    
    print("Fetching artists  tracks... ") 
    with open('../xml_artists_songs/artist_tracks_' + name_file, 'w', encoding='utf-8') as f:
        f.write(urlopen(URL_artist_tracks).read().decode('utf-8'))

    print("Fetching artists infos...")
    with open('../xml_artists_info/artist_info_' + name_file, 'w', encoding='utf-8') as f:
        f.write(urlopen(URL_artist_info).read().decode('utf-8'))
