from hashAtoms import *

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
def checkMoleculeSyntax(molecule):
    checkLetters(molecule)
    checkNumbers(molecule)

# Function that checks if first letter is uppercase and if containing two that second is lowercase.
def checkLetters(molecule):
    letter = molecule.peek()
    if letter.isupper():  # Check if uppercase, if true continue to next letter
        molecule.dequeue()
    else:
        raise GrammarError('Not upper case: ' + str(letter))

    letter = molecule.peek()
    if letter.isalpha():
        if letter.islower():  # Check if next is alphabetical and lower case
            molecule.dequeue()
        else:
            raise GrammarError('Not lower case: ' + str(letter))

    return

# Function that checks if charachter is an int and bigger than 1.
def checkNumbers(molecule):
    firstIteration = 1
    while not molecule.isEmpty():
        charachter = molecule.peek()
        try:  # Check if it's an int and then execute check bigger than 1
            number = int(charachter)
            if firstIteration == 1:
                if number > 1:
                    firstIteration += 1
                    molecule.dequeue()
                else:
                    raise GrammarError('First number is too small: ' + str(charachter))
            else:
                molecule.dequeue()

        except ValueError:  # If not an int
            raise GrammarError('Not an integer: ' + str(charachter))

    return


# Function that adds a molecule to list
def addMolecule(molecule):

    moleculeList = list(molecule)
    molecule = LinkedQ()
    for charachter in moleculeList:
        node = Node(charachter, None, None)
        molecule.enqueue(node)
    return molecule


def checkSyntax(molecule):
    molecule = addMolecule(molecule)
    try:
        checkMoleculeSyntax(molecule)
        return 'Woop, woop, following the syntax'

    except GrammarError as incorrect:
        return str(incorrect)


def main(molecule):
    atomLista= skapaAtomlista()
    hashtabell = lagraHashtabell(atomLista) #Fungerar hit. Det här kommer behövas för att undersöka om det är en verklig atom.
    addMolecule(molecule)

    #result = checkSyntax(molecule)
    #print(result)


if __name__ == '__main__':
    # for row in sys.stdin:
    #	row = row.strip()

    rowlist = ['Na']
    for row in rowlist:
        if row != "#":
            main(row)
