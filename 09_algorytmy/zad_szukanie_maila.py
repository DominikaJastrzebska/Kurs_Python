mail_list = ['ala@wp.pl', 'lala@wp.pl', 'daria@wp.pl', 'dominika@sysbreakers.com']

my_mail = input('Podaj swoj adres email: ')

# found = False
# for element in mail_list:
#     if element == my_mail:
#         found = True
#
# if found is True:
#     print('Email wystepuje na liscie')
# else:
#     print('Email nie wystepuje na liscie')


# i = True
# while i:
#     element_pop = mail_list.pop()
#     if element_pop == my_mail:
#         print('Email na liscie')
#     else:
#         pass

def find_email(searched, emails):
    for e in emails:
        if e == searched:
            return 'Znaleziono'
        else:
            continue
    return 'Email nie istnieje'

with open('emails.txt') as file:
    email_list = email_list.split()

my_mail

def search_email(my_email, emails):
    if email in emails:
        return True
    else:
        return False