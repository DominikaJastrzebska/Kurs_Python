import this
from typing import List

zmienna_this = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

quantity = zmienna_this.count('better')
print('Liczba wystapien slowa "better" to: ', quantity)

zmienna_this_without_star = zmienna_this.replace('*', '')
print('Import this bez gwiazdki: ', zmienna_this_without_star)

zmienna_replace = zmienna_this.replace('explain', 'understand', 1)
print('Zmiana explain na understand: ', zmienna_replace)

zmienna_myslnik = zmienna_this.replace(' ', '-')
print('Zamiana spacji na myslnik: ', zmienna_myslnik)

zmienna_kropka = zmienna_this.split('.')
print('Zmiana na linie z kropka: ', zmienna_kropka)


