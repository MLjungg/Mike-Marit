import unittest

from lab9_2 import *

class SyntaxTest(unittest.TestCase):

    def testCorrectAtom1(self):
        # Testing a correct atom according to the rules.
        self.assertEqual(main("Na"), 'Formeln är syntaktiskt korrekt')

    def testCorrectAtom2(self):
        # Testing a non-correct atomletter according to the rules.
        self.assertEqual(main("Si(C3(COOH)2)4(H2O)7"), 'Formeln är syntaktiskt korrekt')
        self.assertEqual(main("Na332"), 'Formeln är syntaktiskt korrekt')

if __name__ == '__main__':
    unittest.main()

    ''''
    Sample input:
    Na
    H2O
    Si(C3(COOH)2)4(H2O)7
    Na332

    Sample output:
    Formeln är syntaktiskt korrekt
    Formeln är syntaktiskt korrekt
    Formeln är syntaktiskt korrekt
    Formeln är syntaktiskt korrekt
    '''
