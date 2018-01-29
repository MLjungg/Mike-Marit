# -*- coding: utf-8 -*-

from bintreefile import Bintree

svenska = Bintree() #Skapa tomt träd med namn svenska
engelska = Bintree()

'''with open("word3.txt", "r") as svenskfil: #Öppna fil och döp till svenskfil
    for rad in svenskfil: #För varje rad i svenskfil
        ordet = rad.strip() #Skiljer vi på ordet
        #  Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet)
        else:
            svenska.addToTree(ordet)
#svenska.printTree()# in i sökträdet
print("\n")'''

lista = []
with open("engelska.txt", "r") as engelskafil: #Öppna fil och döp till svenskfil
    for rad in engelskafil: #För varje rad i svenskfil
        for ordet in rad.split():
            lista += ordet
            print ordet #Skiljer vi på ordet

        #  Ett trebokstavsord per rad
        #if ordet in engelska:
         #   print(ordet)
        #else:
         #   engelska.addToTree(ordet)
            #svenska.printTree()# in i sökträdet
print lista
#engelska.printTree()
print("\n")