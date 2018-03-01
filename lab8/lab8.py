'''<molekyl> ::= <atom> | <atom><num>
<atom>  ::= <LETTER> | <LETTER><letter>
<LETTER>::= A | B | C | ... | Z
<letter>::= a | b | c | ... | z
<num>   ::= 2 | 3 | 4 | ...
'''

from LinkedQFile import *

class GrammarError(Exception):
    pass

#Function for checking if molecule's syntax is correct
def checkMoleculeSyntax():
    checkLetters()
    checkNumbers()

#Function that checks if first letter is uppercase and if containing two that second is lowercase.
def checkLetters(molecule):
    length = 1
    while length >= 2 and q.isEmpty():
        letter = q.peek()

#Function that checks if charachter is an int and bigger than 1.
def checkNumbers():
    return True

#Function that adds a molecule to list
def addMolecule():
    return True

def checkSyntax():
    return True

def main():
    return True

main()


