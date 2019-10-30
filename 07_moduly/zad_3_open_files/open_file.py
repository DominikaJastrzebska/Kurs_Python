def open_files():
    filename = input('Give me a file name: ')
    with open(filename, 'r') as f:
        f.read()