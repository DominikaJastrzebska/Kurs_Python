import os.path, os

filename = input('Give me a file name: ')


def open_files(exists, name):
    if not exists:
        return False
    else:
        with open(name, 'r') as f:
            content = f.read()
        print('ok')


def write_file(name):
    with open(name, 'a') as f:
        f.write('\nTralala')


if_exists = False
if os.path.exists(filename):
    if_exists = True
    if os.stat(filename).st_size != 0:
        print('File exists, it\'s not empty')
        if_exists = True
    else:
        print('File exists, but it\'s empty')
else:
    print('File doesn\'t exist')


open_files(if_exists, filename)
write_file(filename)





# filename = input('Give me a file name: ')
#
#
# def open_file(filname):
#     try:
#         with open (filename, 'r') as f:
#             f.read()
#         print('File exists')
#     except FileNotFoundError: #FilexistError
#         print('File doesn\'t exist')
#
#



# open_file(filename)