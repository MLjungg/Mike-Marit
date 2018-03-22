class HashNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedQ2:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, hashnode):
        self.length += 1
        if self.first == None:
            self.first = hashnode #Finns endast ett kort
            self.last = hashnode
        else:
            self.last.next = hashnode #Det tidigare sista kortet lankar till den nya sista kortet
            self.last = hashnode #Nu blir det sista kortet new