import unittest

from lab8 import *


class SyntaxTest(unittest.TestCase):

    def testCorrectAtom(self):
        # Testing a correct atom according to the rules.
        self.assertEqual(checkSyntax("Ch9"), 'Woop, woop, following the syntax')
        self.assertEqual(checkSyntax("Xa99"), 'Woop, woop, following the syntax')

    def testNoncorrectAtomletter(self):
        # Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("cr6"), 'Not upper case: c')
        self.assertEqual(checkSyntax("CH9"), 'Not lower case: H')

    def testNoncorrectAtomnumber(self):
        # Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("Cr0"), 'First number is too small: 0')
        self.assertEqual(checkSyntax("Cr-"), 'Not an integer: -')


if __name__ == '__main__':
    unittest.main()
