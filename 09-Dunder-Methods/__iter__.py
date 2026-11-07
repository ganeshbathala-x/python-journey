class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
    def __iter__(self):
        return iter(self.songs)

playlist=Playlist("my favorites")
playlist.add_song("song A")
playlist.add_song("song b")
playlist.add_song("song c")

for song in playlist:
    print(song)