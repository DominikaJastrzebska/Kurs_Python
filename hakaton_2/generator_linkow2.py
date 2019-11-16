# https://helion.pl

# https://helion.pl/ksiazki/jak-naprawic-sprzet-elektroniczny-poradnik-dla-nieelektronika-wydanie-ii-michael-jay-geier,janas2.htm#format/d


def is_id_number(partner_id):
    if partner_id.isdigit():
        if len(partner_id) == 5:
            print('Prawidlowy format')
        else:
            print('Podaj dokladnie 5 cyfr')
    else:
        print('Podaj tylko cyfry')


def main_page(number_id, link):
    end_main_page = '/view/' + number_id
    link_new = link.replace(' ', '') + end_main_page
    return link_new


def split_links(link):
    link_split = link.split('/')
    return link_split


def get_ident(link):
    components_of_link = split_links(link)
    colon_index = ''
    dot_index = ''
    for component in components_of_link:
        if ',' and '.' in component:
            string_with_ident = component
            colon_index = string_with_ident.find(',')
            dot_index = string_with_ident.find('.')
    ident = string_with_ident[colon_index + 1:dot_index]
    return ident


def product_page(partner_id, link, domain):
    ident = get_ident(link)
    link_new = domain + '/view/' + partner_id + '/' + ident
    return link_new


def category_page(link, domain, partner_id):
    end_category = '/kategorie/programowanie'
    link_new = domain + '/page/' + partner_id + end_category
    return link_new


def basket_page(link, domain, partner_id):
    link_new = domain + '/add/' + partner_id
    return link_new


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


def get_link():
    link = input('Podaj link: ')
    return link


def another_link():
    question = input('Czy chcesz podac kolejny link? y/n')
    while True:
        if question.lower() == 'y':
            get_link()
        else:
            print('Koniec podawania linkow')


def main():
    domain = 'https://helion.pl'
    partner_id = get_partner_num()
    link_page = get_link()
    if link_page == 'https://helion.pl':
        main_page(partner_id, link_page)
        print('strona glowna')
    elif 'ksiazki' in link_page:
        product_page(partner_id, link_page, domain)
        'strona ksiazki'
    elif 'kategorie' in link_page:
        category_page(link_page, domain, partner_id)
        print('strona kategorie')
    elif 'zakupy' in link_page:
        basket_page(link_page, domain, partner_id)
        print('strona zakupy')
    another_link()


if __name__ == '__main__':
    main()

