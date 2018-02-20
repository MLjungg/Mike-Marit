Analys:

Vår hypotes:
linjärsökning är O(n)
quicksort. är O(nlog(n))
binary är O(log2(n))
dictionary är O(1)

antal element = 100
l = 0.015
q = 0.005s
b = 0.0062
d = 0.0002s

antal element = 1000
l = 0.0721s
q = 0.0066 s
b = 0.0033 s
d = 0.0003 s

antal element = 10 000
l = 0.6743
q = 0.1038
b = 0.0046
d = 0.0002s

antal element = 100 000
l = 1.6495
q = 1.5594
b = 0.0039
d = 0.0002

antal element = 1 000 000 
linjär = 14.015s
quicksort = 25.4496 s
binary = 0.0068 s
dictionary = 0.0003 s

Resultat:
Linjärsökning = 10 våra värden mellan 8-9.4 så relativt linjärt
Quicksorting = 15 våra värden ca 14 så följer nlogn
binary = 1.5 våra värden mellan 0.8-1.82 följer log2(n)
dictionary= konstant	våra värden är typ konstanta.
