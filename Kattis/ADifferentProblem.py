import sys

for row in sys.stdin:
    ab = row.split()
    a = int(ab[0])
    b = int(ab[1])
    print(abs(a - b))
