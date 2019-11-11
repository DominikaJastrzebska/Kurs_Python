print('Testowy moduł')
print('Wartość zmiennej "__name__" to:', __name__)

if __name__ == "__main__":
    print ('Plik uruchomiony bezpośrednio')
else:
    print ('Plik zaimportowano jako moduł')
