def print_segment(n, total_width):
    for size in range(1, n+1, 2):
        print((size * '*').center(total_width))


def print_tree(size):
    for i in range(3, size+1, 2):
        print_segment(i, size)


print('Choose size of the Christmas tree: ')
n = int(input())
print_tree(n)

