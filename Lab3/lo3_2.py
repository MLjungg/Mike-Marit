# -*- coding: utf-8 -*-

from bintreefile import Bintree

svenska = Bintree() #Skapa tomt träd med namn svenska
engelska = Bintree()

with open("word3.txt", "r") as svenskfil: #Öppna fil och döp till svenskfil
    for rad in svenskfil: #För varje rad i svenskfil
        ordet = rad.strip() #Skiljer vi på ordet
        #  Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet)
        else:
            svenska.addToTree(ordet)
#svenska.printTree()# in i sökträdet
print("\n")

with open("engelska.txt", "r") as engelskafil: #Öppna fil och döp till svenskfil
    for rad in engelskafil:
        rad = rad.replace('.','').replace('"','').replace('!','').replace(',','').replace("'" , '') #Ta bort onödiga tecken
        for ordet in rad.split(): #Ny rad för varje ord
            if ordet in engelska:
                pass
            else:
                engelska.addToTree(ordet)
                if ordet in svenska: #Jämföra ordet mot svenska ordlistan
                    print ordet

print("\n")