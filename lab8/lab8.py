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
    length = 1 #Start at first letter
    while length >= 2
        letter = q.peek()
        
        if letter.isupper and length == 1: #Check if uppercase, if true continue to next letter
            length += 1
            
        elif length == 1:
            raise GrammarError('No upper case: ' + letter)
        
        if letter.isalpha() and letter.islower(): #Check if next is alphabetical and lower case
            length += 1
            
        elif length == 2:
            rasie GrammarError('No lower case ' + letter)

        return
            
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


