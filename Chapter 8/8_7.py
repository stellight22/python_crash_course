#8-7 album 
"""
write a function called make album that builds a dictionary
describing a music album.
the function should take in an artist name and an album title
and it should return a dictionary containing these two pieces
of information

use the function to make three dictionaries representing
different albums.
print each return value to show that the dictionaries are storing the album information
correctly


"""

def make_album_dict(artist_name, album_title, num_tracks = 0):
    album = {'artist': artist_name, 'album': album_title.title()}
    if num_tracks:
        album['num_tracks']= num_tracks
    return album

kesha = make_album_dict('Drake', 'Scorpion')
keke = make_album_dict('Rihanna', 'good girl gone bad')
kakao = make_album_dict('Michael buble', 'christmas in town')
numi = make_album_dict('Drake', 'Good life', 8)

print(kesha)
print(keke)
print(kakao)
print(numi)
