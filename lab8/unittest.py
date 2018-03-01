import unittest

from lab8 import *

class SyntaxTest(unittest.TestCase):

    def testCorrectAtom(self):
        #Testing a correct atom according to the rules.
        self.assertEqual(checkSyntax("Ch9"), 'Woop woop, follow the syntax')

    def testNoncorrectAtomletter(self):
        #Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("cr6"), 'Not upper case: c')
    def testNoncorrectAtomletter(self):
        #Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("CH9"), 'Not lower case H')

    def testNoncorrectAtomnumber(self):
        #Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("Cr0"), 'Too small integer: 0')

    def testNoncorrectAtomnumber(self):
        #Testing a non-correct atomletter according to the rules.
        self.assertEqual(checkSyntax("Cr-"), 'Not an integer: -')	    


if __name__ == '__main__':
	unittest.main()
