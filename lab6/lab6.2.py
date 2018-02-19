class Song:
    def __init__(self, trackid, artisttime, artistname, tracklength, year):
        self.trackid = trackid
        self.artisttime = artisttime
        self.artistname = artistname
        self.tracklength = tracklength
        self.year = year


def readfile(filename):
    songlist = []
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split('\t')
            print (song)
            song = Song(song[0], song[1], song[2], song[3], song[4])  # Creates objects from file
            songlist.append(song)

    return songlist

# Function for linear searching. Check each element in list and compare.
def linsearch(thelist,n):
    maxlength = Song(0,0,0,0.0,0)
    songdict = {}
    for i in range(0,n-1):
        for song in thelist:
            if song.tracklength > maxlength.tracklength and song not in songdict:  # Check if artist is found
                maxlength = song
        songdict[i] = maxlength
    return songdict


def main():
    filename = 'sang-artist-data.txt'

    thelist = readfile(filename)

    #linsearch(thelist)

main()