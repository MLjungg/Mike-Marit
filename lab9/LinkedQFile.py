class Node: #För att hashanoder behövs det här.
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

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

    def dequeue(self):
        if self.length > 0:
            value = self.first.value # Save the first cards value for later print
            self.first = self.first.next #Second card is now first
            self.length = self.length - 1
            return value

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        return self.first.key
