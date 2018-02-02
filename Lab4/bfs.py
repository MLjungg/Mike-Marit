# -*- coding: utf-8 -*-

import sys

from bintreefile import Bintree

svenska = Bintree() #Skapar tomt träd med namn svenska
gamla = Bintree()

#startord = str(input('Ange startord: ')) #Ska den finnas i ordlistan??
#slutord = str(input('Ange slutord: '))

# Skapar kombinationer av startordet utifrån alfabetet
#TODO: När vi gör om ordet till lista kan det inte å,ä,ö avkodas. Kan göra om det på annat sätt?
def makechildren(startord):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    #print startord
    startord = list(startord)
    #print startord

    for i in range(len(startord)):
        for alfabet_letter in alfabet:
            if startord[i] == alfabet_letter:
                pass

            else:
                combination_startord=startord[:] #Så man kopierar lista
                combination_startord[i] = alfabet_letter #Ersätter det index som vi kollar igenom med alfabet_letter
                combination_startord=''.join(combination_startord) #Så man går från list till str
                kollaord(combination_startord)

# Kollar om ordet finns i den svenska ordlistan samt om bokstavskombinationen förekommit tidigare.
def kollaord(ordet):
    if ordet in svenska:
        if ordet in gamla:
            pass
        else:
            print (ordet)
            gamla.addToTree(ordet)

def test():
    # Läser in fil och skapar ett binärtträd från ordlistan.
    with open("word3.txt", "r") as svenskfil:  # Öppna fil och döp till svenskfil
        for rad in svenskfil:  # För varje rad i svenskfil
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.addToTree(ordet)  # Ta bort dubletter i ordlistan

    startord='söt'
    makechildren(startord)
    

test()