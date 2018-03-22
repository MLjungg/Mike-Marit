class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        output = ''
        node = self.first
        while node != None:
            output += str(node.value)
            node = node.next
        return output

    def enqueue(self, x):
        newNode = Node(x)
        self.length += 1
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def dequeue(self):
        if self.length > 0:
            value = self.first.value
            self.first = self.first.next
            self.length = self.length - 1
            return value

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        return self.first.value
