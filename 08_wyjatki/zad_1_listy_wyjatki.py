'''
1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj
wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
'''

my_list = [1, '@', 'jhgfy', {1, 2, 3}, '-', '?', 2, 0, (1, 2, 3), True, False, ['a', 'b', 'v'], 2+3j, {'pl': 'poland', 'en': 'england'}]

for element in my_list:
    try:
        result = 10 / element
    except (TypeError, ZeroDivisionError, ValueError) as e:
        result = 'Wyjatek: ' + str(e)
    except Exception:
        result = 'Inny blad' + e
    print(element, result)
