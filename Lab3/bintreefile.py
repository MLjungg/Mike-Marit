# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def addToTree(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__add(value, self.root)

    def __add(self, value, node):
        if value < node.value:
            if node.left != None:
                self.__add(value, node.left)
            else:
                node.left=Node(value)
        else:
            if node.right != None:
                self.__add(value, node.right)
            else:
                node.right = Node(value)

    def __contains__(self,value):
        if self.root != None:
            if self.finns(self.root, value):
                return True
            else:
                return False
        else:
            return False

    def finns(self, node, value):
        if value == node.value:
            return True
        elif (value < node.value and node.left != None):
            print (node.value)
            return self.finns(node.left, value)
        elif (value > node.value and node.right != None):
            self.finns(node.right, value)


    def printTree(self):
        if self.root != None:
            self.__showTree(self.root)
        else:
            print ('There is no tree to print out')

    def __showTree(self, node):
        if node != None:
            self.__showTree(node.left)
            print (str(node.value) + ' ')
            self.__showTree(node.right)
        else:
            pass

def test():
    svenska = Bintree()
    svenska.addToTree('gurka')
    svenska.addToTree('banan')
    svenska.addToTree('ananas')
    svenska.addToTree('hej')
    svenska.addToTree('spela')
    svenska.addToTree('marsipantarta')

    if 'hej' in svenska:
        print ('funkar')
    else:
        print ('funkar inte')

#    svenska.addToTree('Citron')


#    if 'gurka' in svenska:
#        print('Exist')
#    else:
#        print ('Somethings is totally wrong')

    svenska.printTree()

def main():
    test()

main()