module namespace funcs = 'com.funcs.music';

declare function funcs:giveSomeInfo($artist_nome) as node()*
{
  <artistas> {
    for $a in doc(concat("musicastop_db/xml_artists_info/artist_info_", $artist_nome,  ".xml"))//similar
    let $name := $a/artist/name
    return $name
 }
</artistas>
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
      </song>
 }
</songs>
};

