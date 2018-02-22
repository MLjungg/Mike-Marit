from Song import Song

#TODO: Ingen krockhantering införd. Dock finns en next-node där man kan koppla det till.

class DictHash:
    def __init__(self, size): #The size of the hashtable should be larger than the amount of inserted elements. This way we avoid collusion.
        self.table = [None] * size

    def hashingFunction(self, key):
        characterValue=[ord(c) for c in key]  # Ascii värde för varje bokstav
        keyValue = sum(characterValue)       # Ascii värde för hela ordet
        index = keyValue % len(self.table)   # Dividerar värdet med längden på listan -> resten blir index.

        return index

    def store(self, key, value):
        self.table[self.hashingFunction(key)] = value

    def search(self, key):
        index = self.hashingFunction(key)
        try:
            print(self.table[index].value)

        except AttributeError:
            print('Existerar inte')

#  ------------

class HashNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

#  ------------

def readfile(filename, lines):
    songlist = []
    iter=0
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            if iter == lines:
                return songlist
            iter += 1
            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])  # Creates objects from file
            songlist.append(song)

def main():
    filename = "unique_tracks.txt"

    songlist = readfile(filename, 5)

    dictionary = DictHash(10) #Parametern ska bero på längden av songlist.

    for i in range(0, len(songlist)): #Skapar noder och hashar in dem i en lista
        artistname = songlist[i].artistname
        node = HashNode(artistname, songlist[i], None) #Varje nod håller i artistnamn, all information om artisten och pekar på nästa nod (krock).
        dictionary.store(node.key, node)  # [artistname, object]

    dictionary.search('Faster Pussy cat')

main()