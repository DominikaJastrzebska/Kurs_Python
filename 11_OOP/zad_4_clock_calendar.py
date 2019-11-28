'''
4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc
podawać aktualną datę oraz wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania
tak, aby zegaro-kalendarz zawierał datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia
przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.
Utwórz obiekty, które będą przekazywać różne strefy czasowe i wyświetlać dzięki temu inne czasy zegara.
'''

import datetime


class Clock:
    def __init__(self):
        print('Clock', datetime.time())

    def current_time(self):
        return datetime.datetime.now().time()


class Calendar:
    def __init__(self):
        # print('Wyswietla date', datetime.date(2019, 11, 20))
        print('Calendar')

    def current_date(self):
        return datetime.datetime.now().date()

    def show_calendar(self):
        # datetime modul calendar
        for i in range(1, 31):
            if i % 7 == 0:
                print(i)
            else:
                print(i, end=' ')


class ClockCalendar(Clock, Calendar):
    # def __init__(self):
    #     pass
    def current_date_time(self):
        print(super().current_date())
        print(super().current_time())
        # print('Wyswietla date i czas', datetime.date.today(), datetime.datetime.now())
        # Clock.__init__(self)
        # Calendar.__init__(self)


Clock()
Calendar()
zk = ClockCalendar()
# print(zk.current_time())
zk.current_date_time()
zk.show_calendar()
