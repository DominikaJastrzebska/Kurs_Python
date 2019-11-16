def is_id_number(number):
    if not number.isdigit():
        return False
    else:
        if len(number) != 5:
            print('Dlugosc powinna wynosic 5')
            return False
        else:
            return True


def get_partner_num():
    while True:
        partner_id = input('Podaj swoj numer id:')
        if is_id_number(partner_id):
            break

    return partner_id


num_partera = get_partner_num()
print(num_partera)
