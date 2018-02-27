from Song import Song

class Hashtable:
    def __init__(self, size): #The size of the hashtable should be larger than the amount of inserted elements. This way we avoid collusion.
        self.table = [None] * size

    def hashingFunction(self, key):
        keyValue = 0
        for letter in key:
            keyValue = keyValue*32 + ord(letter)
        index = keyValue % len(self.table)
        return index

    def store(self, key, value, listOfCollisions):  # Hashar in värden på rätt plats
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

            else:  #När pekaren inte längre pekar på ett objekt så placeras ett nytt objektet där.
                temporaryCheck.next = value
                collisions += 1
                listOfCollisions.append(collisions)

    def search(self, key):
        index = self.hashingFunction(key)
        if self.table[index] != None:
            if self.table[index].key == key: #Vi kollar om det översta objektet i index är key.
                print(self.table[index].value)

            else: #Nu kollar vi om objektet finns länkat under istället
                temporaryCheck = self.table[index].next
                while self.table[index].next != None:
                     if temporaryCheck.key == key:
                         print(temporaryCheck.value)
                         break
                     else:
                         temporaryCheck = temporaryCheck.next

#  ------------

class HashNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

#  ------------

def readfile(filename):
    songlist = []
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])  # Creates objects from file
            songlist.append(song)
    return songlist

def loadfactor(songlist): #Loadfactor = 0.50 för att få tillräckligt med luft i listan.
    size = int(len(songlist)/0.50)
    return size

def main():
    filename = "unique_tracks.txt"

    songlist = readfile(filename)  # 999 999 för att testa hela filen. Tar lång tid.
    size = loadfactor(songlist)
    dictionary = Hashtable(size) #Skapar min lista som jag kommer hasha in mina sånger i.
    collisions = [] #Förvarar antalet krockar för varje artist i en lista

    for i in range(0, len(songlist)): #Skapar noder och hashar in dem i en lista
        trackid = (songlist[i].trackid)  # sparar undan key
        node = HashNode(trackid, songlist[i], None)  # Varje nod håller i artistnamn, all information om artisten och pekar på nästa nod (krock).
        dictionary.store(node.key, node, collisions)  # [artistname, object, antalet kollisioner]

    print ('Det sker ' + str(len(collisions)) + ' krockar, och som mest vid ett och samma index sker det ' + str(max(collisions)) + ' krockar')

main()
