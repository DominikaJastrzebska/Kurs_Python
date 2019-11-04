filename = 'text.txt'

with open(filename, 'r', encoding="utf-8") as f:
    content = f.read() #read tworzy string, a readlines tworzy liste

content = content.split()

word_list = []

for element in content:
    element = element.replace(',', '').replace('.', '').replace('!', '')
    word_list.append(element)
    print('Element: ', element)
    #word_list.append(element)
print(word_list)

lenght = 0
longest_word = ''
for element in content:
    if len(element) > lenght:
        lenght = len(element)
        longest_word = element
print('Lenght: ', lenght, longest_word)
