import sys


filename = sample.in
for row in sa:
    ab = row.split()
    a = int(ab[0])
    b = int(ab[1])
    print(abs(a - b))