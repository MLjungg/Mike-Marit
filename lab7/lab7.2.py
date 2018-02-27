from Song import Song
from LinkedQFile import *

class Hashtable:
    def __init__(self, size): #The size of the hashtable should be larger than the amount of inserted elements. This way we avoid collusion.
        self.table = [None] * size

    def hashingFunction(self, key):
        keyValue = 0
        for letter in key:
            keyValue = keyValue*32 + ord(letter)
        index = keyValue % len(self.table)
        return index

    def store(self, hashnode, collisionCounter):  # Hashar in min hashnode
        index = self.hashingFunction(hashnode.key)

        if self.table[index] == None:
            self.table[index] = LinkedQ()  # skapar en länkadlista på platsen
            self.table[index].enqueue(hashnode)
            return collisionCounter
        else:
            self.table[index].enqueue(hashnode)
            collisionCounter += 1
            return collisionCounter

    def search(self, key):
        index = self.hashingFunction(key)
        if self.table[index] == None:
            raise KeyError(key + ' finns inte i listan')

        elif self.table[index].first.key == key:
                print(self.table[index].first.value)
        else:
            temporaryCheck = self.table[index].first
            while temporaryCheck.next != None:
                try:
                    if temporaryCheck.key == key:
                        print(temporaryCheck.Value)

                    else:
                        temporaryCheck.next = temporaryCheck

                except AttributeError:
                    print(key + 'finns inte i listan')

            else:
                raise KeyError(Key + 'finns inte i listan')

# --------------------------------------------------------------

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

# --------------------------------------------------------------
def main():
    filename = "unique_tracks.txt"

    songlist = readfile(filename)  # 999 999 för att testa hela filen. Tar lång tid.
    size = loadfactor(songlist)
    hashtable = Hashtable(size) #Skapar min lista som jag kommer hasha in mina sånger i.
    collisionCounter = 0
    for i in range(0, len(songlist)): #Skapar noder och hashar in dem i en lista
        trackid = (songlist[i].trackid)  # sparar undan key
        hashnode = HashNode(trackid, songlist[i], None)  # Varje nod håller i trackID, all information om artisten och pekar på nästa nod (krock).
        collisionCounter = hashtable.store(hashnode, collisionCounter)  #Skickar in min hashnode som ska placeras i hashtable

    hashtable.search('TRMMMXI128F4285A3F')
    print('Det sker ' + str(collisionCounter) + ' kollisioner')

main()
