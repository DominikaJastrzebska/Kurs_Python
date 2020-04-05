filename = 'text.txt'

# with open(filename, 'r') as f: #r jest domyslne do odczytu tutaj juz nie trzeba zamykac
#     content = f.read() #bo python sam zamyka ten plik
#     print(content)
#
# print('Koniec')
#
# f = open(filename)
# print(f.read())
# f.close()

# with open('text.txt', 'r') as fopen:
#     # print(fopen.readlines())
#     while True:
#         current_line = fopen.readline()
#
#         if current_line == '':
#             break
#         print(current_line)

with open ('text.txt', 'r') as fopen:
    list_of_lines = fopen.readlines()
print(list_of_lines)
print('--------------------------')

#operuje juz tylko na zwyklej liscie
for i in range(len(list_of_lines)):
    print(f'Linia {i}:', list_of_lines[i].strip('\n'), end='*')

# with open('save.txt', 'w') as f:
#     f.write('Line 1\n')
#     f.write('Line 2\n')
#     f.write('Line 3\n')
#     f.write('Line 4\n')

with open('text.txt', 'r', encoding='cp1252') as fopen:
    content = fopen.read()
print(content)