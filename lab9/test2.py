import unittest

from lab9_2 import *

class SyntaxTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(main("C(Xx4)5"), 'Okänd atom vid radslutet 4)5')

    def test2(self):
        self.assertEqual(main("C(OH4)C"), 'Saknad siffra vid radslutet C')

    def test3(self):
        self.assertEqual(main("C(OH4C"), 'Saknad högerparentes vid radslutet ')

    def test4(self):
        self.assertEqual(main("H2O)Fe"), 'Felaktig gruppstart vid radslutet )Fe')

    def test5(self):
        self.assertEqual(main("H0"), 'För litet tal vid radslutet ')

    def test6(self):
        self.assertEqual(main("H1C"), 'För litet tal vid radslutet C')

    def test7(self):
        self.assertEqual(main("H02C"), 'För litet tal vid radslutet 2C')

    def test8(self):
        self.assertEqual(main("Nacl"), 'Saknad stor bokstav vid radslutet cl')

    def test9(self):
        self.assertEqual(main("a"), 'Saknad stor bokstav vid radslutet a')

    def test10(self):
        self.assertEqual(main("(Cl)2)3"), 'Felaktig gruppstart vid radslutet )3')

    def test11(self):
        self.assertEqual(main(")"), 'Felaktig gruppstart vid radslutet )')

    def test12(self):
        self.assertEqual(main("2"), 'Felaktig gruppstart vid radslutet 2')

if __name__ == '__main__':
    unittest.main()

''''
Sample input:
C(Xx4)5
C(OH4)C
C(OH4C
H2O)Fe
H0
H1C
H02C
Nacl
a
(Cl)2)3
)
2
#


Sample output:
Okänd atom vid radslutet 4)5
Saknad siffra vid radslutet C
Saknad högerparentes vid radslutet
Felaktig gruppstart vid radslutet )Fe
För litet tal vid radslutet
För litet tal vid radslutet C
För litet tal vid radslutet 2C
Saknad stor bokstav vid radslutet cl
Saknad stor bokstav vid radslutet a
Felaktig gruppstart vid radslutet )3
Felaktig gruppstart vid radslutet )
Felaktig gruppstart vid radslutet 2
'''
