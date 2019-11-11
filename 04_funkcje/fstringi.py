name = 'Domi'
fav_color = 'red'

print("I'm", name, "my favorite color is", fav_color)
print("I'm {} my favorite color is {}".format(name, fav_color))
print(f"I'm {name} my favorite color is {fav_color}")


def list_my_numbers():
    txt_list = ""
    for i in range(20):
        txt_list += str(i) + " "
    return txt_list


print(f'My numbers: {list_my_numbers()}')


def list_numbers():
    for i in range(20):
        return i


print(f'num: {list_numbers()}')

print(f'My numbers: {list_my_numbers()}')