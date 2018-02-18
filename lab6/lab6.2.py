class Song:
    def __init__(self, artisttime, artistname, tracklength, year):
        self.artisttime = artisttime
        self.artistname = artistname
        self.tracklength = tracklength
        self.year = year

def readfile(filename):
    songlist = []
    songdict = {}
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split('\t')
            song = Song(song[0], song[1], song[2], song[3])  # Creates objects from file
            songlist.append(song)
            songdict[song.trackid] = song  # The dictionary has trackid as key and the name of the song as value.

    return songlist, songdict

def main():
    filename = 'sang-artist-data.txt'

    thelist, dictionary = readfile(filename)

main()