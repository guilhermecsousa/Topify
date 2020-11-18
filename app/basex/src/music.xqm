module namespace funcs = 'com.funcs.music';

declare function funcs:giveSomeInfo($artist_nome) as node()*
{
    for $a in doc(concat("musicastop_db/xml_artists_info/artist_info_", replace($artist_nome," ", "_"),  ".xml"))/lfm/artist
    return 
       <artista>
         <name>
            {$a/name/text()}
            </name>
          <listeners>
            {$a/stats/listeners/text()}
          </listeners>
          <playcount>
            {$a/stats/playcount/text()}
          </playcount>
          <sobre>
            {$a/bio/summary/text()}
          </sobre>
          <similar>
            {$a/similar/artist//name}
          </similar>
       </artista> 
};

declare function funcs:giveTopGlobal() as node()
{
  <artistas> {
    for $a in doc("musicastop_db/top_artists.xml")//artist
    return
      <artist>
        <name>{$a/name/text()}</name>
        <listeners>{$a/listeners/text()}</listeners>
      </artist>
 }
</artistas>
}; 

declare function funcs:givePlaylist() as element()
{
    for $a in doc("playlist.xml")//playlist
    return
      $a
}; 

declare function funcs:giveTopPortugal() as node()
{
  <artistas> {
    for $a in doc("musicastop_db/top_artistsPT.xml")//artist
    return
      <artist>
        <name>{$a/name/text()}</name>
        <listeners>{$a/listeners/text()}</listeners>
      </artist>
 }
</artistas>
};

declare function funcs:giveTopSongsGlobal() as node()
{
  <songs> {
    for $t in doc("musicastop_db/top_songs.xml")//track
    return
      <song>
        <name>{$t/name/text()}</name>
        <artist>{$t/artist/name/text()}</artist>
        <listeners>{$t/listeners/text()}</listeners>
        <playcount>{$t/playcount/text()}</playcount>
        <mbid>{$t/mbid/text()}</mbid>
      </song>
 }
</songs>
};

declare function funcs:giveTopSongsPT() as node()
{
  <songs> {
    for $t in doc("musicastop_db/top_songsPT.xml")//track
    return
      <song>
        <name>{$t/name/text()}</name>
        <artist>{$t/artist/name/text()}</artist>
        <listeners>{$t/listeners/text()}</listeners>
        <playcount>{$t/playcount/text()}</playcount>
        <mbid>{$t/mbid/text()}</mbid>
      </song>
 }
</songs>
}; 

declare updating function funcs:insertTrack($artist_nome,$track)
{
  let $f := doc(concat("musicastop_db/xml_artists_songs/artist_tracks_", replace($artist_nome, ' ', '_'), ".xml"))//track
  let $playlist := doc("musicastop_db/playlist.xml")
  for $a in $f where $a/name/text() = $track
  return insert node (
    <track>
      <name>{$a/name/text()}</name>
      <listeners> {$a/listeners/text()} </listeners>
      <url> {$a/url/text()} </url>
      <artist>
         <name>{$a/artist/name/text()}</name>
         <url>{$a/artist/url/text()}</url>
       </artist>
    </track>
  ) as first into $playlist
}; 


declare updating function funcs:deleteTrack($artist_name, $track)
{
  let $a := doc("musicastop_db/playlist.xml")//track
  for $e in $a
  return
  for $b in $e where ($b/name/text() = $track or $b/artist/name/text() = $artist_name)
  return delete node $b
};   

declare function funcs:trackFromPlaylist() as node()
{
  <Tracks> {
    for $a in doc("musicastop_db/playlist.xml")//track
    return $a
 } </Tracks> 
};



