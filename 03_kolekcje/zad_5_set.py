'''
5▹ Porównaj zachowanie discard() vs remove() dla typu set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)
Remove element elem from the set if it is present.
'''

example_set = {1, 2, 3, 4, 5, 'e', 'r', 'xyz'}
print(example_set.discard(1))
print(example_set.discard(5))
print('Discard: ', example_set)

example_set2 = {1, 2, 3, 4, 5, 'e', 'r', 'xyz'}
print(example_set2.remove(1))
print(example_set2.remove(5))
#print(example_set2.remove(10)) #return KeyError: 10
print('Remove: ', example_set2)
