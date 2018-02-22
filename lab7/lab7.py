from Song import Song

class DictHash:
    def __init__(self):
        self.songdict = {}

    def store(self, key, value):
        self.songdict[key] = value

    def search(self, key):
        try:
            print(self.songdict[key])
        except KeyError:
            print (key + ' finns inte i hashtabellen')

def readfile(filename, dictionary):
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks

            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])  # Creates objects from file
            artistname = song.artistname
            dictionary.store(artistname, song)
    return dictionary

def main():
    filename = "unique_tracks.txt"

    dictionary = DictHash()

    songdict = readfile(filename, dictionary)

    songdict.search('Mikael')
    songdict.search('Maria')

main()