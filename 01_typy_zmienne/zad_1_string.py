"""
1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z
trzech środkowych znaków danego ciągu.
"""

word = 'armagedon'
word_len = len(word)
middle = word_len//2
print(word_len)
print(word[middle-1:middle+2])
