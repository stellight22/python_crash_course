#make an album dict with while loop

def make_album_dict(artist, album_name):
    album = {'artist': artist, 'album': album_name.title()}
    return album

while True:
    print("Enter artist name: ")
    print("Enter album name: ")
    print("Enter 'q' to quit at any time.")

    artist = input("Enter artist's name: ")
    if artist == 'q':
        break

    album_name = input("Enter album name: ")
    if album_name == 'q':
        break

    album = make_album_dict(artist, album_name)
    print(album)
    

    
    

