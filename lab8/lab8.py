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
def checkMoleculeSyntax(molecule):
    checkLetters(molecule)
    checkNumbers(molecule)

#Function that checks if first letter is uppercase and if containing two that second is lowercase.
def checkLetters(molecule):
    length = 1 #Start at first letter
    letter = molecule.peek()
    if letter.isupper and length == 1: #Check if uppercase, if true continue to next letter
        molecule.dequeue()
        length += 1
            
    elif length == 1:
        raise GrammarError('Not upper case: ' + str(letter))

    letter = molecule.peek()
    if letter.isalpha() and letter.islower() and length == 2: #Check if next is alphabetical and lower case
        molecule.dequeue()
        length += 1
            
    elif length == 2:
        raise GrammarError('Not lower case ' + str(letter))

    return
            
#Function that checks if charachter is an int and bigger than 1.
def checkNumbers(molecule):
    while not molecule.isEmpty():
        charachter = molecule.peek()
        try: #Check if it's an int and then execute check bigger than 1
            number = int(charachter) 
            if number > 1:
                molecule.dequeue()
            else:
                raise GrammarError('Not an acceptable number: ' + str(charachter))
        
        except ValueError: #If not an int
            raise GrammarError('Not an integer: ' + str(charachter))

    return

#Function that adds a molecule to list
def addMolecule(molecule):
    moleculeList = list(molecule)
    molecule = LinkedQ()
    for charachter in moleculeList:
        molecule.enqueue(charachter)
    return molecule

def checkSyntax(molecule):
    molecule = addMolecule(molecule)
    try:
        checkMoleculeSyntax(molecule)
        return 'Woop, woop, following the syntax'
    
    except GrammarError as incorrect:
        return str(incorrect)        

def main():
    molecule = "Ch4"
    result = checkSyntax(molecule)
    print(result)
    
main()


