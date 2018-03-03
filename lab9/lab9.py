from bintreefile import *
from LinkedQFile import *
import sys

# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

'''Ditt program ska läsa formeln tecken för tecken och med rekursiv medåkning kolla syntaxen.
 Rekursiv medåkning innebär att huvudprogrammet först gör anropet readformel(),
 varefter readformel() anropar readmol() som anropar readgroup() och sedan eventuellt sej själv
 (men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck).

 Funktionen readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol() etc - allt enligt grammatiken.
 När ett syntaxbrott upptäcks genereras en exception (raise Syntaxfel("Saknad högerparentes"))
 som fångas i huvudprogrammet och där skrivs hela resten av indataraden ut.'''

#--------------------------------------------------------------------------------------------------

class GrammarError(Exception):
    pass

# Function for checking if molecule's syntax is correct
def readformula(molecule):
    molecule = addMolecule(molecule)
    readmol(molecule)

def readmol(molecule):
    readgroup(molecule)
    if not molecule.isEmpty():
        readmol(molecule)
    else:
        if openlefts > 0:
            raise GrammarError('Saknad högerparentes vid radslutet ' + str(molecule))

def readgroup(molecule):
    if molecule.peek() == '(':
        global openlefts
        openlefts += 1
        molecule.dequeue()
        readmol(molecule)
    elif molecule.peek() == ')':
        if openlefts > 0:
            openlefts -= 1
            molecule.dequeue()
            if molecule.peek().isnumeric():
                readnumbers(molecule)
            else:
                raise GrammarError('Saknad siffra vid radslutet ' + str(molecule)) #+sista delen av molekylen
        else:
            raise GrammarError('Felaktig gruppstart vid radslutet ' + str(molecule)) #+sista delen av molekylen
            
    else:
        readatom(molecule)
        if (not molecule.isEmpty()) and molecule.peek().isnumeric() :
            readnumbers(molecule)

# Function that checks if charachter is an int and bigger than 1.
def readnumbers(molecule):
    firstIteration = 1
    while (not molecule.isEmpty()) and molecule.peek().isnumeric():
        number = int(molecule.dequeue())
        if firstIteration == 1:
            if number == 1:
                if not molecule.isEmpty() and molecule.peek().isnumeric():
                    firstIteration += 1
                else:
                    raise GrammarError('För litet tal vid radslutet ' + str(molecule)) #Glöm ej str-func
            elif number > 1:
                firstIteration += 1
            else:
                raise GrammarError('För litet tal vid radslutet ' + str(molecule)) #Glöm ej str-func

def readatom(molecule):
    firstletter = molecule.peek()
    if not firstletter.isupper():
        raise GrammarError('Saknad stor bokstav vid radslutet ' + str(molecule)) #+radslut
    molecule.dequeue()
    atom = firstletter
    if not molecule.isEmpty():
        secondletter = molecule.peek()
        if secondletter.isalpha() and secondletter.islower():
            molecule.dequeue()
            atom += secondletter

    if not atom in binaryatomlist:
        raise GrammarError('Okänd atom vid radslutet ' + str(molecule)) #+radslut


# Function that adds a molecule to list
def addMolecule(molecule):

    moleculeList = list(molecule)
    molecule = LinkedQ()
    for charachter in moleculeList:
        molecule.enqueue(charachter)
    return molecule

def readfile(file):
    atomlist = []
    with open(file,'r') as atomfile:
        for line in atomfile:
            atom = line.strip().split(' ')
            atomlist = atom
    return atomlist
            
def binarysort(atomlist):
    binaryatomlist = Bintree()
    for atom in atomlist:
        binaryatomlist.addToTree(atom)
    return binaryatomlist
    
def main(molecule):
    filename = 'atoms.txt'
    atomlist = readfile(filename)
    global binaryatomlist
    binaryatomlist = binarysort(atomlist)

    try:
        readformula(molecule)
        print('Formeln är syntaktiskt korrekt')
    except GrammarError as incorrect:
        print(str(incorrect))

    

    
    
    #atomLista= skapaAtomlista()
    #hashtabell = lagraHashtabell(atomLista) #Fungerar hit. Det här kommer behövas för att undersöka om det är en verklig atom.
    #addMolecule(molecule)

    #result = checkSyntax(molecule)
    #print(result)


if __name__ == '__main__':
	for row in sys.stdin:
		row = row.strip()
		if row != "#":
                        openlefts = 0
                        main(row)
		else:
			break


