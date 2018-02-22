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

