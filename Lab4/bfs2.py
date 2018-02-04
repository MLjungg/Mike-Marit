# -*- coding: utf-8 -*-

from LinkedQFile import *
from bintreefile import *

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()

def makechildren(startord):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    startord = list(startord)

    for i in range(len(startord)):
        for alfabet_letter in alfabet:
            if startord[i] == alfabet_letter:
                pass
            else:
                combination_startord=startord[:] #Så man kopierar lista
                combination_startord[i] = alfabet_letter #Ersätter det index som vi kollar igenom med alfabet_letter
                combination_startord=''.join(combination_startord) #Så man går från list till str
                if combination_startord in svenska and combination_startord not in gamla:
                    q.enqueue(combination_startord)
                    gamla.addToTree(combination_startord) #Sparar vi tillagda ord

def test():
    # Läser in fil och skapar ett binärtträd från ordlistan.
    with open("word3.txt", "r") as svenskfil:  # Öppna fil och döp till svenskfil
        for rad in svenskfil:  # För varje rad i svenskfil
            ordet = rad.strip()
            if ordet in svenska:
                pass  # Ignorera dubletter i ordlistan
            else:
                svenska.addToTree(ordet)

    startord = 'ute'
    slutord = 'hit'
    q.enqueue(startord)
    found = False

    while not q.isEmpty():
        nod = q.dequeue()
        if nod == slutord:
            print ('Hittad!!')
            found = True
            print (nod)
            break
        else:
            makechildren(nod)

    if found == False:
        print('Baajs den fanns inte')

test()

