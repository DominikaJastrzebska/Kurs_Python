# name_woman = input('Enter woman\'s name: ')
# name_man = input('Enter man\'s name: ')


names_love = 'DomilovesDarek'
names_love = names_love.lower()
print(names_love)
numbers = []
for letter in names_love:
    numbers.append(names_love.count(letter))
    names_love = names_love.replace(letter, '')
    print(names_love)
    # print(names_love[index])
    # names_love = names_love.count(names_love[index])
print(numbers)

for number in numbers:
    if number == 0:
        numbers.remove(0)

print(numbers)

for number in numbers:
    print('number', number)
    print('numbers', numbers, len(numbers))
    print('pop', numbers.pop(0), numbers.pop())

print('lista', numbers)

lista = [1, 1, 2]
for i in lista:
    lista.pop(0) + lista.pop()
print(lista)





