# def get_partner_id():
#     partner_id = input('Podaj swoj numer id, jesli chcesz przerwac, wpisz q')
#     return partner_id
#
#
# def get_link():
#     link = input('Wklej skopiowany link: ')
#     return link

partner_id = input('Podaj swoj numer id, jesli chcesz przerwac, wpisz q')
link = input('Wklej skopiowany link: ')


# def is_id(id_partner):
#     if len(id_partner) == 5 and id_partner.isdigit():
#         return True
#     else:
#         return False
#

# number = get_partner_id()

# can_be_id = False
#
#
# if is_id(number):
#     pass
# else:
#     while True:
#         id = get_partner_id()
#         if id == 'q':
#             break
# strona glowna linki
# input: https://helion.pl/
# output: https://helion.pl/view/90412

# Strona produktu
# input: https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d
# output: https://helion.pl/view/90412/algoip

# strona kategorii linki
# input: https://helion.pl/kategorie/programowanie
# output: https://helion.pl/page/90412/kategorie/programowanie

# strona zakupy
# https://helion.pl/zakupy/edit.cgi
# nalezy sciagnac id z poszczegolnych ksiazek
# input: https://helion.pl/ksiazki/jak-naprawic-sprzet-elektroniczny-poradnik-dla-nieelektronika-wydanie-ii-michael-jay-geier,janas2.htm#format/d
# output: https://helion.pl/add/90412/janas2


def main_page(partner_id, link):
    # number = get_partner_id()
    # link = get_link()  # 'https://helion.pl'
    end_main_page = '/view/' + partner_id
    link_new = link.replace(' ', '') + end_main_page
    return link_new


def split_links():
    link = get_link()
    link_split = link.split('/')
    return link_split


def get_ident():
    components_of_link = split_links()
    colon_index = ''
    dot_index = ''
    for component in components_of_link:
        if ',' and '.' in component:
            string_with_ident = component
            colon_index = string_with_ident.find(',')
            dot_index = string_with_ident.find('.')
    ident = string_with_ident[colon_index + 1:dot_index]
    print(ident)
    return ident


def product_page():
    ident = get_ident()
    maine_page = 'https://helion.pl' + '/view/'
    link_new = maine_page + ident
    return link_new


def category_page():
    ident = get_ident()



# print(colon_index, dot_index)


print(main_page(partner_id, link))


# print(product_page())
