#Laboration 6 Del1
import timeit

class Song:
    def __init__(self, trackid, songid, artistname, songtitle):
        self.trackid = trackid
        self.songid = songid
        self.artistname = artistname
        self.songtitle = songtitle

    def __str__(self):
        return str(self.trackid) + ': ' + str(self.songid) + ': ' + str(self.artistname) + ': ' + str(self.songtitle)

    def __lt__(self, other):
        return self.artistname < other.artistname

def main():
    songlist = []
    songdict = {}
    with open("unique_tracks.txt", "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])      
            songlist.append(song)
            songdict[song.trackid] = song
    print(songdict['TRMMMWA128F426B589']) #Ska få ut hela låten tangle of aspens
    print(songlist[4])
            
print(timeit.timeit(main, number=2 ))
