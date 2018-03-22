from bintreefile import *
from LinkedQFile import *
from molgrafik import *
from hashatoms import *


# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...


class GrammarError(Exception):
    pass


class Ruta:
    def __init__(self, atom="()", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


# Function for checking if molecule's syntax is correct - <mol>
def readformula(molecule):
    molecule = addMolecule(molecule)  # Creates a linkedlist out of the molecule.
    if not molecule.isEmpty():
        mol = readmol(molecule)
    else:
        raise GrammarError('Felaktig gruppstart vid radslutet ' + str(molecule))
    return mol


# Check if our molecule is a molecule - <group> | <group><mol>
def readmol(molecule):
    mol = readgroup(molecule)  # Check group
    if not molecule.isEmpty():
        if mol == None: #If we have a right parenthis we dont create a new "ruta". Hence it doesnt have an mol.next. It is simply None.
            return
        else:
            mol.next = readmol(molecule)  # Check if we have group+mol
    else:
        if openlefts > 0:
            raise GrammarError('Saknad högerparentes vid radslutet ' + str(molecule))
    return mol


# Check if molecule contains of a group
def readgroup(molecule):
    if not molecule.isEmpty():
        global parenthesisNumbers

        if molecule.peek() == '(':  # if we have parenthesis we check: (<mol>)<num>
            ruta = Ruta()
            global openlefts
            openlefts += 1
            molecule.dequeue()
            ruta.down = readmol(molecule)
            ruta.num = parenthesisNumbers
            return ruta
        elif molecule.peek() == ')':  # (<mol>)<num>
            if openlefts > 0:
                openlefts -= 1
                molecule.dequeue()
                if not molecule.isEmpty() and molecule.peek().isnumeric():  # Check number after molecule.
                    parenthesisNumbers = readnumbers(molecule)
                else:
                    raise GrammarError('Saknad siffra vid radslutet ' + str(molecule))
            else:
                raise GrammarError('Felaktig gruppstart vid radslutet ' + str(molecule))

        elif molecule.peek().isalpha():  # <atom> | <atom><num>
            ruta = Ruta()
            ruta.atom = readatom(molecule)
            if not molecule.isEmpty() and molecule.peek().isnumeric():
                ruta.num = readnumbers(molecule)
            return ruta
        else:
            raise GrammarError('Felaktig gruppstart vid radslutet ' + str(molecule))
    else:
        raise GrammarError('Felaktig gruppstart vid radslutet ' + str(molecule))


# Function that checks if charachter is an int and bigger than 1.
def readnumbers(molecule):
    firstIteration = 1
    while not molecule.isEmpty() and molecule.peek().isnumeric():
        number = int(molecule.dequeue())
        if firstIteration == 1:
            if number == 1:
                if not molecule.isEmpty() and molecule.peek().isnumeric():
                    firstIteration += 1
                else:
                    raise GrammarError('För litet tal vid radslutet ' + str(molecule))
            elif number > 1:
                firstIteration += 1
            else:
                raise GrammarError('För litet tal vid radslutet ' + str(molecule))
    return number


# Check if molecule is a correct atom - <LETTER> | <LETTER><letter>
def readatom(molecule):
    firstletter = molecule.peek()
    if not firstletter.isupper():
        raise GrammarError('Saknad stor bokstav vid radslutet ' + str(molecule))
    molecule.dequeue()
    atom = firstletter  # Save for later check in atomlist
    if not molecule.isEmpty():
        secondletter = molecule.peek()
        if secondletter.isalpha() and secondletter.islower():
            molecule.dequeue()
            atom += secondletter

    if not atom in binaryatomlist:
        raise GrammarError('Okänd atom vid radslutet ' + str(molecule))  # +radslut

    return atom


# Function that adds a molecule to list
def addMolecule(molecule):
    moleculeList = list(molecule)
    molecule = LinkedQ()
    for charachter in moleculeList:
        molecule.enqueue(charachter)
    return molecule

def readfile():
    line = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv'
    return line.strip().split(' ')


def binarysort(atomlist):
    binaryatomlist = Bintree()
    for atom in atomlist:
        binaryatomlist.addToTree(atom)
    return binaryatomlist

def weigth(mol):
    atomlista=skapaAtomlista()
    hashtabell=lagraHashtabell(atomlista)
    vikt = 0
    totalvikt= recursiveWeigth(mol, hashtabell, vikt)
    return totalvikt

def recursiveWeigth(mol, hashtabell, vikt):
    if mol.atom == '()':
       tempvikt=recursiveWeigth(mol.down,hashtabell, 0) #Counts one branch
       tempvikt=tempvikt*mol.num
       vikt=vikt+tempvikt #Adds all branches

    else:
       vikt += hashtabell.search(mol.atom).vikt
       if mol.next == None:
          return vikt

    if mol.next != None:
        return(recursiveWeigth(mol.next, hashtabell, vikt))

    return vikt

def main(molecule):
    global openlefts  # Keeps track of closed or open parenthesis.
    openlefts = 0
    atomlist = readfile()  # Necessary to check if the given atom is a real atom.
    global binaryatomlist
    binaryatomlist = binarysort(atomlist)

    try:
        mol = readformula(molecule)  # I mol finns hela molekylsekvensen.
        print(weigth(mol))
        mg = Molgrafik()
        mg.show(mol)
        print('Formeln är syntaktiskt korrekt')
    except GrammarError as incorrect:
        print(str(incorrect))

if __name__ == '__main__':
    for row in sys.stdin:
        row = row.strip()
        if row != "#":
            openlefts = 0
            main(row)
        else:
            break
