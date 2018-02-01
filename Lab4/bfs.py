# -*- coding: utf-8 -*-

from bintreefile import Bintree

svenska = Bintree() #Skapa tomt träd med namn svenska
gamla = Bintree()

#startord = str(input('Ange startord: ')) #Ska den finnas i ordlistan??
#slutord = str(input('Ange slutord: '))

#Läser in fil och skapar ett binärtträd från ordlistan.
with open("word3.txt", "r") as svenskfil:  # Öppna fil och döp till svenskfil
    for rad in svenskfil:  # För varje rad i svenskfil
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.addToTree(ordet)  #Ta bort dubletter i ordlistan

# Skapar kombinationer av startordet utifrån alfabetet
def makechildren(startord):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    startord = list(startord)

    for letter in startord:
        for alfabet_letter in alfabet
            if letter == alfabet_letter:
                print('works')
            else:
                print('doesnt work')
                letter = alfabet_letter
                combination_startord = str(startord)
                kollaord(combination_startord)

# Kollar om ordet finns i den svenska ordlistan samt om bokstavskombinationen förekommit tidigare.
def kollaord(ordet):
    if ordet in svenska:
        if ordet in gamla:
            pass
        else:
            gamla.addToTree(ordet)
            print (ordet)

def test():
    startord='sur'
    makechildren(startord)

test()