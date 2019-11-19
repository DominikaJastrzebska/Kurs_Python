
def transform_main_page_link(number_id, link):
    end_main_page = '/view/' + number_id
    link_new = link + end_main_page
    # link_new = link.replace(' ', '') + end_main_page
    return link_new


def transform_product_page(partner_id, link, domain, ident):
    # ident = get_ident(link)
    link_new = domain + '/view/' + partner_id + '/' + ident
    return link_new


def transform_category_page(partner_id, link, domain, components):
    # components = split_links(link)
    end_category = ''
    for index, element in enumerate(components):
        if components[index] == 'kategorie':
            end_category = '/page/' + components[index] + '/' + components[index + 1]
    link_new = domain + '/' + partner_id + end_category
    return link_new


def transform_basket_page(partner_id, link, domain):
    link_new = domain + '/add/' + partner_id
    return link_new


