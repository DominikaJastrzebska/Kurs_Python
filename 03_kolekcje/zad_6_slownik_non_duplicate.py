'''
6▹ Utwórz listę zawierającą wartości słownika, bez duplikatów.
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31}
'''

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31}
days_s = set(days.values())
print(days_s)
days_l = list(days_s)
print(days_l)