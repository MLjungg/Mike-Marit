# -*- coding: utf-8 -*-

# Klass för noder i träder
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Skapa ett binärt träd

class Bintree:
    def __init__(self):
        self.root = None

    def addToTree(self, value):
        if self.root == None: #Om det inte finns något i trädet skapa en rot till trädet
            self.root = Node(value)
        else:
            self.__add(value, self.root) #Anropa __add för att lägga till i trädet

    def __add(self, value, node):
        if value < node.value:
            if node.left != None: #Om värdet till vänster om noden är None finns det ingen nod där
                self.__add(value, node.left) #Vandrar vidare
            else:
                node.left=Node(value) #Finns ej något till vänster. Nya noden skapas till vänster
        else:
            if node.right != None:
                self.__add(value, node.right)
            else:
                node.right = Node(value)

    def __contains__(self,value):
        if self.root != None: #Om det finns något i trädet
            if self.__finns(value,self.root): #Om funktionen_finns retunerar true ska contains returnera true
                return True
            else:
                return False
        else:
            return False

    def __finns(self, value, node):
        if value == node.value: #Om noden och sökta värdet är samma returnera true
            return True
        elif value < node.value and node.left != None: # Om värdet är mindre än noden och det finns något till vänster
            return self.__finns(value, node.left) #Rekursivt. Sök till vänster
        elif value > node.value and node.right != None: # Om värdet är större än noden och det finns något till höger
            return self.__finns(value, node.right) # Rekursivt. Sök till höger
        else:
            False

    def printTree(self):
        if self.root != None: #Om trädet inte är tom
            self.__showTree(self.root)
        else:
            print ('There is no tree to print out')

    def __showTree(self, node):
        if node != None:
            self.__showTree(node.left)
            print (str(node.value) + ' ')
            self.__showTree(node.right)

def test():
    svenska = Bintree()
    svenska.addToTree('gurka')
    svenska.addToTree('banan')
    svenska.addToTree('ananas')
    svenska.addToTree('hej')
    svenska.addToTree('spela')
    svenska.addToTree('marsipantarta')
    svenska.addToTree('citron')

    #Testkod förvänta else-satsen
'''    if 'bajs' in svenska:
        print('Exist')
    else:
       print ('Something is totally wrong')

    #Förvänta exist
    if 'citron' in svenska:
        print('Exist')
    else:
        print ('Something is totally wrong')'''

    #svenska.printTree()

def main():
    test()

main()