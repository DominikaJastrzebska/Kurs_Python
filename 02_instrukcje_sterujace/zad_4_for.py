N = int(input('Podaj liczbe naturalna: '))
if N <=8:
    i = 0
    for i in range (1,N):
        if i == 0:
            print(str(i)+'!=1')
        else:
            i = i * i
            print(str(N)+'!='+str(i))