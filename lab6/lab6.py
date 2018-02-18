# Laboration 6 Del1
import timeit

'''
Förberedelseuppgift:
Vad representerar parametern stmt: The statement you want to test.
Vad representerar parametern number?: Number of executions of the main statement.
Vad är det timeit tar tid på:
Vad skrivs ut av ett anrop av timeit: How long time the statement took to run.

Intressant information:
* Linear= The linear search is used to find an item in a list. The items do not have to be in order. To search for an item, start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.
* Quicksort= In quicksort you choose a pivot and sort the list based on weather its greater or smaller than the pivot - you seperate these two with a "wall". In case the pivot is bigger, you continue to check the next index. If it's smaller, you change place between that index and the value next to the "wall". When you have checked every element you place the pivot next to the wall - it is now in the right position. Timecomplexity is O(nlogn) and in worst case O(n^2).
* Binary = To search for an item, look in the middle of the list and see if the number you want is in the middle, above the middle or below the middle. If it is in the middle, you have found the item. If it is higher than the middle value, then adjust the bottom of the list so that you search in a smaller list starting one above the middle of the list. If the number is lower than the middle value, then adjust the top of the list so that you search in a smaller list which has its highest position one less than the middle position.
'''


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


# Function reads the file and saves the music-content as objects in a list and a dictionary.
def readfile(filename):
    songlist = []
    songdict = {}
    with open(filename, "r") as tracks:
        for line in tracks:  # För varje rad i tracks
            song = line.strip().split("<SEP>")
            song = Song(song[0], song[1], song[2], song[3])  # Creates objects from file
            songlist.append(song)
            songdict[song.trackid] = song  # The dictionary has trackid as key and the name of the song as value.

    return songlist, songdict


# Function for linear searching. Check each element in list and compare.
def linsearch(thelist, testartist):
    for artist in thelist:
        if artist.artistname == testartist:  # Check if artist is found
            return True
    return False  # Artist is not included in list


# Sort the list with quicksort method.
def sorting(thelist):
    quicksort(thelist, 0, len(thelist) - 1)

def quicksort(thelist, first, last):
    if first < last:  #  When you have broken down the list to no more than two elements, it stops the function and goes down in the stack frame (recursion).
        split = quicksortexecution(thelist, first, last) #This breaks down the list into smaller list whom are "sorted" due to pivot.
        quicksort(thelist, first, split - 1)  # Recursive with left side of split
        quicksort(thelist, split + 1, last)  # Recursive with right side of split

def quicksortexecution(thelist, first, last):
    pivotvalue = thelist[first]
    left = first + 1 #This is the first value you compare the pivot with. (left!=first due to pivot=first).
    right = last
    done = 0

    while done == 0:
        # Move the left marker
        while left <= right and thelist[left] <= pivotvalue:
            left = left + 1

        # Move the right marker
        while right >= left and thelist[right] >= pivotvalue:
            right = right - 1

        # If the right is less than left we have two allocated values
        if right < left:
            done = True

        # Swap - Let the left be right and right be left
        else:
            temp = thelist[left]
            thelist[left] = thelist[right]
            thelist[right] = temp

    # You swap the pivot with the index next to the "split/wall". The list is now "sorted".
    temp = thelist[first]
    thelist[first] = thelist[right]
    thelist[right] = temp

    return right  # Return the splitvalue


# Search for value with binary search
def binarysearch(thelist, artist):
    first = 0
    last = len(thelist) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2  # Check the middle
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

    thelist, dictionary = readfile(filename)
    n = len(thelist)
    print("Number of elements =", n)
    last = thelist[n - 1]  # We want to search the whole list
    testartist = last.artistname

    lintime = timeit.timeit(stmt=lambda: linsearch(thelist, testartist), number=1000)
    print("Linesearch took", round(lintime, 4), "seconds")

    # Testcode
    # print(dictionary['TRMMMWA128F426B589']) #should get song tangle of aspens
    # print(thelist[4]) #Expected same result

    # Sort the list with quicksort method + take time
    sortingtime = timeit.timeit(stmt=lambda: sorting(thelist), number=1)
    print("Quicksorting took", round(sortingtime, 4), "seconds")

    # Search with binarysearch + take time
    binarytime = timeit.timeit(stmt=lambda: binarysearch(thelist, testartist), number=1000)
    print("Binarysearch took", round(binarytime, 4), "seconds")

    # Search in dictonary + take time
    dicttime = timeit.timeit(stmt=lambda: searchdict(dictionary, testartist), number=1000)
    print("Searching in dictionary took", round(dicttime, 4), "seconds")

main()
