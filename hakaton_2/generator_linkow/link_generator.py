# https://helion.pl

# https://helion.pl/ksiazki/jak-naprawic-sprzet-elektroniczny-poradnik-dla-nieelektronika-wydanie-ii-michael-jay-geier,janas2.htm#format/d

import write_links_to_file


def transform_main_page_link(number_id, link):
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


def transform_product_page(partner_id, link, domain):
    ident = get_ident(link)
    link_new = domain + '/view/' + partner_id + '/' + ident
    return link_new


def transform_category_page(partner_id, link, domain):
    components = split_links(link)
    end_category = ''
    for index, element in enumerate(components):
        if components[index] == 'kategorie':
            end_category = '/page/' + components[index] + '/' + components[index + 1]
    link_new = domain + '/' + partner_id + end_category
    return link_new


def transform_basket_page(partner_id, link, domain):
    link_new = domain + '/add/' + partner_id
    return link_new


def is_id_number(number):
    if not number.isdigit():
        print('Podaj same cyfry')
        return False
    else:
        if len(number) != 5:
            print('Dlugosc powinna wynosic 5')
            return False
        else:
            return True


def get_partner_num():
    while True:
        partner_id = input('Podaj swoj numer id: ')
        if is_id_number(partner_id):
            break

    return partner_id


def get_link():
    link = input('Podaj link: ')
    return link


def another_link():
    question = input('Czy chcesz podac kolejny link? y/n ')
    if question.lower() == 'y':
        return True
    else:
        return False


# def main():
#     domain = 'https://helion.pl'
#     partner_id = get_partner_num()
#     link_page = get_link()
#     if link_page == 'https://helion.pl':
#         main_page(partner_id, link_page)
#         print('strona glowna')
#     elif 'ksiazki' in link_page:
#         product_page(partner_id, link_page, domain)
#         'strona ksiazki'
#     elif 'kategorie' in link_page:
#         category_page(link_page, domain, partner_id)
#         print('strona kategorie')
#     elif 'zakupy' in link_page:
#         basket_page(link_page, domain, partner_id)
#         print('strona zakupy')
#
#     while True:
#         # czy chcesz podac t/n
#         #jesli tak -> wywołaj funkcje
#         # nie -> break
#     another_link()


def main():
    domain = 'https://helion.pl'
    partner_id = get_partner_num()

    while True:
        link_page = get_link()
        # if 'helion.pl' in link_page:
        #     url = main_page(partner_id, link_page)
        #     print('glowna', url)
        # url = ''
        if link_page == 'https://helion.pl ':
            url = transform_main_page_link(partner_id, link_page)
            print('Strona główna', url)
        elif 'ksiazki' in link_page and 'kategorie' not in link_page:
            url = transform_product_page(partner_id, link_page, domain)
            print('Strona produktu - ksiazki', url)
        elif 'kategorie' in link_page:
            url = transform_category_page(partner_id, link_page, domain)
            print('Strona kategorie', url)
        elif 'zakupy' in link_page:
            url = transform_basket_page(partner_id, link_page, domain)
            print('Strona zakupy', url)

        write_links_to_file.write_links_to_file(partner_id, link_page, domain, url)

        # with open('links.csv', 'a') as f:
        #     f.writelines(f'\n{link_page}, {url}')

        if not another_link():
            break

    # while True:
    # # czy chcesz podac t/n
    # # jesli tak -> wywołaj funkcje
    # # nie -> break
    # another_link()


if __name__ == '__main__':
    main()
