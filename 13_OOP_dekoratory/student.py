import datetime
import holidays


class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property  # uzywamy metody jako atrybutu, bez uzywania osobnych nawiasow do wywolania
    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    # def set_min_avg(self, new_avg): trzeba wywolywac na kazdym obiekcie aby zmienio kazdemu srednia
    #     self.min_avg = new_avg

    @classmethod  # metoda wykona sie dla calej naszej klasy
    def set_min_avg(cls, new_avg):
        cls.min_avg = new_avg

    @staticmethod  # nie potrzebuje miec danych ani dostepu do danych, moglaby istniec poza klasa, ale jest z klasa powiazana
    def academic_football_team_chear(nr):  # jesli nie byloby tutaj dekoratora to trzebaby dodac self
        return 'Go go NYA ' * nr

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6 or day in holidays.US():
            return 'Nie'
        else:
            return 'Tak'


obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)

print(obj_anna.min_avg)
print(Student.min_avg)

obj_anna.set_min_avg(3.0)
print(obj_anna.min_avg)
print(Student.academic_football_team_chear(4))
print(obj_anna.email)

today = datetime.date.today()
another_day = datetime.date(2020, 1, 1)
print('Czy dzisiaj są zajęcia? ', Student.academic_day(another_day))
print(today)

pl_holidays = holidays.Poland()
print(pl_holidays)

if '1/1/2019' in pl_holidays:
    print('Tak')

print(pl_holidays.get('2019-01-06'))

print(datetime.date(2019, 11, 30))