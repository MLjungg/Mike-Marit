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
    
    def __le__(self, other):
        return self.artistname <= other.artistname
    
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

#Function for linear searching 
def linsearch(thelist, testartist):
    for artist in thelist:
        if artist.artistname == testartist: #Check if artist is found
            return True
    return False #Artist is not included in list

#Should sort the list with quicksort method
def sorting(thelist):
    quicksort(thelist, 0, len(thelist)-1)

def quicksort(thelist, first, last):
    if first < last:
        split = quicksortexecution(thelist, first, last)
        quicksort(thelist, first, split-1) #Recursive with left side of split
        quicksort(thelist, split+1, last) #right side
        
def quicksortexecution(thelist, first, last):
    pivotvalue = thelist[first]
    left = first + 1
    right = last
    done = 0
    
    while done == 0:
        #Move the left marker
        while left <= right and thelist[left] <= pivotvalue:
            left = left + 1

        #Move the right marker
        while right >= left and thelist[right] >= pivotvalue:
            right = right - 1

        #If the right is less than left we have two allocated values
        if right < left:
            done = True

        #Let left be right and right be left
        else:
            temp = thelist[left]
            thelist[left] = thelist[right]
            thelist[right] = temp

    #Sort the list with found split
    temp = thelist[first]
    thelist[first] = thelist[right]
    thelist[right] = temp

    return right #Return the splitvalue

#Search for value with binary search
def binarysearch(thelist, artist):
    first = 0
    last = len(thelist)-1
    found = False

    while first <= last and not found:
        middle = (first + last)//2 #Check the middle
        if thelist[middle].artistname == artist:
            found = True 
        else:
            if artist < thelist[middle].artistname:
                last = middle - 1
            else:
                first = middle + 1
    return found

def searchdict(dictionary, element):
    return element in dictionary

def main():
    filename = "unique_tracks.txt"
    # file_del2 = "/info/tilda/sang-artist-data.txt" #Used later in lab

    thelist, dictionary = readfile(filename)
    n = len(thelist)
    print("Number of elements =", n)
    last = thelist[n-1] #We want to search the whole list
    testartist = last.artistname
    

    lintime = timeit.timeit(stmt = lambda: linsearch(thelist, testartist), number = 1000)
    print("Linesearch took", round(lintime, 4) , "seconds")

    #Testcode           
    #print(dictionary['TRMMMWA128F426B589']) #should get song tangle of aspens
    #print(thelist[4]) #Expected same result

    #Sort the list with quicksort method + take time
    sortingtime = timeit.timeit(stmt = lambda: sorting(thelist), number = 1)
    print("Quicksorting took", round(sortingtime, 4) , "seconds")

    #Search with binarysearch + take time
    binarytime = timeit.timeit(stmt = lambda: binarysearch(thelist, testartist), number = 1000)
    print("Binarysearch took", round(binarytime, 4) , "seconds")

    #Search in dictonary + take time
    dicttime = timeit.timeit(stmt = lambda: searchdict(dictionary, testartist), number = 1000)
    print("Searching in dictionary took", round(dicttime, 4) , "seconds")
    
main()
            
#print(timeit.timeit(main, number=2 )) #Test of timeit

