"""
2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w
środku s1.
"""

s1 = 'AliBaba23'
s2 = 'Alladin Resort'
s3 = s1[0:len(s1)//2] + s2 + s1[len(s1)//2:len(s1)]

print(s3)