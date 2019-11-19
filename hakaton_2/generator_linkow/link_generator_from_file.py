import transform_page
import write_links_to_file


def get_link():
    """Returns user link"""
    link = input('Enter a link: ')
    return link


def is_partner_id(number):
    """Returns bool: True for success, False otherwise"""
    if not number.isdigit():
        print('Put only digits.')
        return False
    else:
        if len(number) != 5:
            print('Put exactly 5 digits!')
            return False
        else:
            return True


def get_partner_id():
    """Returns partner id number"""
    while True:
        partner_id = input('Enter your id partner number: ')
        if is_partner_id(partner_id):
            break
    return partner_id


def get_filename():
    filename = input('Enter a filename: ')
    return filename


def read_links_from_file(filename):
    """Returns list of links from file"""
    with open(filename, 'r') as f:
        links = f.readlines()
        for index, link in enumerate(links):
            links[index] = link.strip()
    return links


def get_ident(link, components_of_link):  # jesli pierwsza linia w pliku jest pusta, to wyrzuca blad, co tutaj trzeba zrobic?
    # components_of_link = split_links(link)
    colon_index = ''
    dot_index = ''
    for component in components_of_link:
        if ',' and '.' in component:
            string_with_ident = component
            colon_index = string_with_ident.find(',')
            dot_index = string_with_ident.find('.')
    ident = string_with_ident[colon_index + 1: dot_index]
    return ident


def split_links(link):
    link_split = link.split('/')
    return link_split


# filename = get_filename()
# read_links_from_file(filename)
# get_partner_id()


def main():
    filename = get_filename()
    list_links = read_links_from_file(filename)
    partner_id = get_partner_id()
    domain = 'https://helion.pl'

    for link in list_links:
        components_of_link = split_links(link)
        ident = get_ident(link, components_of_link)
        # ident = get_ident(link, components_of_link)
        if link == 'https://helion.pl':
            url = transform_page.transform_main_page_link(partner_id, link)
            print('Strona główna', url)
        elif 'ksiazki' in link and 'kategorie' not in link:
            url = transform_page.transform_product_page(partner_id, link, domain, ident)
            print('Strona produktu - ksiazki', url)
        elif 'kategorie' in link:
            url = transform_page.transform_category_page(partner_id, link, domain, components_of_link)
            print('Strona kategorie', url)
        elif 'zakupy' in link:
            url = transform_page.transform_basket_page(partner_id, link, domain)
            print('Strona zakupy', url)

        write_links_to_file.write_links_to_file(partner_id, link, domain, url)


if __name__ == '__main__':
    main()
