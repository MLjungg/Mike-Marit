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

def readfile(filename):
    songlist = []
    songdict = {}
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])      
            songlist.append(song)
            songdict[song.trackid] = song
            
    return songlist, songdict

def linsearch(thelist, testartist):
    for artist in thelist:
        if artist.artistname == testartist: #Check if artist is found
            return True
    return False #Artist is not included in list
        
def main():
    filename = "unique_tracks.txt"
    # file_del2 = "/info/tilda/sang-artist-data.txt"

    thelist, dictionary = readfile(filename)
    number_elements = len(thelist)
    print("Number of elements =", number_elements)
    n = number_elements
    last = thelist[n-1] #We want to search the whole list
    testartist = last.artistname

    lintime = timeit.timeit(stmt = lambda: linsearch(thelist, testartist), number = 1000)
    print("Linesearch took", round(lintime, 4) , "seconds")

    #Testcode           
    #print(dictionary['TRMMMWA128F426B589']) #should get song tangle of aspens
    #print(thelist[4]) #Expected same result
    
main()
            
#print(timeit.timeit(main, number=2 )) #Test of timeit

