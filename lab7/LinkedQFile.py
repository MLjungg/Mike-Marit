class HashNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, node):
        self.length += 1
        if self.first == None:
            self.first = node #Finns endast ett kort
            self.last = node
        else:
            self.last.next = node #Det tidigare sista kortet lankar till den nya sista kortet
            self.last = node #Nu blir det sista kortet new