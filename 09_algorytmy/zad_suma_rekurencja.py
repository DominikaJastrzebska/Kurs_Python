def suma_for(N):
    s = 0
    for i in range(1, N+1):
        s = s + i
    return s


print("Suma - for: ", suma_for(10))


def suma_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n-1
    return s


print('Suma while: ', suma_while(10))


def suma_recursion(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursion(n-1)


print('Suma rekurencyjnie:', suma_recursion(10))

