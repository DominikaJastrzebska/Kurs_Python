class Employee:

    company = 'Love Python Company'

    def __init__(self, position, salary, name, surname, seniority, is_student):
        self.position = position
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.is_student = is_student

    def salary_bump(self):
        self.salary *= 1.1
        return self.salary

    def tax(self):
        if self.salary * 12 <= 90000:
            return self.salary * 0.18
        else:
            return (90000 * 0.18) + (self.salary - 90000) * 0.32

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
        return self.salary * proc

    def employee_email(self):
        primary = self.name + '.' + self.surname
        secondary = self.company.replace(' ', '').lower()
        email = primary + '@' + secondary + '.com'
        return email

    def employee_email_consonant(self):
        VOWELS = ['x', 'a', 'e', 'y', 'u', 'i', 'o']
        human_name = self.name.lower() + self.surname.lower()
        human_name_consonant = ''
        for letter in human_name:
            if letter in VOWELS:
                human_name = human_name.replace(letter, '')
                human_name_consonant = human_name
        domain = self.company.lower().replace(' ', '')
        email = human_name_consonant + '@' + domain + '.com'
        return email


p1 = Employee('programista', 5500, 'Jan', 'Kowalski', 3, False)
print(p1.name)
print(p1.salary)
print(p1.salary_bump())
print(p1.salary)
print(p1.tax())
print(p1.health_care())
print(p1.company)
print(p1.employee_email())
print(p1.employee_email_consonant())