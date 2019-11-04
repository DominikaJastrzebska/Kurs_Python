with open ('words.txt', 'r') as f:
    content = f.read()
    content = content.split()
    print('Content: ', content)

with open('words.txt', 'r') as f:
    lines = f.readlines()
    print('Lines: ', lines)

words_dict = {}
for line in lines:
    line = line.strip()
    line = line.split(':')
    print('Line strip', line[0], line[1])
    words_dict[line[0]] = line[1]
print(words_dict)

for key, value in words_dict.items():
    words_dict[key] = value.split(',')
print(words_dict)
