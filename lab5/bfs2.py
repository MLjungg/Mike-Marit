# -*- coding: utf-8 -*-

from LinkedQFile import *
from bintreefile import *
import sys

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()

def makechildren(nod, slutord):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    startord = list(nod.word)

    for i in range(len(startord)):
        for alfabet_letter in alfabet:
            if startord[i] == alfabet_letter:
                pass
            else:
                combination_startord=startord[:] #kopierar lista
                combination_startord[i] = alfabet_letter #Ersätter det index som vi kollar igenom med alfabet_letter
                combination_startord=''.join(combination_startord) #Så man går från list till str
                if combination_startord in svenska and combination_startord not in gamla:
                    child = ParentNode(combination_startord, nod) #Skapar ett barn (objekt) med det nya ordet som pekar på dess parent-word.
                    q.enqueue(child)
                    gamla.addToTree(combination_startord) #Sparar vi tillagda ord
                    if combination_startord == slutord:
                        writechain(child)
                        sys.exit(0)

def writechain(child):
    if child.parent != None:
        writechain(child.parent)
    print(child.word)


def test():
    # Läser in fil och skapar ett binärtträd från ordlistan.
    with open("word3.txt", "r") as svenskfil:  # Öppna fil och döp till svenskfil
        for rad in svenskfil:  # För varje rad i svenskfil
            ordet = rad.strip()
            if ordet in svenska:
                pass  # Ignorera dubletter i ordlistan
            else:
                svenska.addToTree(ordet)

    startord = 'söt'
    slutord = 'sur'

    q.enqueue(ParentNode(startord, None)) #Lägger startordet högst upp i kön

    while not q.isEmpty():
        nod = q.dequeue() #Översta ordet tas bort från kön
        makechildren(nod, slutord) #Det bortagna ordet skickas med som parameter för att skapa dess barn.

    print('Det fanns ingen väg')
    sys.exit(1)

test()

