class Song:
    def __init__(self, trackid, artistname, songtitle, tracklength, year):
        self.trackid = trackid
        self.artistname = artistname
        self.songtitle = songtitle
        self.tracklength = tracklength
        self.year = year


def readfile(filename):
    songlist = []
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split('\t')
            song = Song(song[0], song[1], song[2], song[3], song[4])  # Creates objects from file
            songlist.append(song)

    return songlist

# Function for linear searching. Check each element in list and compare.
def linsearch(thelist,n):
    maxlength = thelist[0]
    songdict = {}
    for i in range(0,n):
        for song in thelist:
            if song.tracklength > maxlength.tracklength and song not in songdict:  # Check if artist is found
                maxlength = song
        songdict[i] = maxlength
    return songdict

def main():
    filename = 'sang-artist-data.txt'
    thelist = readfile(filename)
    n = int(input('Vilket n för längsta låten?'))
    songdict = linsearch(thelist, n)
    print(songdict[n-1].songtitle)

main()
