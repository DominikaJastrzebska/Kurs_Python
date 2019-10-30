rows = 7
col = 2

print([['*']*col]*rows)

print(['*']*rows*col)

print([['*']*col for i in range(rows)])

print([['*']*rows for i in range(col)])

#print([['*']*rows]*[col])

# items = {1, 2, 3}
#
# print(items[0])


eclipse = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(eclipse[-1:-4:-1].reverse())