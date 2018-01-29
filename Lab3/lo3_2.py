# -*- coding: utf-8 -*-

from bintreefile import Bintree

svenska = Bintree() #Skapa tomt träd

with open("word3.txt", "r") as svenskfil: #Öppna fil och döp till svenskfil
    for rad in svenskfil: #För varje rad i svenskfil
        ordet = rad.strip() #Skiljer vi på orden
        #print ordet# Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet)
        else:
            svenska.addToTree(ordet)
#svenska.printTree()# in i sökträdet
print("\n")