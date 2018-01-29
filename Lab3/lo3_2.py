# -*- coding: utf-8 -*-

from bintreefile import Bintree

svenska = Bintree()
with open("word3.txt", "r") as svenskfil:

    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet)
        else:
            svenska.addToTree(ordet)             # in i sökträdet
print("\n")