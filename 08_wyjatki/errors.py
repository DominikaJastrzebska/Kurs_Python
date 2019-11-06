import sys

# result = 'hello' + 4
# odp = input('alala', 3, 1)
# res = 4 / 0
# name = Rita

# f = open('lalala.txt')
# content = f.read()


# weight = float(input('Give me a weight: '))
# height = float(input('Give me a height: '))
# bmi = 'nie zdefiniowano'
# try:
#     bmi = weight / height ** 2
# except ZeroDivisionError:
#     print('Nie dziel przez zero')
#     # bmi = 0
# print(round(bmi, 2))


# try:
#     x = float(input('Podaj liczbe: '))
#     result = 4/x
# except ValueError as e:
#     # handle ValueError exception
#     print('VE', e)
# except (TypeError, ZeroDivisionError) as e:
#     print(e)
# except:
#     # handle all other exceptions
#     print('Nie mam pojęcia jakim jestem błędem!')

# try:
#     x = float(input('Podaj liczbe: '))
#     result = 4/x
# except Exception as e:
#     print('E', e)

# try:
# #     x = float(input('Podaj liczbe: '))
# #     result = 4/x
# # except:
# #     pass

# try:
#     x = 5 / 0
# except ZeroDivisionError as e:
#     print("Nie dziel przez zero! Twój wyjątek to:", e)
#     x = 0 # potrzebujemy x więc go nadpiszemy
# finally:
#     print ("Zawsze się wyświetlę")
#     print(x + 4)

# try:
#     x = float(input('Podaj liczbe: '))
#     result = 5 / x
# except Exception as e:
#     print('Blad to: ', sys.exc_info()[0])

# try:
#     x = float(input('Podaj liczbe: '))
#     result = 5 / x
# except Exception as e:
#     print('Blad to: ', type(e))

# raise KeyboardInterrupt
# raise ValueError
# raise MemoryError

# print('Początek programu')
# raise Exception('To jest ogólny wyjątek')
# print('Koniec programu')

# def hello_exception():
#     print('Początek programu')
#     raise ArithmeticError('To jest blad arytmetyczny')
#     print('Koniec programu')
# try:
#     hello_exception()
# except ArithmeticError as ex:
#     print('Oh nie blad', ex)
#     print(sys.exc_info())
# except:
#     print('Inny blad')


def predict_future():
    num = int(input("Podaj dowolną liczbę naturalną: "))
    if num < 0:
        raise ValueError("To nie jest liczba naturalna!")
    else:
        print("Za", 10 * num, "ludzkość będzie mogła się teleportować")


try:
    predict_future()
except ValueError as e:
    print(e)
