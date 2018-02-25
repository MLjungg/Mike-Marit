from Song import Song

#TODO: Tror hashfunktionen inte ger en bra spridning. Behöver undersökas.

class DictHash:
    def __init__(self, size): #The size of the hashtable should be larger than the amount of inserted elements. This way we avoid collusion.
        self.table = [None] * size

    def hashingFunction(self, key):
        keyValue = 0
        for letter in key:
            keyValue = keyValue*32 + ord(letter)
        index = keyValue % len(self.table)
        return index

    def store(self, key, value, listOfCollisions):
        index = self.hashingFunction(key)
        collisions = 0

        if self.table[index] == None: #Om platsen i listan är tom.
            self.table[index] = value

        elif self.table[index].next == None: #Om pekaren är tom placeras nästa objekt där. En kollision har inträffat.
            collisions = 1
            listOfCollisions.append(collisions)
            self.table[index].next = value

        else:
            temporaryCheck = self.table[index].next
            while temporaryCheck.next != None: #Så länge pekaren har ett objekt
                collisions += 1
                temporaryCheck = temporaryCheck.next

            else:  #När pekaren inte längre pekar på None placeras objektet där. Returnerar också ett värde på antalet krockar.
                temporaryCheck.next = value
                collisions += 1
                listOfCollisions.append(collisions)

    def search(self, key):
        index = self.hashingFunction(key)
        temporaryCheck = self.table[index].next
        try:
            if self.table[index].key == key: #Vi kollar om det översta objektet i index är key.
                print(self.table[index].value)

            else: #Nu kollar vi om objektet finns länkat under istället
                while self.table[index].next != None:
                     if temporaryCheck.key == key:
                         print(temporaryCheck.value)
                         break
                     else:
                         temporaryCheck = temporaryCheck.next

                else:
                    print(key + ' doesnt exist in list')

        except AttributeError:
            print(key + ' Existerar inte')

#  ------------

class HashNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

#  ------------

def readfile(filename,lines):
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

def loadfactor(songlist):
    size = int(len(songlist)/0.50) #Loadfactor=0.50
    return size

def main():
    filename = "unique_tracks.txt"

    songlist = readfile(filename, 50000)  # 999 999 för att testa hela filen. Tar lång tid.
    size = loadfactor(songlist)
    dictionary = DictHash(size) #Parametern ska bero på längden av songlist.
    collisions = [] #Förvarar antalet krockar för varje artist i en lista

    for i in range(0, len(songlist)): #Skapar noder och hashar in dem i en lista
        artistname = songlist[i].artistname
        node = HashNode(artistname, songlist[i], None) #Varje nod håller i artistnamn, all information om artisten och pekar på nästa nod (krock).
        dictionary.store(node.key, node, collisions)  # [artistname, object]

    dictionary.search('Faster Pussy cat')
    print ('Det sker ' + str(len(collisions)) + ' krockar, och som mest vid ett och samma index sker det ' + str(max(collisions)) + ' krockar')

main()
