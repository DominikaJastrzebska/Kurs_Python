'''
https://stackoverflow.com/questions/33624221/make-a-yearly-calendar-without-importing-a-calendar
'''


data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
]


# for i in range(len(data)):
#     print(data[i][0])
#     days = []
#     for x in range(7):
#         for j in data[i][1]:
#             print(j, end=' ')

def make_simple_calendar():
    for month, days in data:
        print(month)
        start_day = 0
        for day in days:
            if day <= 9:
                print('0'+str(day), end=' ')
            else:
                print('{0:<3}'.format(day), end='')
            start_day += 1
            if start_day == 7:
                print()
                start_day = 0
        print()
        print()


make_simple_calendar()