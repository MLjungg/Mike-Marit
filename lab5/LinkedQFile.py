class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self,x):
        newNode = Node(x)
        self.length += 1
        if self.first == None:
            self.first = newNode #Finns endast ett kort
            self.last = newNode
        else:
            self.last.next = newNode #Det tidigare sista kortet lankar till den nya sista kortet
            self.last = newNode #Nu blir det sista kortet new

    def dequeue(self):
        if self.length > 0:
            value = self.first.value # Save the first cards value for later print
            self.first = self.first.next #Second card is now first
            self.length = self.length - 1
            return value

    def isEmpty(self):
        return self.length == 0
