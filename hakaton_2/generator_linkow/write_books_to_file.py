#
# link = 'https://helion.pl/ksiazki/czysty-kod-podrecznik-dobrego-programisty-robert-c-martin,czykov.htm#format/d'
#
#
# def split_links_to_title():
#     link_splited = link.split('/')
#     return link_splited


def write_links_to_file(partner_id, link_page, domain, url):
    with open('links.csv', 'a') as f:
        f.writelines(f'\n{link_page}, {url}\n')

